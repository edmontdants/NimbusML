# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
WeightedAverage
"""


from ..utils.entrypoints import Component
from ..utils.utils import try_set


def weighted_average(
        weightage_name='Auc',
        **params):
    """
    **Description**
        None

    :param weightage_name: The metric type to be used to find the
        weights for each model (settings).
    """

    entrypoint_name = 'WeightedAverage'
    settings = {}

    if weightage_name is not None:
        settings['WeightageName'] = try_set(
            obj=weightage_name,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'Accuracy',
                'Auc',
                'PosPrecision',
                'PosRecall',
                'NegPrecision',
                'NegRecall'])

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='EnsembleBinaryOutputCombiner')
    return component
