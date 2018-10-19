# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Transforms.Segregator
"""


from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def transforms_segregator(
        data,
        column,
        output_data=None,
        model=None,
        mode='Inner',
        **params):
    """
    **Description**
        Un-groups vector columns into sequences of rows, inverse of Group
        transform

    :param data: Input dataset (inputs).
    :param column: Columns to unroll, or 'pivot' (inputs).
    :param mode: Specifies how to unroll multiple pivot columns of
        different size. (inputs).
    :param output_data: Transformed dataset (outputs).
    :param model: Transform model (outputs).
    """

    entrypoint_name = 'Transforms.Segregator'
    inputs = {}
    outputs = {}

    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if column is not None:
        inputs['Column'] = try_set(
            obj=column,
            none_acceptable=False,
            is_of_type=list,
            is_column=True)
    if mode is not None:
        inputs['Mode'] = try_set(
            obj=mode,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'Inner',
                'Outer',
                'First'])
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
