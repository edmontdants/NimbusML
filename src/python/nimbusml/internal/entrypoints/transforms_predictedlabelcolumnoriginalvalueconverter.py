# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Transforms.PredictedLabelColumnOriginalValueConverter
"""


from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def transforms_predictedlabelcolumnoriginalvalueconverter(
        data,
        predicted_label_column,
        output_data=None,
        model=None,
        **params):
    """
    **Description**
        Transforms a predicted label column to its original values, unless it
        is of type bool.

    :param data: Input dataset (inputs).
    :param predicted_label_column: The predicted label column
        (inputs).
    :param output_data: Transformed dataset (outputs).
    :param model: Transform model (outputs).
    """

    entrypoint_name = 'Transforms.PredictedLabelColumnOriginalValueConverter'
    inputs = {}
    outputs = {}

    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if predicted_label_column is not None:
        inputs['PredictedLabelColumn'] = try_set(
            obj=predicted_label_column,
            none_acceptable=False,
            is_of_type=str,
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
