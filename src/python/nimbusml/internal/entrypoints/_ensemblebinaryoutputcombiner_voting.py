# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Voting
"""


from ..utils.entrypoints import Component


def voting(
        **params):
    """
    **Description**
        None

    """

    entrypoint_name = 'Voting'
    settings = {}

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='EnsembleBinaryOutputCombiner')
    return component
