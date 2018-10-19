# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
SgdBinaryClassifier
"""

__all__ = ["SgdBinaryClassifier"]


from ...core.loss.loss_factory import check_loss, create_loss
from ...entrypoints.trainers_stochasticgradientdescentbinaryclassifier import \
    trainers_stochasticgradientdescentbinaryclassifier
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignatureWithRoles


class SgdBinaryClassifier(
        BasePipelineItem,
        DefaultSignatureWithRoles):
    """

    Machine Learning Hogwild Stochastic Gradient Descent Binary
    Classifier

    .. remarks::
        The Stochastic Gradient Descent (SGD) is one of the most popular
        stochastic optimization procedure that can be integrated into several
        machine learning tasks to achieve state-of-the-art performance. The
        Hogwild SGD binary classification learner implements SGD for binary
        classification that supports multi-threading without any locking. If
        the
        associated optimization problem is sparse, then Hogwild SGD achieves
        a
        nearly optimal rate of convergence. For a detailed reference, please
        refer to `http://arxiv.org/pdf/1106.5730v2.pdf
        <http://arxiv.org/pdf/1106.5730v2.pdf>`_.


        **Reference**

            `http://arxiv.org/pdf/1106.5730v2.pdf
            <http://arxiv.org/pdf/1106.5730v2.pdf>`_


    :param normalize: Specifies the type of automatic normalization used:

        * ``"Auto"``: if normalization is needed, it is performed
          automatically. This is the default choice.
        * ``"No"``: no normalization is performed.
        * ``"Yes"``: normalization is performed.
        * ``"Warn"``: if normalization is needed, a warning
          message is displayed, but normalization is not performed.

        Normalization rescales disparate data ranges to a standard scale.
        Feature
        scaling insures the distances between data points are proportional
        and
        enables various optimization methods such as gradient descent to
        converge
        much faster. If normalization is performed, a ``MaxMin`` normalizer
        is
        used. It normalizes values in an interval [a, b] where ``-1 <= a <=
        0``
        and ``0 <= b <= 1`` and ``b - a = 1``. This normalizer preserves
        sparsity by mapping zero to zero.

    :param caching: Whether learner should cache input training data.

    :param loss: The default is :py:class:`'log' <nimbusml.loss.Log>`. Other
        choices are :py:class:`'exp' <nimbusml.loss.Exp>`, :py:class:`'hinge'
        <nimbusml.loss.Hinge>`, and :py:class:`'smoothed_hinge'
        <nimbusml.loss.SmoothedHinge>`. For more information, please see the
        documentation page about losses, [Loss](xref:nimbusml.loss).

    :param l2_weight: L2 regularizer constant.

    :param train_threads: Degree of lock-free parallelism. Defaults to
        automatic depending on data sparseness. Determinism not guaranteed.

    :param convergence_tolerance: Exponential moving averaged improvement
        tolerance for convergence.

    :param max_iterations: Maximum number of iterations; set to 1 to simulate
        online learning.

    :param init_learning_rate: Initial learning rate (only used by SGD).

    :param shuffle: Shuffle data every epoch?.

    :param positive_instance_weight: Apply weight to the positive class, for
        imbalanced data.

    :param check_frequency: Convergence check frequency (in terms of number of
        iterations). Default equals number of threads.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:func:`LogisticRegressionClassifier
        <nimbusml.linear_model.LogisticRegressionClassifier>`,
        :py:func:`AveragedPerceptronBinaryClassifier
        <nimbusml.linear_model.AveragedPerceptronBinaryClassifier>`

    .. index:: models, classification, stocastic, gradient, descent

    Example:
       .. literalinclude:: /../nimbusml/examples/SgdBinaryClassifier.py
              :language: python
    """

    @trace
    def __init__(
            self,
            normalize='Auto',
            caching='Auto',
            loss='log',
            l2_weight=1e-06,
            train_threads=None,
            convergence_tolerance=0.0001,
            max_iterations=20,
            init_learning_rate=0.01,
            shuffle=True,
            positive_instance_weight=1.0,
            check_frequency=None,
            **params):
        BasePipelineItem.__init__(
            self, type='classifier', **params)

        self.normalize = normalize
        self.caching = caching
        self.loss = loss
        check_loss(
            'ClassificationLossFunction',
            self.__class__.__name__,
            self.loss)
        self.l2_weight = l2_weight
        self.train_threads = train_threads
        self.convergence_tolerance = convergence_tolerance
        self.max_iterations = max_iterations
        self.init_learning_rate = init_learning_rate
        self.shuffle = shuffle
        self.positive_instance_weight = positive_instance_weight
        self.check_frequency = check_frequency

    @property
    def _entrypoint(self):
        return trainers_stochasticgradientdescentbinaryclassifier

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            feature_column=self._getattr_role(
                'feature_column',
                all_args),
            label_column=self._getattr_role(
                'label_column',
                all_args),
            weight_column=self._getattr_role(
                'weight_column',
                all_args),
            normalize_features=self.normalize,
            caching=self.caching,
            loss_function=create_loss(
                'ClassificationLossFunction',
                self.__class__.__name__,
                self.loss),
            l2_const=self.l2_weight,
            num_threads=self.train_threads,
            convergence_tolerance=self.convergence_tolerance,
            max_iterations=self.max_iterations,
            init_learning_rate=self.init_learning_rate,
            shuffle=self.shuffle,
            positive_instance_weight=self.positive_instance_weight,
            check_frequency=self.check_frequency)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)
