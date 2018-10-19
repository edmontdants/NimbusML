# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
ToKey
"""

__all__ = ["ToKey"]


from ...entrypoints.transforms_texttokeyconverter import \
    transforms_texttokeyconverter
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignature


class ToKey(BasePipelineItem, DefaultSignature):
    """

    Text transforms that can be performed on data before training
    a model.

    .. remarks::
        The ``ToKey`` transform converts a column of text to key values
        using a dictionary. This operation can be reversed by using
        :py:class:`FromKey <nimbusml.preprocessing.FromKey>` to obtain the
        orginal values.

    :param max_num_terms: Maximum number of terms to keep per column when auto-
        training.

    :param term: List of terms.

    :param sort: How items should be ordered when vectorized. By default, they
        will be in the order encountered. If by value items are sorted
        according to their default comparison, e.g., text sorting will be case
        sensitive (e.g., 'A' then 'Z' then 'a').

    :param text_key_values: Whether key value metadata should be text,
        regardless of the actual input type.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`FromKey <nimbusml.preprocessing.FromKey>`,
        :py:class:`OneHotHashVectorizer
        <nimbusml.feature_extraction.categorical.OneHotHashVectorizer>`,
        :py:class:`OneHotVectorizer
        <nimbusml.feature_extraction.categorical.OneHotVectorizer>`,
        :py:class:`NGramFeaturizer
        <nimbusml.feature_extraction.text.NGramFeaturizer>`.

    .. index:: transform, preprocessing, text

    Example:
       .. literalinclude:: /../nimbusml/examples/ToKey.py
              :language: python
    """

    @trace
    def __init__(
            self,
            max_num_terms=1000000,
            term=None,
            sort='Occurrence',
            text_key_values=False,
            **params):
        BasePipelineItem.__init__(
            self, type='transform', **params)

        self.max_num_terms = max_num_terms
        self.term = term
        self.sort = sort
        self.text_key_values = text_key_values

    @property
    def _entrypoint(self):
        return transforms_texttokeyconverter

    @trace
    def _get_node(self, **all_args):

        input_columns = self.input
        if input_columns is None and 'input' in all_args:
            input_columns = all_args['input']
        if 'input' in all_args:
            all_args.pop('input')

        output_columns = self.output
        if output_columns is None and 'output' in all_args:
            output_columns = all_args['output']
        if 'output' in all_args:
            all_args.pop('output')

        # validate input
        if input_columns is None:
            raise ValueError(
                "'None' input passed when it cannot be none.")

        if not isinstance(input_columns, list):
            raise ValueError(
                "input has to be a list of strings, instead got %s" %
                type(input_columns))

        # validate output
        if output_columns is None:
            output_columns = input_columns

        if not isinstance(output_columns, list):
            raise ValueError(
                "output has to be a list of strings, instead got %s" %
                type(output_columns))

        algo_args = dict(
            column=[
                dict(
                    Source=i,
                    Name=o) for i,
                o in zip(
                    input_columns,
                    output_columns)] if input_columns else None,
            max_num_terms=self.max_num_terms,
            term=self.term,
            sort=self.sort,
            text_key_values=self.text_key_values)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)
