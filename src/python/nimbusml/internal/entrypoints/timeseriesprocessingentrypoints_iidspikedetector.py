# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
TimeSeriesProcessingEntryPoints.IidSpikeDetector
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def timeseriesprocessingentrypoints_iidspikedetector(
        source,
        data,
        name,
        output_data=None,
        model=None,
        confidence=99.0,
        side='TwoSided',
        pvalue_history_length=100,
        **params):
    """
    **Description**
        This transform detects the spikes in a i.i.d. sequence using adaptive
        kernel density estimation.

    :param source: The name of the source column. (inputs).
    :param data: Input dataset (inputs).
    :param name: The name of the new column. (inputs).
    :param confidence: The confidence for spike detection in the
        range [0, 100]. (inputs).
    :param side: The argument that determines whether to detect
        positive or negative anomalies, or both. (inputs).
    :param pvalue_history_length: The size of the sliding window for
        computing the p-value. (inputs).
    :param output_data: Transformed dataset (outputs).
    :param model: Transform model (outputs).
    """

    entrypoint_name = 'TimeSeriesProcessingEntryPoints.IidSpikeDetector'
    inputs = {}
    outputs = {}

    if source is not None:
        inputs['Source'] = try_set(
            obj=source,
            none_acceptable=False,
            is_of_type=str,
            is_column=True)
    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if name is not None:
        inputs['Name'] = try_set(
            obj=name,
            none_acceptable=False,
            is_of_type=str,
            is_column=True)
    if confidence is not None:
        inputs['Confidence'] = try_set(
            obj=confidence,
            none_acceptable=False,
            is_of_type=numbers.Real)
    if side is not None:
        inputs['Side'] = try_set(
            obj=side,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'Positive',
                'Negative',
                'TwoSided'])
    if pvalue_history_length is not None:
        inputs['PvalueHistoryLength'] = try_set(
            obj=pvalue_history_length,
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