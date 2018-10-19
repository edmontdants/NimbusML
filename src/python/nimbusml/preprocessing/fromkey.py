# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
FromKey
"""

__all__ = ["FromKey"]


from sklearn.base import TransformerMixin

from ..base_transform import BaseTransform
from ..internal.core.preprocessing.fromkey import FromKey as core
from ..internal.utils.utils import trace


class FromKey(core, BaseTransform, TransformerMixin):
    """

    Text transforms that can be performed on data before training
    a model.

    .. remarks::
        The ``FromKey`` transform converts a column of keys, generated using
        :py:class:`ToKey <nimbusml.preprocessing.ToKey>`, to their original
        values.

    :param columns: see `Columns </nimbusml/concepts/columns>`_.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`ToKey <nimbusml.preprocessing.ToKey>`,
        :py:class:`OneHotHashVectorizer
        <nimbusml.feature_extraction.categorical.OneHotHashVectorizer>`,
        :py:class:`OneHotVectorizer
        <nimbusml.feature_extraction.categorical.OneHotVectorizer>`,
        :py:class:`NGramFeaturizer
        <nimbusml.feature_extraction.text.NGramFeaturizer>`,

    .. index:: transform, preprocessing, text

    Example:
       .. literalinclude:: /../nimbusml/examples/FromKey.py
              :language: python
    """

    @trace
    def __init__(
            self,
            columns=None,
            **params):

        if columns:
            params['columns'] = columns
        BaseTransform.__init__(self, **params)
        core.__init__(
            self,
            **params)
        self._columns = columns

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
