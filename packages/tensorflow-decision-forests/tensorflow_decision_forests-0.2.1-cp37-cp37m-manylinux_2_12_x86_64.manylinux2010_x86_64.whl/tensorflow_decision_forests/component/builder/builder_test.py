# Copyright 2021 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import os

from absl import flags
from absl import logging
from absl.testing import parameterized
import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow_decision_forests import keras
from tensorflow_decision_forests.component import py_tree
from tensorflow_decision_forests.component.builder import builder as builder_lib
from tensorflow_decision_forests.component.inspector import inspector as inspector_lib

Tree = py_tree.tree.Tree
NonLeafNode = py_tree.node.NonLeafNode
NumericalHigherThanCondition = py_tree.condition.NumericalHigherThanCondition
CategoricalIsInCondition = py_tree.condition.CategoricalIsInCondition
SimpleColumnSpec = py_tree.dataspec.SimpleColumnSpec
LeafNode = py_tree.node.LeafNode
ProbabilityValue = py_tree.value.ProbabilityValue
RegressionValue = py_tree.value.RegressionValue

# pylint: disable=g-long-lambda


def data_root_path() -> str:
  return ""


def test_data_path() -> str:
  return os.path.join(data_root_path(),
                      "external/ydf/yggdrasil_decision_forests/test_data")


def tmp_path() -> str:
  return flags.FLAGS.test_tmpdir


def test_model_directory() -> str:
  return os.path.join(test_data_path(), "model")


def test_dataset_directory() -> str:
  return os.path.join(test_data_path(), "dataset")


class BuilderTest(parameterized.TestCase, tf.test.TestCase):

  def test_classification_random_forest(self):
    model_path = os.path.join(tmp_path(), "classification_rf")
    logging.info("Create model in %s", model_path)
    builder = builder_lib.RandomForestBuilder(
        path=model_path,
        model_format=builder_lib.ModelFormat.TENSORFLOW_SAVED_MODEL,
        objective=py_tree.objective.ClassificationObjective(
            label="color", classes=["red", "blue", "green"]))

    #  f1>=1.5
    #    │
    #    ├─(pos)─ f2 in ["cat","dog"]
    #    │         │
    #    │         ├─(pos)─ value: [0.8, 0.1, 0.1]
    #    │         └─(neg)─ value: [0.1, 0.8, 0.1]
    #    └─(neg)─ value: [0.1, 0.1, 0.8]
    builder.add_tree(
        Tree(
            NonLeafNode(
                condition=NumericalHigherThanCondition(
                    feature=SimpleColumnSpec(
                        name="f1", type=py_tree.dataspec.ColumnType.NUMERICAL),
                    threshold=1.5,
                    missing_evaluation=False),
                pos_child=NonLeafNode(
                    condition=CategoricalIsInCondition(
                        feature=SimpleColumnSpec(
                            name="f2",
                            type=py_tree.dataspec.ColumnType.CATEGORICAL),
                        mask=["cat", "dog"],
                        missing_evaluation=False),
                    pos_child=LeafNode(
                        value=ProbabilityValue(
                            probability=[0.8, 0.1, 0.1], num_examples=10)),
                    neg_child=LeafNode(
                        value=ProbabilityValue(
                            probability=[0.1, 0.8, 0.1], num_examples=20))),
                neg_child=LeafNode(
                    value=ProbabilityValue(
                        probability=[0.1, 0.1, 0.8], num_examples=30)))))

    builder.close()

    logging.info("Loading model")
    loaded_model = tf.keras.models.load_model(model_path)

    logging.info("Make predictions")
    tf_dataset = tf.data.Dataset.from_tensor_slices({
        "f1": [1.0, 2.0, 3.0],
        "f2": ["cat", "cat", "bird"]
    }).batch(2)
    predictions = loaded_model.predict(tf_dataset)
    self.assertAllClose(predictions,
                        [[0.1, 0.1, 0.8], [0.8, 0.1, 0.1], [0.1, 0.8, 0.1]])

  def test_classification_cart(self):
    model_path = os.path.join(tmp_path(), "classification_cart")
    logging.info("Create model in %s", model_path)
    builder = builder_lib.CARTBuilder(
        path=model_path,
        model_format=builder_lib.ModelFormat.TENSORFLOW_SAVED_MODEL,
        objective=py_tree.objective.ClassificationObjective(
            label="color", classes=["red", "blue", "green"]))

    #  f1>=1.5
    #    ├─(pos)─ f2 in ["cat","dog"]
    #    │         ├─(pos)─ value: [0.8, 0.1, 0.1]
    #    │         └─(neg)─ value: [0.1, 0.8, 0.1]
    #    └─(neg)─ value: [0.1, 0.1, 0.8]
    builder.add_tree(
        Tree(
            NonLeafNode(
                condition=NumericalHigherThanCondition(
                    feature=SimpleColumnSpec(
                        name="f1", type=py_tree.dataspec.ColumnType.NUMERICAL),
                    threshold=1.5,
                    missing_evaluation=False),
                pos_child=NonLeafNode(
                    condition=CategoricalIsInCondition(
                        feature=SimpleColumnSpec(
                            name="f2",
                            type=py_tree.dataspec.ColumnType.CATEGORICAL),
                        mask=["cat", "dog"],
                        missing_evaluation=False),
                    pos_child=LeafNode(
                        value=ProbabilityValue(
                            probability=[0.8, 0.1, 0.1], num_examples=10)),
                    neg_child=LeafNode(
                        value=ProbabilityValue(
                            probability=[0.1, 0.8, 0.1], num_examples=20))),
                neg_child=LeafNode(
                    value=ProbabilityValue(
                        probability=[0.1, 0.1, 0.8], num_examples=30)))))

    builder.close()

    logging.info("Loading model")
    loaded_model = tf.keras.models.load_model(model_path)

    logging.info("Make predictions")
    tf_dataset = tf.data.Dataset.from_tensor_slices({
        "f1": [1.0, 2.0, 3.0],
        "f2": ["cat", "cat", "bird"]
    }).batch(2)
    predictions = loaded_model.predict(tf_dataset)
    self.assertAllClose(predictions,
                        [[0.1, 0.1, 0.8], [0.8, 0.1, 0.1], [0.1, 0.8, 0.1]])

  def test_regression_random_forest(self):
    model_path = os.path.join(tmp_path(), "regression_rf")
    logging.info("Create model in %s", model_path)
    builder = builder_lib.RandomForestBuilder(
        path=model_path,
        model_format=builder_lib.ModelFormat.TENSORFLOW_SAVED_MODEL,
        objective=py_tree.objective.RegressionObjective(label="age"))

    #  f1>=1.5
    #    ├─(pos)─ age: 1
    #    └─(neg)─ age: 2
    builder.add_tree(
        Tree(
            NonLeafNode(
                condition=NumericalHigherThanCondition(
                    feature=SimpleColumnSpec(
                        name="f1", type=py_tree.dataspec.ColumnType.NUMERICAL),
                    threshold=1.5,
                    missing_evaluation=False),
                pos_child=LeafNode(
                    value=RegressionValue(value=1, num_examples=30)),
                neg_child=LeafNode(
                    value=RegressionValue(value=2, num_examples=30)))))

    builder.close()

    logging.info("Loading model")
    loaded_model = tf.keras.models.load_model(model_path)

    logging.info("Make predictions")
    tf_dataset = tf.data.Dataset.from_tensor_slices({
        "f1": [1.0, 2.0],
    }).batch(2)
    predictions = loaded_model.predict(tf_dataset)
    self.assertAllClose(predictions, [[2.0], [1.0]])

  def test_binary_classification_gbt(self):
    model_path = os.path.join(tmp_path(), "binary_classification_gbt")
    logging.info("Create model in %s", model_path)
    builder = builder_lib.GradientBoostedTreeBuilder(
        path=model_path,
        model_format=builder_lib.ModelFormat.TENSORFLOW_SAVED_MODEL,
        bias=1.0,
        objective=py_tree.objective.ClassificationObjective(
            label="color", classes=["red", "blue"]))

    #  bias: 1.0 (toward "blue")
    #  f1>=1.5
    #    ├─(pos)─ +1.0 (toward "blue")
    #    └─(neg)─ -1.0 (toward "blue")
    builder.add_tree(
        Tree(
            NonLeafNode(
                condition=NumericalHigherThanCondition(
                    feature=SimpleColumnSpec(
                        name="f1", type=py_tree.dataspec.ColumnType.NUMERICAL),
                    threshold=1.5,
                    missing_evaluation=False),
                pos_child=LeafNode(
                    value=RegressionValue(value=+1, num_examples=30)),
                neg_child=LeafNode(
                    value=RegressionValue(value=-1, num_examples=30)))))

    builder.close()

    logging.info("Loading model")
    loaded_model = tf.keras.models.load_model(model_path)

    logging.info("Make predictions")
    tf_dataset = tf.data.Dataset.from_tensor_slices({
        "f1": [1.0, 2.0],
    }).batch(2)
    predictions = loaded_model.predict(tf_dataset)
    self.assertAllClose(
        predictions,
        [[1.0 / (1.0 + math.exp(0.0))], [1.0 / (1.0 + math.exp(-2.0))]])

  def test_multi_class_classification_gbt(self):
    model_path = os.path.join(tmp_path(), "multi_class_classification_gbt")
    logging.info("Create model in %s", model_path)
    builder = builder_lib.GradientBoostedTreeBuilder(
        path=model_path,
        model_format=builder_lib.ModelFormat.TENSORFLOW_SAVED_MODEL,
        objective=py_tree.objective.ClassificationObjective(
            label="color", classes=["red", "blue", "green"]))

    #  f1>=1.5
    #    ├─(pos)─ +1.0 (toward "red")
    #    └─(neg)─ -1.0 (toward "red")
    #  f1>=2.5
    #    ├─(pos)─ +1.0 (toward "blue")
    #    └─(neg)─ -1.0 (toward "blue")
    #  f1>=3.5
    #    ├─(pos)─ +1.0 (toward "green")
    #    └─(neg)─ -1.0 (toward "green")

    for threshold in [1.5, 2.5, 3.5]:
      builder.add_tree(
          Tree(
              NonLeafNode(
                  condition=NumericalHigherThanCondition(
                      feature=SimpleColumnSpec(
                          name="f1",
                          type=py_tree.dataspec.ColumnType.NUMERICAL),
                      threshold=threshold,
                      missing_evaluation=False),
                  pos_child=LeafNode(
                      value=RegressionValue(value=+1, num_examples=30)),
                  neg_child=LeafNode(
                      value=RegressionValue(value=-1, num_examples=30)))))

    builder.close()

    logging.info("Loading model")
    loaded_model = tf.keras.models.load_model(model_path)

    logging.info("Make predictions")
    tf_dataset = tf.data.Dataset.from_tensor_slices({
        "f1": [1.0, 2.0],
    }).batch(2)
    predictions = loaded_model.predict(tf_dataset)

    soft_max_sum = np.sum(np.exp([+1, -1, -1]))
    self.assertAllClose(predictions, [[1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0],
                                      [
                                          math.exp(+1) / soft_max_sum,
                                          math.exp(-1) / soft_max_sum,
                                          math.exp(-1) / soft_max_sum
                                      ]])

  def test_regression_gbt(self):
    model_path = os.path.join(tmp_path(), "regression_gbt")
    logging.info("Create model in %s", model_path)
    builder = builder_lib.GradientBoostedTreeBuilder(
        path=model_path,
        bias=1.0,
        model_format=builder_lib.ModelFormat.TENSORFLOW_SAVED_MODEL,
        objective=py_tree.objective.RegressionObjective(label="age"))

    # bias: 1.0
    #  f1>=1.5
    #    ├─(pos)─ +1
    #    └─(neg)─ -1
    builder.add_tree(
        Tree(
            NonLeafNode(
                condition=NumericalHigherThanCondition(
                    feature=SimpleColumnSpec(
                        name="f1", type=py_tree.dataspec.ColumnType.NUMERICAL),
                    threshold=1.5,
                    missing_evaluation=False),
                pos_child=LeafNode(
                    value=RegressionValue(value=+1, num_examples=30)),
                neg_child=LeafNode(
                    value=RegressionValue(value=-1, num_examples=30)))))

    builder.close()

    logging.info("Loading model")
    loaded_model = tf.keras.models.load_model(model_path)

    logging.info("Make predictions")
    tf_dataset = tf.data.Dataset.from_tensor_slices({
        "f1": [1.0, 2.0],
    }).batch(2)
    predictions = loaded_model.predict(tf_dataset)
    self.assertAllClose(predictions, [[0.0], [2.0]])

  def test_ranking_gbt(self):
    model_path = os.path.join(tmp_path(), "ranking_gbt")
    logging.info("Create model in %s", model_path)
    builder = builder_lib.GradientBoostedTreeBuilder(
        path=model_path,
        bias=1.0,
        model_format=builder_lib.ModelFormat.TENSORFLOW_SAVED_MODEL,
        objective=py_tree.objective.RankingObjective(
            label="document", group="query"))

    # bias: 1.0
    #  f1>=1.5
    #    ├─(pos)─ +1
    #    └─(neg)─ -1
    builder.add_tree(
        Tree(
            NonLeafNode(
                condition=NumericalHigherThanCondition(
                    feature=SimpleColumnSpec(
                        name="f1", type=py_tree.dataspec.ColumnType.NUMERICAL),
                    threshold=1.5,
                    missing_evaluation=False),
                pos_child=LeafNode(
                    value=RegressionValue(value=+1, num_examples=30)),
                neg_child=LeafNode(
                    value=RegressionValue(value=-1, num_examples=30)))))

    builder.close()

    logging.info("Loading model")
    loaded_model = tf.keras.models.load_model(model_path)

    logging.info("Make predictions")
    tf_dataset = tf.data.Dataset.from_tensor_slices({
        "f1": [1.0, 2.0],
    }).batch(2)
    predictions = loaded_model.predict(tf_dataset)
    self.assertAllClose(predictions, [[0.0], [2.0]])

  def test_error_empty_path(self):
    self.assertRaises(
        ValueError, lambda: builder_lib.RandomForestBuilder(
            path="",
            model_format=builder_lib.ModelFormat.TENSORFLOW_SAVED_MODEL,
            objective=py_tree.objective.RegressionObjective("label")))

  def test_error_multi_tree_cart(self):
    builder = builder_lib.CARTBuilder(
        path=os.path.join(tmp_path(), "model"),
        objective=py_tree.objective.RegressionObjective("label"))
    builder.add_tree(Tree(LeafNode(RegressionValue(1, 30))))

    self.assertRaises(
        ValueError,
        lambda: builder.add_tree(Tree(LeafNode(RegressionValue(1, 30)))))

  def test_error_reg_cart_with_class_tree(self):
    builder = builder_lib.CARTBuilder(
        path=os.path.join(tmp_path(), "model"),
        objective=py_tree.objective.RegressionObjective("label"))
    self.assertRaises(
        ValueError, lambda: builder.add_tree(
            Tree(
                LeafNode(
                    ProbabilityValue(
                        probability=[0.8, 0.1, 0.1], num_examples=10)))))

  def test_error_class_cart_with_reg_tree(self):
    builder = builder_lib.CARTBuilder(
        path=os.path.join(tmp_path(), "model"),
        objective=py_tree.objective.ClassificationObjective(
            "label", classes=["red", "blue"]))
    self.assertRaises(
        ValueError,
        lambda: builder.add_tree(Tree(LeafNode(RegressionValue(1, 10)))))

  def test_error_wrong_class_leaf_dim(self):
    builder = builder_lib.CARTBuilder(
        path=os.path.join(tmp_path(), "model"),
        objective=py_tree.objective.ClassificationObjective(
            "label", classes=["red", "blue"]))
    self.assertRaises(
        ValueError, lambda: builder.add_tree(
            Tree(
                LeafNode(
                    ProbabilityValue(
                        probability=[0.8, 0.1, 0.1], num_examples=10)))))

  def test_error_gbt_with_class_tree(self):
    builder = builder_lib.GradientBoostedTreeBuilder(
        path=os.path.join(tmp_path(), "model"),
        objective=py_tree.objective.ClassificationObjective(
            "label", classes=["red", "blue", "green"]))

    self.assertRaises(
        ValueError, lambda: builder.add_tree(
            Tree(
                LeafNode(
                    ProbabilityValue(
                        probability=[0.8, 0.1, 0.1], num_examples=10)))))

  def test_error_gbt_wrong_number_of_trees(self):
    builder = builder_lib.GradientBoostedTreeBuilder(
        path=os.path.join(tmp_path(), "model"),
        objective=py_tree.objective.ClassificationObjective(
            "label", classes=["red", "blue", "green"]))

    builder.add_tree(Tree(LeafNode(RegressionValue(1, num_examples=10))))
    self.assertRaises(ValueError, builder.close)

  def test_get_set_dictionary(self):
    builder = builder_lib.RandomForestBuilder(
        path=os.path.join(tmp_path(), "model"),
        objective=py_tree.objective.ClassificationObjective(
            "label", classes=["true", "false"]))

    builder.add_tree(
        Tree(
            NonLeafNode(
                condition=CategoricalIsInCondition(
                    feature=SimpleColumnSpec(
                        name="f1",
                        type=py_tree.dataspec.ColumnType.CATEGORICAL),
                    mask=["x", "y"],
                    missing_evaluation=False),
                pos_child=LeafNode(
                    value=ProbabilityValue(
                        probability=[0.8, 0.2], num_examples=10)),
                neg_child=LeafNode(
                    value=ProbabilityValue(
                        probability=[0.2, 0.8], num_examples=20)))))

    self.assertEqual(builder.get_dictionary("f1"), ["<OOD>", "x", "y"])
    builder.set_dictionary("f1", ["<OOD>", "x", "y", "z"])
    self.assertEqual(builder.get_dictionary("f1"), ["<OOD>", "x", "y", "z"])
    builder.close()

  def test_extract_random_forest(self):
    """Extract 5 trees from a trained RF model, and pack them into a model."""

    # Load a dataset
    dataset_path = os.path.join(test_dataset_directory(), "adult_test.csv")
    dataframe = pd.read_csv(dataset_path)
    # This "adult_binary_class_rf" model expect for "education_num" to be a
    # string.
    dataframe["education_num"] = dataframe["education_num"].astype(str)
    dataset = keras.pd_dataframe_to_tf_dataset(dataframe, "income")

    # Load an inspector to an existing model.
    src_model_path = os.path.join(test_model_directory(),
                                  "adult_binary_class_rf")
    inspector = inspector_lib.make_inspector(src_model_path)

    # Extract a piece of this model
    dst_model_path = os.path.join(tmp_path(), "model")
    builder = builder_lib.RandomForestBuilder(
        path=dst_model_path,
        objective=inspector.objective(),
        # Make sure the features and feature dictionaries are the same as in the
        # original model.
        import_dataspec=inspector.dataspec)

    # Extract the first 5 trees
    for i in range(5):
      tree = inspector.extract_tree(i)
      builder.add_tree(tree)

    builder.close()

    truncated_model = tf.keras.models.load_model(dst_model_path)

    # By default, the model builder export numerical features as float32. In
    # this dataset, some numerical features are stored as int64. Therefore,
    # we need to apply a cast.
    #
    # TODO(gbm): Allow the user to specify the signature in a model builder.
    numerical_features = []
    for feature in inspector.features():
      if feature.type == keras.FeatureSemantic.NUMERICAL.value:
        numerical_features.append(feature)

    # Cast all the numerical features to floats.
    def cast_numerical_to_float32(features, labels):
      for numerical_feature in numerical_features:
        features[numerical_feature.name] = tf.cast(
            features[numerical_feature.name], tf.float32)
      return features, labels

    predictions = truncated_model.predict(
        dataset.map(cast_numerical_to_float32))
    self.assertEqual(predictions.shape, (9769, 1))


if __name__ == "__main__":
  tf.test.main()
