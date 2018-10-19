# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Data.CustomTextLoader
"""


from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def data_customtextloader(
        input_file,
        data=None,
        custom_schema=None,
        **params):
    """
    **Description**
        Import a dataset from a text file

    :param input_file: Location of the input file (inputs).
    :param custom_schema: Custom schema to use for parsing (inputs).
    :param data: The resulting data view (outputs).
    """

    entrypoint_name = 'Data.CustomTextLoader'
    inputs = {}
    outputs = {}

    if input_file is not None:
        inputs['InputFile'] = try_set(
            obj=input_file,
            none_acceptable=False,
            is_of_type=str)
    if custom_schema is not None:
        inputs['CustomSchema'] = try_set(
            obj=custom_schema,
            none_acceptable=True,
            is_of_type=str)
    if data is not None:
        outputs['Data'] = try_set(
            obj=data,
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
