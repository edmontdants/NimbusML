# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
KMeansPlusPlus
"""

__all__ = ["KMeansPlusPlus"]


from ...entrypoints.trainers_kmeansplusplusclusterer import \
    trainers_kmeansplusplusclusterer
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignatureWithRoles


class KMeansPlusPlus(BasePipelineItem, DefaultSignatureWithRoles):
    """

    Machine Learning KMeans clustering algorithm

    .. remarks::
        `K-means <https://en.wikipedia.org/wiki/K-means_clustering>`_ is a
        popular clustering algorithm. With `K-means++
        <https://en.wikipedia.org/wiki/K-means%2b%2b>`_, the data is
        clustered
        into a specified number of clusters in order to minimize the
        within-cluster sum of squares. K-means++ improves upon K-means by
        using
        a better method for choosing the initial cluster centers.


        **Reference**

            `https://www.microsoft.com/en-us/research/wp-
            content/uploads/2016/02/ding15.pdf <https://www.microsoft.com/en-
            us/research/wp-content/uploads/2016/02/ding15.pdf>`_


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

    :param n_clusters: The number of clusters.

    :param train_threads: Degree of lock-free parallelism. Defaults to
        automatic. Determinism not guaranteed.

    :param init_algorithm: Cluster initialization algorithm.

    :param opt_tol: Tolerance parameter for trainer convergence. Lower =
        slower, more accurate.

    :param max_iterations: Maximum number of iterations.

    :param accel_mem_budget_mb: Memory budget (in MBs) to use for KMeans
        acceleration.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:func:`LogisticRegressionClassifier
        <nimbusml.linear_model.LogisticRegressionClassifier>`,
        :py:func:`AveragedPerceptronBinaryClassifier
        <nimbusml.linear_model.AveragedPerceptronBinaryClassifier>`

    .. index:: models, classification, stocastic, gradient, descent

    Example:
       .. literalinclude:: /../nimbusml/examples/KMeansPlusPlus.py
              :language: python
    """

    @trace
    def __init__(
            self,
            normalize='Auto',
            caching='Auto',
            n_clusters=5,
            train_threads=None,
            init_algorithm='KMeansParallel',
            opt_tol=1e-07,
            max_iterations=1000,
            accel_mem_budget_mb=4096,
            **params):
        BasePipelineItem.__init__(
            self, type='clusterer', **params)

        self.normalize = normalize
        self.caching = caching
        self.n_clusters = n_clusters
        self.train_threads = train_threads
        self.init_algorithm = init_algorithm
        self.opt_tol = opt_tol
        self.max_iterations = max_iterations
        self.accel_mem_budget_mb = accel_mem_budget_mb

    @property
    def _entrypoint(self):
        return trainers_kmeansplusplusclusterer

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            feature_column=self._getattr_role(
                'feature_column',
                all_args),
            weight_column=self._getattr_role(
                'weight_column',
                all_args),
            normalize_features=self.normalize,
            caching=self.caching,
            k=self.n_clusters,
            num_threads=self.train_threads,
            init_algorithm=self.init_algorithm,
            opt_tol=self.opt_tol,
            max_iterations=self.max_iterations,
            accel_mem_budget_mb=self.accel_mem_budget_mb)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)

    @trace
    def fit_predict(self, X, y=None, **params):
        """
        Fits and predicts.
        """
        self.fit(X, y=y, **params)
        return self.predict(X)
