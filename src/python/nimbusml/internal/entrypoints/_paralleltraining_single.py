# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Single
"""


from ..utils.entrypoints import Component


def single(
        **params):
    """
    **Description**
        Single node machine learning process.

    """

    entrypoint_name = 'Single'
    settings = {}

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='ParallelTraining')
    return component
