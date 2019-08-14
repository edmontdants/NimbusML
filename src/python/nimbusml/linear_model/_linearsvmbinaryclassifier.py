# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
LinearSvmBinaryClassifier
"""

__all__ = ["LinearSvmBinaryClassifier"]


from sklearn.base import ClassifierMixin

from ..base_predictor import BasePredictor
from ..internal.core.linear_model._linearsvmbinaryclassifier import \
    LinearSvmBinaryClassifier as core
from ..internal.utils.utils import trace


class LinearSvmBinaryClassifier(
        core,
        BasePredictor,
        ClassifierMixin):
    """

    Linear Support Vector Machine (SVM) Binary Classifier

    .. remarks::
        Linear SVM implements an algorithm that finds a hyperplane in the
        feature space for binary classification, by solving an SVM problem.
        For instance, with feature values $f_0, f_1,..., f_{D-1}$, the
        prediction is given by determining what side of the hyperplane the
        point falls into. That is the same as the sign of the feautures'
        weighted sum, i.e. $\sum_{i = 0}^{D-1} \left(w_i * f_i \right) + b$,
        where $w_0, w_1,..., w_{D-1}$ are the weights computed by the
        algorithm, and *b* is the bias computed by the algorithm.

        This algorithm implemented is the PEGASOS method, which alternates
        between stochastic gradient descent steps and projection steps,
        introduced by Shalev-Shwartz, Singer and Srebro.


        **Reference**

            `Wikipedia entry for Support Vector Machine
            <https://en.wikipedia.org/wiki/Support-vector_machine>`_

            `Pegasos: Primal Estimated sub-GrAdient SOlver for SVM
            <https://ttic.uchicago.edu/~shai/papers/ShalevSiSr07.pdf>`_


    :param feature: see `Columns </nimbusml/concepts/columns>`_.

    :param label: see `Columns </nimbusml/concepts/columns>`_.

    :param weight: see `Columns </nimbusml/concepts/columns>`_.

    :param normalize: Specifies the type of automatic normalization used:

        * ``"Auto"``: if normalization is needed, it is performed
          automatically. This is the default choice.
        * ``"No"``: no normalization is performed.
        * ``"Yes"``: normalization is performed.
        * ``"Warn"``: if normalization is needed, a warning
          message is displayed, but normalization is not performed.

        Normalization rescales disparate data ranges to a standard scale.
        Feature
        scaling ensures the distances between data points are proportional
        and
        enables various optimization methods such as gradient descent to
        converge
        much faster. If normalization is performed, a ``MinMax`` normalizer
        is
        used. It normalizes values in an interval [a, b] where ``-1 <= a <=
        0``
        and ``0 <= b <= 1`` and ``b - a = 1``. This normalizer preserves
        sparsity by mapping zero to zero.

    :param caching: Whether trainer should cache input training data.

    :param lambda_: Regularizer constant.

    :param perform_projection: Perform projection to unit-ball? Typically used
        with batch size > 1.

    :param number_of_iterations: Number of iterations.

    :param initial_weights_diameter: Sets the initial weights diameter that
        specifies the range from which values are drawn for the initial
        weights. These weights are initialized randomly from within this range.
        For example, if the diameter is specified to be ``d``, then the weights
        are uniformly distributed between ``-d/2`` and ``d/2``. The default
        value is ``0``, which specifies that all the  weights are set to zero.

    :param no_bias: No bias.

    :param initial_weights: Initial Weights and bias, comma-separated.

    :param shuffle: Whether to shuffle for each training iteration.

    :param batch_size: Batch size.

    :param params: Additional arguments sent to compute engine.

    .. index:: models, classification, svm

    Example:
       .. literalinclude:: /../nimbusml/examples/LinearSvmBinaryClassifier.py
               :language: python
    """

    @trace
    def __init__(
            self,
            normalize='Auto',
            caching='Auto',
            lambda_=0.001,
            perform_projection=False,
            number_of_iterations=1,
            initial_weights_diameter=0.0,
            no_bias=False,
            initial_weights=None,
            shuffle=True,
            batch_size=1,
            feature=None,
            label=None,
            weight=None,
            **params):

        if 'feature_column_name' in params:
            raise NameError(
                "'feature_column_name' must be renamed to 'feature'")
        if feature:
            params['feature_column_name'] = feature
        if 'label_column_name' in params:
            raise NameError(
                "'label_column_name' must be renamed to 'label'")
        if label:
            params['label_column_name'] = label
        if 'example_weight_column_name' in params:
            raise NameError(
                "'example_weight_column_name' must be renamed to 'weight'")
        if weight:
            params['example_weight_column_name'] = weight
        BasePredictor.__init__(self, type='classifier', **params)
        core.__init__(
            self,
            normalize=normalize,
            caching=caching,
            lambda_=lambda_,
            perform_projection=perform_projection,
            number_of_iterations=number_of_iterations,
            initial_weights_diameter=initial_weights_diameter,
            no_bias=no_bias,
            initial_weights=initial_weights,
            shuffle=shuffle,
            batch_size=batch_size,
            **params)
        self.feature = feature
        self.label = label
        self.weight = weight

    @trace
    def predict_proba(self, X, **params):
        '''
        Returns probabilities
        '''
        return self._predict_proba(X, **params)

    @trace
    def decision_function(self, X, **params):
        '''
        Returns score values
        '''
        return self._decision_function(X, **params)

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
