# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
LogLoss
"""


from ..utils.entrypoints import Component


def log_loss(
        **params):
    """
    **Description**
        Log loss.

    """

    entrypoint_name = 'LogLoss'
    settings = {}

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='ClassificationLossFunction')
    return component
