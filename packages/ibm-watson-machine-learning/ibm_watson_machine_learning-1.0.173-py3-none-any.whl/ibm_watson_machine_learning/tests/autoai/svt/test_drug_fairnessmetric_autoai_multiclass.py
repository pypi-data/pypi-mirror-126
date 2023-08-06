#  (C) Copyright IBM Corp. 2021.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import unittest
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression as LR
from sklearn.tree import DecisionTreeClassifier as Tree
from sklearn.neighbors import KNeighborsClassifier as KNN

from lale.lib.lale import Hyperopt
from lale import wrap_imported_operators

from pprint import pprint
import pandas as pd
from os import environ

from ibm_watson_machine_learning import APIClient

from ibm_watson_machine_learning.experiment import AutoAI
from ibm_watson_machine_learning.deployment import WebService

from ibm_watson_machine_learning.helpers.connections import S3Connection, S3Location, DataConnection, FSLocation

from ibm_watson_machine_learning.tests.utils.utils import get_wml_credentials, get_cos_credentials, bucket_exists, \
    bucket_name_gen, get_space_id, is_cp4d
from ibm_watson_machine_learning.tests.utils.cleanup import bucket_cleanup, space_cleanup
from ibm_watson_machine_learning.utils.autoai.enums import PositiveLabelClass, TShirtSize

from ibm_watson_machine_learning.utils.autoai.errors import MissingPositiveLabel, AutoAIComputeError

from lale.operators import TrainablePipeline
from ibm_watson_machine_learning.helpers import pipeline_to_script


@unittest.skip("Fairness metric is not yet supported")
class TestAutoAIRemote(unittest.TestCase):
    """
    The test covers:
    - connections preparing
    - optimizer with fairness info and accuracy scorer set up
    - training of the optimizer
    - results checking
    - optimizer with fairness info and fairness scorer set up
    - training of the optimizer
    - summary checking
    - deployment of the last created optimizer
    """
    wml_client: 'APIClient' = None
    experiment: 'AutoAI' = None
    remote_auto_pipelines = None
    hyperopt_pipelines = None
    prefix = None
    new_pipeline = None
    mitigated_pipeline = None
    wml_credentials = None
    cos_credentials = None
    pipeline_opt = None
    service: 'WebService' = None

    data_location = './autoai/data/drug_train_data_updated.csv'
    target_column = 'DRUG'

    trained_pipeline_details = None
    run_id = None

    data_connection = None
    results_connection = None

    train_data = None

    cos_endpoint = "https://s3.us-south.cloud-object-storage.appdomain.cloud"
    if "BUCKET_NAME" in environ:
        bucket_name = environ['BUCKET_NAME']
    else:
        bucket_name = "wml-autoaitests-qa"

    pod_version = environ.get('KB_VERSION', None)
    space_name = environ.get('SPACE_NAME', 'regression_tests_sdk_space')

    data_cos_path = 'data/drug_train_data_updated.csv'
    cos_resource_instance_id = None

    results_cos_path = 'results_wml_autoai'

    best_pipeline: 'Pipeline' = None
    deployed_pipeline = None

    fairness_info = {
        "protected_attributes": [
            {"feature": "SEX", "privileged_groups": ['F']},
            {"feature": "BP", "privileged_groups": ["LOW", "NORMAL"]}
        ],
        "favorable_labels": ["drugA", "drugC"]
    }

    OPTIMIZER_NAME = 'Drug Data AutoAI with fairness SDK test'
    DEPLOYMENT_NAME = "Drug Data AutoAI with fairness SDK test Deployment "

    space_id = None
    project_id = None

    summary = None

    asset_id = None

    @classmethod
    def setUpClass(cls) -> None:
        """
        Load WML credentials from config.ini file based on ENV variable.
        """
        cls.data = pd.read_csv(cls.data_location)
        cls.X = cls.data.drop([cls.target_column], axis=1)
        cls.y = cls.data[cls.target_column]

        wrap_imported_operators()

        cls.wml_credentials = get_wml_credentials()

        cls.wml_client = APIClient(wml_credentials=cls.wml_credentials)
        if not cls.wml_client.ICP:
            cls.cos_credentials = get_cos_credentials()
            cls.cos_endpoint = cls.cos_credentials.get('endpoint_url')
            cls.cos_resource_instance_id = cls.cos_credentials.get('resource_instance_id')

        cls.project_id = cls.wml_credentials.get('project_id')

    def test_00a_space_cleanup(self):
        space_cleanup(self.wml_client,
                      get_space_id(self.wml_client, self.space_name,
                                   cos_resource_instance_id=self.cos_resource_instance_id),
                      days_old=7)
        TestAutoAIRemote.space_id = get_space_id(self.wml_client, self.space_name,
                                                 cos_resource_instance_id=self.cos_resource_instance_id)

        if self.wml_client.ICP:
            self.wml_client.set.default_project(self.project_id)
        else:
            self.wml_client.set.default_space(self.space_id)

    def test_00b_prepare_COS_instance(self):
        if self.wml_client.ICP or self.wml_client.WSD:
            self.skipTest("Prepare COS is available only for Cloud")

        import ibm_boto3
        cos_resource = ibm_boto3.resource(
            service_name="s3",
            endpoint_url=self.cos_endpoint,
            aws_access_key_id=self.cos_credentials['cos_hmac_keys']['access_key_id'],
            aws_secret_access_key=self.cos_credentials['cos_hmac_keys']['secret_access_key']
        )
        # Prepare bucket
        if not bucket_exists(cos_resource, self.bucket_name):
            try:
                bucket_cleanup(cos_resource, prefix=f"{self.bucket_name}-")
            except Exception as e:
                print(f"Bucket cleanup with prefix {self.bucket_name}- failed due to:\n{e}\n skipped")

            import datetime
            TestAutoAIRemote.bucket_name = bucket_name_gen(prefix=f"{self.bucket_name}-{str(datetime.date.today())}")
            print(f"Creating COS bucket: {TestAutoAIRemote.bucket_name}")
            cos_resource.Bucket(TestAutoAIRemote.bucket_name).create()

            self.assertIsNotNone(TestAutoAIRemote.bucket_name)
            self.assertTrue(bucket_exists(cos_resource, TestAutoAIRemote.bucket_name))

        print(f"Using COS bucket: {TestAutoAIRemote.bucket_name}")

    def test_01_initialize_AutoAI_experiment__pass_credentials__object_initialized(self):
        TestAutoAIRemote.experiment = AutoAI(wml_credentials=self.wml_credentials.copy(),
                                             project_id=self.project_id,
                                             space_id=self.space_id)

        self.assertIsInstance(self.experiment, AutoAI, msg="Experiment is not of type AutoAI.")

    def test_02_save_remote_data_and_DataConnection_setup(self):
        if self.wml_client.ICP:
            TestAutoAIRemote.data_connection = DataConnection(
                location=FSLocation(path=self.data_location))
            TestAutoAIRemote.results_connection = None

        else:  # for cloud and COS
            TestAutoAIRemote.data_connection = DataConnection(
                connection=S3Connection(endpoint_url=self.cos_endpoint,
                                        access_key_id=self.cos_credentials['cos_hmac_keys']['access_key_id'],
                                        secret_access_key=self.cos_credentials['cos_hmac_keys']['secret_access_key']),
                location=S3Location(bucket=self.bucket_name,
                                    path=self.data_cos_path)
            )
            TestAutoAIRemote.results_connection = DataConnection(
                connection=S3Connection(endpoint_url=self.cos_endpoint,
                                        access_key_id=self.cos_credentials['cos_hmac_keys']['access_key_id'],
                                        secret_access_key=self.cos_credentials['cos_hmac_keys']['secret_access_key']),
                location=S3Location(bucket=self.bucket_name,
                                    path=self.results_cos_path)
            )
            TestAutoAIRemote.data_connection.write(data=self.data, remote_name=self.data_cos_path)

        self.assertIsNotNone(obj=TestAutoAIRemote.data_connection)

    def test_03_initialize_optimizer(self):
        from ibm_watson_machine_learning.experiment.autoai.optimizers import RemoteAutoPipelines

        TestAutoAIRemote.remote_auto_pipelines = self.experiment.optimizer(
            name=self.OPTIMIZER_NAME,
            prediction_type=AutoAI.PredictionType.BINARY,
            prediction_column=self.target_column,
            scoring=AutoAI.Metrics.ACCURACY_SCORE,
            t_shirt_size=TShirtSize.S if self.wml_client.ICP else TShirtSize.L,
            fairness_info=self.fairness_info,
            autoai_pod_version=self.pod_version,
            max_number_of_estimators=1
        )

        self.assertIsInstance(self.remote_auto_pipelines, RemoteAutoPipelines,
                              msg="experiment.optimizer did not return RemoteAutoPipelines object")

    def test_04_get_configuration_parameters_of_remote_auto_pipeline(self):
        parameters = self.remote_auto_pipelines.get_params()
        print(parameters)
        self.assertIsInstance(parameters, dict, msg='Config parameters are not a dictionary instance.')

    def test_05_fit_run_training_of_auto_ai_in_wml(self):

        TestAutoAIRemote.trained_pipeline_details = self.remote_auto_pipelines.fit(
            training_data_reference=[self.data_connection],
            training_results_reference=self.results_connection,
            background_mode=False)

        TestAutoAIRemote.run_id = self.trained_pipeline_details['metadata']['id']

        self.assertIsNotNone(self.data_connection.auto_pipeline_params,
                             msg='DataConnection auto_pipeline_params was not updated.')

        TestAutoAIRemote.train_data = self.remote_auto_pipelines.get_data_connections()[0].read()

        print("train data sample:")
        print(self.train_data.head())
        self.assertGreater(len(self.train_data), 0)

    def test_06_get_run_status(self):
        status = self.remote_auto_pipelines.get_run_status()
        self.assertEqual(status, "completed", msg="AutoAI run didn't finished successfully. Status: {}".format(status))

    def test_07_get_run_details(self):
        parameters = self.remote_auto_pipelines.get_run_details()
        # print(parameters)
        self.assertIsNotNone(parameters)

    def test_08_summary_listing_all_pipelines_from_wml(self):
        TestAutoAIRemote.summary = self.remote_auto_pipelines.summary()
        print(TestAutoAIRemote.summary)
        self.assertIn('holdout_disparate_impact', list(TestAutoAIRemote.summary.columns))

        for col in self.summary.columns:
            print(self.summary[col])

    def test_09_get_pipeline__load_lale_pipeline__pipeline_loaded(self):
        TestAutoAIRemote.best_pipeline = self.remote_auto_pipelines.get_pipeline()
        print(f"Fetched pipeline type: {type(self.best_pipeline)}")

        self.assertIsInstance(self.best_pipeline, TrainablePipeline,
                              msg="Fetched pipeline is not of TrainablePipeline instance.")
        predictions = self.best_pipeline.predict(
            X=self.train_data.drop([self.target_column], axis=1).values[:5])
        print(predictions)

    def test_10__pipeline_to_script__lale__pretty_print(self):
        pipeline_to_script(self.best_pipeline)
        pipeline_code = self.best_pipeline.pretty_print()
        exception = None
        try:
            exec(pipeline_code)

        except Exception as exception:
            self.assertIsNone(exception, msg="Pretty print from lale pipeline was not successful")

    def test_11__predict__do_the_predict_on_lale_pipeline__results_computed(self):
        y_true = self.train_data[self.target_column].values
        predictions = self.best_pipeline.predict(self.train_data.drop([self.target_column], axis=1).values)
        print(predictions)
        print('refined accuracy', accuracy_score(y_true, predictions))

    def test_12__remove_last_freeze_trainable__prefix_returned(self):
        TestAutoAIRemote.prefix = self.best_pipeline.remove_last().freeze_trainable()
        self.assertIsInstance(TestAutoAIRemote.prefix, TrainablePipeline,
                              msg="Prefix pipeline is not of TrainablePipeline instance.")

    def test_13_add_estimator(self):
        TestAutoAIRemote.new_pipeline = TestAutoAIRemote.prefix >> (LR | Tree | KNN)

    def test_14_hyperopt_fit_new_pipepiline(self):
        train_X = self.train_data.drop([self.target_column], axis=1).values
        train_y = self.train_data[self.target_column].values

        hyperopt = Hyperopt(estimator=TestAutoAIRemote.new_pipeline, cv=3, max_evals=5)
        TestAutoAIRemote.hyperopt_pipelines = hyperopt.fit(train_X, train_y)

    def test_15_get_pipeline_from_hyperopt(self):
        from sklearn.pipeline import Pipeline
        new_pipeline_model = TestAutoAIRemote.hyperopt_pipelines.get_pipeline()
        print(f"Hyperopt_pipeline_model is type: {type(new_pipeline_model)}")
        TestAutoAIRemote.new_pipeline = new_pipeline_model.export_to_sklearn_pipeline()
        self.assertIsInstance(TestAutoAIRemote.new_pipeline, Pipeline,
                              msg=f"Incorect Sklearn Pipeline type after conversion. Current: {type(TestAutoAIRemote.new_pipeline)}")

    def test_16__predict__do_the_predict_on_sklearn_pipeline__results_computed(self):
        y_true = self.train_data[self.target_column].values
        predictions = TestAutoAIRemote.new_pipeline.predict(self.train_data.drop([self.target_column], axis=1).values)
        print(predictions)
        print('refined accuracy', accuracy_score(y_true, predictions))

    ### Run training with fairness scorer

    def test_17_initialize_optimizer(self):
        from ibm_watson_machine_learning.experiment.autoai.optimizers import RemoteAutoPipelines

        TestAutoAIRemote.remote_auto_pipelines = self.experiment.optimizer(
            name=self.OPTIMIZER_NAME,
            prediction_type=AutoAI.PredictionType.BINARY,
            prediction_column=self.target_column,
            scoring=AutoAI.Metrics.ACCURACY_AND_DISPARATE_IMPACT_SCORE,
            t_shirt_size=TShirtSize.S if self.wml_client.ICP else TShirtSize.L,
            fairness_info=self.fairness_info,
            autoai_pod_version=self.pod_version
        )

        self.assertIsInstance(self.remote_auto_pipelines, RemoteAutoPipelines,
                              msg="experiment.optimizer did not return RemoteAutoPipelines object")

    def test_18_fit_run_training_of_auto_ai_in_wml(self):

        TestAutoAIRemote.trained_pipeline_details = self.remote_auto_pipelines.fit(
            training_data_reference=[self.data_connection],
            training_results_reference=self.results_connection,
            background_mode=False)

        TestAutoAIRemote.run_id = self.trained_pipeline_details['metadata']['id']

        self.assertIsNotNone(self.data_connection.auto_pipeline_params,
                             msg='DataConnection auto_pipeline_params was not updated.')

        TestAutoAIRemote.train_data = self.remote_auto_pipelines.get_data_connections()[0].read()

        print("train data sample:")
        print(self.train_data.head())
        self.assertGreater(len(self.train_data), 0)

    def test_19a_get_run_status(self):
        status = self.remote_auto_pipelines.get_run_status()
        self.assertEqual(status, "completed", msg="AutoAI run didn't finished successfully. Status: {}".format(status))

    def test_19b_get_run_details(self):
        parameters = self.remote_auto_pipelines.get_run_details()
        # print(parameters)
        self.assertIsNotNone(parameters)
        self.assertIn('metrics', str(parameters))

    def test_19c_summary_listing_all_pipelines_from_wml(self):
        TestAutoAIRemote.summary = self.remote_auto_pipelines.summary()
        print(TestAutoAIRemote.summary)
        self.assertIn('accuracy_and_disparate_impact', str(list(TestAutoAIRemote.summary.columns)))

    def test_20_predict__do_the_predict_on_lale_pipeline__results_computed(self):
        TestAutoAIRemote.mitigated_pipeline = self.remote_auto_pipelines.get_pipeline()
        print(f"Fetched pipeline type: {type(self.best_pipeline)}")
        self.assertIsInstance(self.mitigated_pipeline, TrainablePipeline,
                              msg="Fetched pipeline is not of TrainablePipeline instance.")
        predictions = self.mitigated_pipeline.predict(
            X=self.train_data.drop([self.target_column], axis=1).values[:10])
        print(predictions)
        self.assertEqual(len(predictions), 10)

    #################################
    #      DEPLOYMENT SECTION       #
    #################################

    def test_21_deployment_setup_and_preparation(self):
        TestAutoAIRemote.service = WebService(source_wml_credentials=self.wml_credentials.copy(),
                                              source_project_id=self.project_id,
                                              source_space_id=self.space_id)
        self.wml_client.set.default_space(self.space_id)
        self.assertIsNone(self.service.name)
        self.assertIsNone(self.service.id)
        self.assertIsNone(self.service.scoring_url)

    def test_22__deploy__deploy_best_computed_pipeline_from_autoai_on_wml(self):
        self.service.create(
            experiment_run_id=self.run_id,
            model="Pipeline_3",
            deployment_name=self.DEPLOYMENT_NAME)

        self.assertIsNotNone(self.service.name)
        self.assertIsNotNone(self.service.id)
        self.assertIsNotNone(self.service.asset_id)

    def test_24_score_deployed_model(self):
        nb_records = 10
        predictions = self.service.score(payload=self.train_data.drop([self.target_column], axis=1)[:nb_records])
        print(predictions)
        self.assertIsNotNone(predictions)
        self.assertEqual(len(predictions['predictions'][0]['values']), nb_records)

    def test_25_delete_deployment_and_model(self):
        print("Delete current deployment: {}".format(self.service.deployment_id))
        self.service.delete()
        self.wml_client.set.default_space(self.space_id) if not self.wml_client.default_space_id else None
        self.wml_client.repository.delete(self.service.asset_id)
        self.wml_client.set.default_project(self.project_id) if is_cp4d() else None


if __name__ == '__main__':
    unittest.main()
