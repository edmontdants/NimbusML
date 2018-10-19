# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Models.PAVCalibrator
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def models_pavcalibrator(
        data,
        uncalibrated_predictor_model,
        predictor_model=None,
        max_rows=1000000000,
        **params):
    """
    **Description**
        Apply a PAV calibrator to an input model

    :param data: Input dataset (inputs).
    :param uncalibrated_predictor_model: The predictor to calibrate
        (inputs).
    :param max_rows: The maximum number of examples to train the
        calibrator on (inputs).
    :param predictor_model: The trained model (outputs).
    """

    entrypoint_name = 'Models.PAVCalibrator'
    inputs = {}
    outputs = {}

    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if uncalibrated_predictor_model is not None:
        inputs['UncalibratedPredictorModel'] = try_set(
            obj=uncalibrated_predictor_model,
            none_acceptable=False,
            is_of_type=str)
    if max_rows is not None:
        inputs['MaxRows'] = try_set(
            obj=max_rows,
            none_acceptable=False,
            is_of_type=numbers.Real,
            valid_range={
                'Inf': 0,
                'Max': 2147483647})
    if predictor_model is not None:
        outputs['PredictorModel'] = try_set(
            obj=predictor_model, none_acceptable=False, is_of_type=str)

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
