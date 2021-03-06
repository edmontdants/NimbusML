# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
TreeFeaturizer
"""

__all__ = ["TreeFeaturizer"]


from sklearn.base import TransformerMixin

from ..base_transform import BaseTransform
from ..internal.core.feature_extraction.treefeaturizer import \
    TreeFeaturizer as core
from ..internal.utils.utils import trace


class TreeFeaturizer(core, BaseTransform, TransformerMixin):
    """

    TreeFeaturizer.

    .. remarks::
        Trains a tree ensemble, or loads it from a file, then maps a numeric
        feature vector to three outputs:

        * A vector containing the individual tree outputs of the tree
          ensemble.
        * A vector indicating the leaves that the feature vector falls on in
          the tree ensemble.
        * A vector indicating the paths that the feature vector falls on in
          the
          tree ensemble. If a both a model file and a trainer are specified,
          will use the model file. If neither are specified, will train a
          default FastTree model. This can handle key labels by training a
          regression model towards their optionally permuted indices.

    :param columns: see `Columns </nimbusml/concepts/columns>`_.

    :param predictor_model: Trainer to use.

    :param suffix: Output column: The suffix to append to the default column
        names.

    :param label_permutation_seed: If specified, determines the permutation
        seed for applying this featurizer to a multiclass problem.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`TensorFlowScorer
        <nimbusml.preprocessing.TensorFlowScorer>`
    """

    @trace
    def __init__(
            self,
            predictor_model,
            suffix=None,
            label_permutation_seed=0,
            columns=None,
            **params):

        if columns:
            params['columns'] = columns
        BaseTransform.__init__(self, **params)
        core.__init__(
            self,
            predictor_model=predictor_model,
            suffix=suffix,
            label_permutation_seed=label_permutation_seed,
            **params)
        self._columns = columns

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
