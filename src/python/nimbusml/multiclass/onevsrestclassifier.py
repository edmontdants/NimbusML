# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
OneVsRestClassifier
"""

__all__ = ["OneVsRestClassifier"]


from sklearn.base import ClassifierMixin

from ..base_predictor import BasePredictor
from ..internal.core.multiclass.onevsrestclassifier import \
    OneVsRestClassifier as core
from ..internal.utils.utils import trace


class OneVsRestClassifier(core, BasePredictor, ClassifierMixin):
    """

    One-vs-All macro (OVA)


    .. remarks::
        `OneVsRestClassifier
        <https://en.wikipedia.org/wiki/Multiclass_classification>` converts
        any binary classifiers into mult-class.
        A multi-class classification problem (with K classes) can be
        decomposed into K binary classification
        problems per class, with label as 0 or 1 (if a sample belongs to the
        class). OneVsRestClassifier
        predicts the label with the highest score from the basic learners.

    :param feature: see `Columns </nimbusml/concepts/columns>`_.

    :param label: see `Columns </nimbusml/concepts/columns>`_.

    :param weight: see `Columns </nimbusml/concepts/columns>`_.

    :param classifier: The subgraph for the binary trainer used to construct
        the OVA learner. This should be a TrainBinary node.

    :param output_for_sub_graph: The training subgraph output.

    :param use_probabilities: Use probabilities in OVA combiner.

    :param normalize: If ``Auto``, the choice to normalize depends on the
        preference declared by the algorithm. This is the default choice. If
        ``No``, no normalization is performed. If ``Yes``, normalization always
        performed. If ``Warn``, if normalization is needed by the algorithm, a
        warning message is displayed but normalization is not performed. If
        normalization is performed, a ``MaxMin`` normalizer is used. This
        normalizer preserves sparsity by mapping zero to zero.

    :param caching: Whether learner should cache input training data.

    :param params: Additional arguments sent to compute engine.

    .. note::

        This algorithm can be treated as a wrapper for all the binary
        classifiers in nimbusml. A few binary
        classifiers already have implementation for multi-class problems,
        thus users can choose either one
        depending on the context. The OVA version of a binary classifier,
        such as wrapping a :py:class:`LightGbmBinaryClassifier
        <nimbusml.ensemble.LightGbmBinaryClassifier>` ,
        can be different from :py:class:`LightGbmClassifier
        <nimbusml.ensemble.LightGbmClassifier>` ,
        which develops a multi-class classifier directly.

    .. seealso::
        :py:class:`FastForestBinaryClassifier
        <nimbusml.ensemble.FastForestBinaryClassifier>`,
        :py:class:`FastTreesBinaryClassifier
        <nimbusml.ensemble.FastTreesBinaryClassifier>`,
        :py:class:`GamBinaryClassifier
        <nimbusml.ensemble.GamBinaryClassifier>`,
        :py:class:`LightGbmBinaryClassifier
        <nimbusml.ensemble.LightGbmBinaryClassifier>`,
        :py:class:`AveragedPerceptronBinaryClassifier
        <nimbusml.linear_model.AveragedPerceptronBinaryClassifier>`,
        :py:class:`FastLinearBinaryClassifier
        <nimbusml.linear_model.FastLinearBinaryClassifier>`,
        :py:class:`LogisticRegressionBinaryClassifier
        <nimbusml.linear_model.LogisticRegressionBinaryClassifier>`,
        :py:class:`SgdBinaryClassifier
        <nimbusml.linear_model.SgdBinaryClassifier>`.

    .. index:: models, classification, multi-class

    Example:
       .. literalinclude:: /../nimbusml/examples/OneVsRestClassifier.py
              :language: python
    """

    @trace
    def __init__(
            self,
            classifier,
            output_for_sub_graph=0,
            use_probabilities=True,
            normalize='Auto',
            caching='Auto',
            feature=None,
            label=None,
            weight=None,
            **params):

        if 'feature_column' in params:
            raise NameError(
                "'feature_column' must be renamed to 'feature'")
        if feature:
            params['feature_column'] = feature
        if 'label_column' in params:
            raise NameError(
                "'label_column' must be renamed to 'label'")
        if label:
            params['label_column'] = label
        if 'weight_column' in params:
            raise NameError(
                "'weight_column' must be renamed to 'weight'")
        if weight:
            params['weight_column'] = weight
        BasePredictor.__init__(self, type='classifier', **params)
        core.__init__(
            self,
            classifier=classifier,
            output_for_sub_graph=output_for_sub_graph,
            use_probabilities=use_probabilities,
            normalize=normalize,
            caching=caching,
            **params)
        self.feature = feature
        self.label = label
        self.weight = weight

    @trace
    def predict_proba(self, X, **params):
        '''
        Returns probabilities
        '''
        self.classifier._check_implements_method('predict_proba')
        if not self.use_probabilities:
            raise ValueError(
                '{}: use_probabilities needs to be set to True'
                ' for predict_proba()'.format(
                    self.__class__))
        return self._predict_proba(X, **params)

    @trace
    def decision_function(self, X, **params):
        '''
        Returns score values
        '''
        self.classifier._check_implements_method(
            'decision_function')
        if self.use_probabilities:
            raise ValueError(
                '{}: use_probabilities needs to be set to False'
                ' for decision_function()'.format(
                    self.__class__))
        return self._decision_function(X, **params)

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
