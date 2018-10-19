# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Transforms.FeatureCombiner
"""


from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def transforms_featurecombiner(
        data,
        output_data=None,
        model=None,
        features=None,
        **params):
    """
    **Description**
        Combines all the features into one feature column.

    :param data: Input dataset (inputs).
    :param features: Features (inputs).
    :param output_data: Transformed dataset (outputs).
    :param model: Transform model (outputs).
    """

    entrypoint_name = 'Transforms.FeatureCombiner'
    inputs = {}
    outputs = {}

    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if features is not None:
        inputs['Features'] = try_set(
            obj=features,
            none_acceptable=True,
            is_of_type=list,
            is_column=True)
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
