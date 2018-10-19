# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
ColumnDuplicator
"""

__all__ = ["ColumnDuplicator"]


from ....entrypoints.transforms_columncopier import transforms_columncopier
from ....utils.utils import trace
from ...base_pipeline_item import BasePipelineItem, DefaultSignature


class ColumnDuplicator(BasePipelineItem, DefaultSignature):
    """

    Duplicates columns from the dataset

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`ColumnDropper
        <nimbusml.preprocessing.schema.ColumnDropper>`,
        :py:class:`ColumnSelector
        <nimbusml.preprocessing.schema.ColumnSelector>`.

    .. index:: transform, schema

    Example:
       .. literalinclude:: /../nimbusml/examples/ColumnDuplicator.py
              :language: python
    """

    @trace
    def __init__(
            self,
            **params):
        BasePipelineItem.__init__(
            self, type='transform', **params)

    @property
    def _entrypoint(self):
        return transforms_columncopier

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
                    Source=i, Name=o) for i, o in zip(
                    input_columns, output_columns)] if input_columns else None)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)
