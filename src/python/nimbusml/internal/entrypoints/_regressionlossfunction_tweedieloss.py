# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
TweedieLoss
"""

import numbers

from ..utils.entrypoints import Component
from ..utils.utils import try_set


def tweedie_loss(
        index=1.5,
        **params):
    """
    **Description**
        Tweedie loss.

    :param index: Index parameter for the Tweedie distribution, in
        the range [1, 2]. 1 is Poisson loss, 2 is gamma loss, and
        intermediate values are compound Poisson loss. (settings).
    """

    entrypoint_name = 'TweedieLoss'
    settings = {}

    if index is not None:
        settings['Index'] = try_set(
            obj=index,
            none_acceptable=True,
            is_of_type=numbers.Real)

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='RegressionLossFunction')
    return component
