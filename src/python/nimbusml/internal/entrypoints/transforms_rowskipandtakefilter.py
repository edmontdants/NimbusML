# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Transforms.RowSkipAndTakeFilter
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def transforms_rowskipandtakefilter(
        data,
        output_data=None,
        model=None,
        skip=None,
        take=None,
        **params):
    """
    **Description**
        Allows limiting input to a subset of rows at an optional offset.  Can
        be used to implement data paging.

    :param skip: Number of items to skip (inputs).
    :param data: Input dataset (inputs).
    :param take: Number of items to take (inputs).
    :param output_data: Transformed dataset (outputs).
    :param model: Transform model (outputs).
    """

    entrypoint_name = 'Transforms.RowSkipAndTakeFilter'
    inputs = {}
    outputs = {}

    if skip is not None:
        inputs['Skip'] = try_set(
            obj=skip,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if take is not None:
        inputs['Take'] = try_set(
            obj=take,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if output_data is not None:
        outputs['OutputData'] = try_set(
            obj=output_data,
            none_acceptable=False,
            is_of_type=str)
    if model is not None:
        outputs['Model'] = try_set(
            obj=model,
            none_acceptable=False,
            is_of_type=str)

    input_variables = {
        x for x in unlist(inputs.values())
        if isinstance(x, str) and x.startswith("$")}
    output_variables = {
        x for x in unlist(outputs.values())
        if isinstance(x, str) and x.startswith("$")}

    entrypoint = EntryPoint(
        name=entrypoint_name, inputs=inputs, outputs=outputs,
        input_variables=input_variables,
        output_variables=output_variables)
    return entrypoint
