# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Handler
"""

__all__ = ["Handler"]


from ....entrypoints.transforms_missingvaluehandler import \
    transforms_missingvaluehandler
from ....utils.utils import trace
from ...base_pipeline_item import BasePipelineItem, DefaultSignature


class Handler(BasePipelineItem, DefaultSignature):
    """

    Replace NaN values in a column with imputed values.

    .. remarks::
        ``Handler`` is a combination of :py:class:`Filter
        <nimbusml.preprocessing.missing_values.Filter>` and :py:class:`Indicator
        <nimbusml.preprocessing.missing_values.Indicator>`. It creates two
        columns, one
        containing the imputed values as specified by ``replace_with``
        argument,
        and the second column containing indicator values of which rows
        entries
        were imputed. This works for columns that have numeric type.

    :param replace_with: The method to use to replace NaN values. The
    following choices are available.

       * Def: Replace with default value of that type, usually ``0``. If no
        replace
       method is specified, this is the default strategy.
       * Mean: Replace NaN values with the mean of the values in that column.
       * Min: Replace with minimum value in the column.
       * Max: Replace with maximum value in the column.

    :param impute_by_slot: Whether to impute values by slot.

    :param concat: Whether or not to concatenate an indicator vector column to
        the value column.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`Filter <nimbusml.preprocessing.missing_values.Filter>`,
        :py:class:`Indicator <nimbusml.preprocessing.missing_values.Indicator>`.

    .. index:: handler

    Example:
       .. literalinclude:: /../nimbusml/examples/Handler.py
              :language: python
    """

    @trace
    def __init__(
            self,
            replace_with='DefaultValue',
            impute_by_slot=True,
            concat=True,
            **params):
        BasePipelineItem.__init__(
            self, type='transform', **params)

        self.replace_with = replace_with
        self.impute_by_slot = impute_by_slot
        self.concat = concat

    @property
    def _entrypoint(self):
        return transforms_missingvaluehandler

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
            replace_with=self.replace_with,
            impute_by_slot=self.impute_by_slot,
            concat=self.concat)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)
