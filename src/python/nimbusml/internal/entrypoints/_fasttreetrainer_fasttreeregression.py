# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
FastTreeRegression
"""

import numbers

from ..utils.entrypoints import Component
from ..utils.utils import try_set


def fast_tree_regression(
        training_data,
        num_trees=100,
        num_leaves=20,
        feature_column='Features',
        min_documents_in_leafs=10,
        label_column='Label',
        learning_rates=0.2,
        weight_column=None,
        group_id_column=None,
        normalize_features='Auto',
        caching='Auto',
        best_step_ranking_regression_trees=False,
        use_line_search=False,
        num_post_bracket_steps=0,
        min_step_size=0.0,
        optimization_algorithm='GradientDescent',
        early_stopping_rule=None,
        early_stopping_metrics=1,
        enable_pruning=False,
        use_tolerant_pruning=False,
        pruning_threshold=0.004,
        pruning_window_size=5,
        shrinkage=1.0,
        dropout_rate=0.0,
        get_derivatives_sample_rate=1,
        write_last_ensemble=False,
        max_tree_output=100.0,
        random_start=False,
        filter_zero_lambdas=False,
        baseline_scores_formula=None,
        baseline_alpha_risk=None,
        position_discount_freeform=None,
        parallel_trainer=None,
        num_threads=None,
        rng_seed=123,
        feature_select_seed=123,
        entropy_coefficient=0.0,
        histogram_pool_size=-1,
        disk_transpose=None,
        feature_flocks=True,
        categorical_split=False,
        max_categorical_groups_per_node=64,
        max_categorical_split_points=64,
        min_docs_percentage_for_categorical_split=0.001,
        min_docs_for_categorical_split=100,
        bias=0.0,
        bundling='None',
        max_bins=255,
        sparsify_threshold=0.7,
        feature_first_use_penalty=0.0,
        feature_reuse_penalty=0.0,
        gain_confidence_level=0.0,
        softmax_temperature=0.0,
        execution_times=False,
        feature_fraction=1.0,
        bagging_size=0,
        bagging_train_fraction=0.7,
        split_fraction=1.0,
        smoothing=0.0,
        allow_empty_trees=True,
        feature_compression_level=1,
        compress_ensemble=False,
        max_trees_after_compression=-1,
        print_test_graph=False,
        print_train_valid_graph=False,
        test_frequency=2147483647,
        **params):
    """
    **Description**
        Trains gradient boosted decision trees to fit target values using
        least-squares.

    :param num_trees: Total number of decision trees to create in the
        ensemble (settings).
    :param training_data: The data to be used for training
        (settings).
    :param num_leaves: The max number of leaves in each regression
        tree (settings).
    :param feature_column: Column to use for features (settings).
    :param min_documents_in_leafs: The minimal number of documents
        allowed in a leaf of a regression tree, out of the subsampled
        data (settings).
    :param label_column: Column to use for labels (settings).
    :param learning_rates: The learning rate (settings).
    :param weight_column: Column to use for example weight
        (settings).
    :param group_id_column: Column to use for example groupId
        (settings).
    :param normalize_features: Normalize option for the feature
        column (settings).
    :param caching: Whether learner should cache input training data
        (settings).
    :param best_step_ranking_regression_trees: Use best regression
        step trees? (settings).
    :param use_line_search: Should we use line search for a step size
        (settings).
    :param num_post_bracket_steps: Number of post-bracket line search
        steps (settings).
    :param min_step_size: Minimum line search step size (settings).
    :param optimization_algorithm: Optimization algorithm to be used
        (GradientDescent, AcceleratedGradientDescent) (settings).
    :param early_stopping_rule: Early stopping rule. (Validation set
        (/valid) is required.) (settings).
    :param early_stopping_metrics: Early stopping metrics. (For
        regression, 1: L1, 2:L2; for ranking, 1:NDCG@1, 3:NDCG@3)
        (settings).
    :param enable_pruning: Enable post-training pruning to avoid
        overfitting. (a validation set is required) (settings).
    :param use_tolerant_pruning: Use window and tolerance for pruning
        (settings).
    :param pruning_threshold: The tolerance threshold for pruning
        (settings).
    :param pruning_window_size: The moving window size for pruning
        (settings).
    :param shrinkage: Shrinkage (settings).
    :param dropout_rate: Dropout rate for tree regularization
        (settings).
    :param get_derivatives_sample_rate: Sample each query 1 in k
        times in the GetDerivatives function (settings).
    :param write_last_ensemble: Write the last ensemble instead of
        the one determined by early stopping (settings).
    :param max_tree_output: Upper bound on absolute value of single
        tree output (settings).
    :param random_start: Training starts from random ordering
        (determined by /r1) (settings).
    :param filter_zero_lambdas: Filter zero lambdas during training
        (settings).
    :param baseline_scores_formula: Freeform defining the scores that
        should be used as the baseline ranker (settings).
    :param baseline_alpha_risk: Baseline alpha for tradeoffs of risk
        (0 is normal training) (settings).
    :param position_discount_freeform: The discount freeform which
        specifies the per position discounts of documents in a query
        (uses a single variable P for position where P=0 is first
        position) (settings).
    :param parallel_trainer: Allows to choose Parallel FastTree
        Learning Algorithm (settings).
    :param num_threads: The number of threads to use (settings).
    :param rng_seed: The seed of the random number generator
        (settings).
    :param feature_select_seed: The seed of the active feature
        selection (settings).
    :param entropy_coefficient: The entropy (regularization)
        coefficient between 0 and 1 (settings).
    :param histogram_pool_size: The number of histograms in the pool
        (between 2 and numLeaves) (settings).
    :param disk_transpose: Whether to utilize the disk or the data's
        native transposition facilities (where applicable) when
        performing the transpose (settings).
    :param feature_flocks: Whether to collectivize features during
        dataset preparation to speed up training (settings).
    :param categorical_split: Whether to do split based on multiple
        categorical feature values. (settings).
    :param max_categorical_groups_per_node: Maximum categorical split
        groups to consider when splitting on a categorical feature.
        Split groups are a collection of split points. This is used
        to reduce overfitting when there many categorical features.
        (settings).
    :param max_categorical_split_points: Maximum categorical split
        points to consider when splitting on a categorical feature.
        (settings).
    :param min_docs_percentage_for_categorical_split: Minimum
        categorical docs percentage in a bin to consider for a split.
        (settings).
    :param min_docs_for_categorical_split: Minimum categorical doc
        count in a bin to consider for a split. (settings).
    :param bias: Bias for calculating gradient for each feature bin
        for a categorical feature. (settings).
    :param bundling: Bundle low population bins. Bundle.None(0): no
        bundling, Bundle.AggregateLowPopulation(1): Bundle low
        population, Bundle.Adjacent(2): Neighbor low population
        bundle. (settings).
    :param max_bins: Maximum number of distinct values (bins) per
        feature (settings).
    :param sparsify_threshold: Sparsity level needed to use sparse
        feature representation (settings).
    :param feature_first_use_penalty: The feature first use penalty
        coefficient (settings).
    :param feature_reuse_penalty: The feature re-use penalty
        (regularization) coefficient (settings).
    :param gain_confidence_level: Tree fitting gain confidence
        requirement (should be in the range [0,1) ). (settings).
    :param softmax_temperature: The temperature of the randomized
        softmax distribution for choosing the feature (settings).
    :param execution_times: Print execution time breakdown to stdout
        (settings).
    :param feature_fraction: The fraction of features (chosen
        randomly) to use on each iteration (settings).
    :param bagging_size: Number of trees in each bag (0 for disabling
        bagging) (settings).
    :param bagging_train_fraction: Percentage of training examples
        used in each bag (settings).
    :param split_fraction: The fraction of features (chosen randomly)
        to use on each split (settings).
    :param smoothing: Smoothing paramter for tree regularization
        (settings).
    :param allow_empty_trees: When a root split is impossible, allow
        training to proceed (settings).
    :param feature_compression_level: The level of feature
        compression to use (settings).
    :param compress_ensemble: Compress the tree Ensemble (settings).
    :param max_trees_after_compression: Maximum Number of trees after
        compression (settings).
    :param print_test_graph: Print metrics graph for the first test
        set (settings).
    :param print_train_valid_graph: Print Train and Validation
        metrics in graph (settings).
    :param test_frequency: Calculate metric values for
        train/valid/test every k rounds (settings).
    """

    entrypoint_name = 'FastTreeRegression'
    settings = {}

    if num_trees is not None:
        settings['NumTrees'] = try_set(
            obj=num_trees,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if training_data is not None:
        settings['TrainingData'] = try_set(
            obj=training_data, none_acceptable=False, is_of_type=str)
    if num_leaves is not None:
        settings['NumLeaves'] = try_set(
            obj=num_leaves,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if feature_column is not None:
        settings['FeatureColumn'] = try_set(
            obj=feature_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if min_documents_in_leafs is not None:
        settings['MinDocumentsInLeafs'] = try_set(
            obj=min_documents_in_leafs,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if label_column is not None:
        settings['LabelColumn'] = try_set(
            obj=label_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if learning_rates is not None:
        settings['LearningRates'] = try_set(
            obj=learning_rates,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if weight_column is not None:
        settings['WeightColumn'] = try_set(
            obj=weight_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if group_id_column is not None:
        settings['GroupIdColumn'] = try_set(
            obj=group_id_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if normalize_features is not None:
        settings['NormalizeFeatures'] = try_set(
            obj=normalize_features,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'No',
                'Warn',
                'Auto',
                'Yes'])
    if caching is not None:
        settings['Caching'] = try_set(
            obj=caching,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'Auto',
                'Memory',
                'Disk',
                'None'])
    if best_step_ranking_regression_trees is not None:
        settings['BestStepRankingRegressionTrees'] = try_set(
            obj=best_step_ranking_regression_trees,
            none_acceptable=True,
            is_of_type=bool)
    if use_line_search is not None:
        settings['UseLineSearch'] = try_set(
            obj=use_line_search, none_acceptable=True, is_of_type=bool)
    if num_post_bracket_steps is not None:
        settings['NumPostBracketSteps'] = try_set(
            obj=num_post_bracket_steps,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if min_step_size is not None:
        settings['MinStepSize'] = try_set(
            obj=min_step_size,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if optimization_algorithm is not None:
        settings['OptimizationAlgorithm'] = try_set(
            obj=optimization_algorithm,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'GradientDescent',
                'AcceleratedGradientDescent',
                'ConjugateGradientDescent'])
    if early_stopping_rule is not None:
        settings['EarlyStoppingRule'] = try_set(
            obj=early_stopping_rule, none_acceptable=True, is_of_type=dict)
    if early_stopping_metrics is not None:
        settings['EarlyStoppingMetrics'] = try_set(
            obj=early_stopping_metrics,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if enable_pruning is not None:
        settings['EnablePruning'] = try_set(
            obj=enable_pruning, none_acceptable=True, is_of_type=bool)
    if use_tolerant_pruning is not None:
        settings['UseTolerantPruning'] = try_set(
            obj=use_tolerant_pruning, none_acceptable=True, is_of_type=bool)
    if pruning_threshold is not None:
        settings['PruningThreshold'] = try_set(
            obj=pruning_threshold,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if pruning_window_size is not None:
        settings['PruningWindowSize'] = try_set(
            obj=pruning_window_size,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if shrinkage is not None:
        settings['Shrinkage'] = try_set(
            obj=shrinkage,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if dropout_rate is not None:
        settings['DropoutRate'] = try_set(
            obj=dropout_rate,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if get_derivatives_sample_rate is not None:
        settings['GetDerivativesSampleRate'] = try_set(
            obj=get_derivatives_sample_rate,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if write_last_ensemble is not None:
        settings['WriteLastEnsemble'] = try_set(
            obj=write_last_ensemble, none_acceptable=True, is_of_type=bool)
    if max_tree_output is not None:
        settings['MaxTreeOutput'] = try_set(
            obj=max_tree_output,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if random_start is not None:
        settings['RandomStart'] = try_set(
            obj=random_start, none_acceptable=True, is_of_type=bool)
    if filter_zero_lambdas is not None:
        settings['FilterZeroLambdas'] = try_set(
            obj=filter_zero_lambdas, none_acceptable=True, is_of_type=bool)
    if baseline_scores_formula is not None:
        settings['BaselineScoresFormula'] = try_set(
            obj=baseline_scores_formula, none_acceptable=True, is_of_type=str)
    if baseline_alpha_risk is not None:
        settings['BaselineAlphaRisk'] = try_set(
            obj=baseline_alpha_risk, none_acceptable=True, is_of_type=str)
    if position_discount_freeform is not None:
        settings['PositionDiscountFreeform'] = try_set(
            obj=position_discount_freeform,
            none_acceptable=True,
            is_of_type=str)
    if parallel_trainer is not None:
        settings['ParallelTrainer'] = try_set(
            obj=parallel_trainer, none_acceptable=True, is_of_type=dict)
    if num_threads is not None:
        settings['NumThreads'] = try_set(
            obj=num_threads,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if rng_seed is not None:
        settings['RngSeed'] = try_set(
            obj=rng_seed,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if feature_select_seed is not None:
        settings['FeatureSelectSeed'] = try_set(
            obj=feature_select_seed,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if entropy_coefficient is not None:
        settings['EntropyCoefficient'] = try_set(
            obj=entropy_coefficient,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if histogram_pool_size is not None:
        settings['HistogramPoolSize'] = try_set(
            obj=histogram_pool_size,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if disk_transpose is not None:
        settings['DiskTranspose'] = try_set(
            obj=disk_transpose, none_acceptable=True, is_of_type=bool)
    if feature_flocks is not None:
        settings['FeatureFlocks'] = try_set(
            obj=feature_flocks, none_acceptable=True, is_of_type=bool)
    if categorical_split is not None:
        settings['CategoricalSplit'] = try_set(
            obj=categorical_split, none_acceptable=True, is_of_type=bool)
    if max_categorical_groups_per_node is not None:
        settings['MaxCategoricalGroupsPerNode'] = try_set(
            obj=max_categorical_groups_per_node,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if max_categorical_split_points is not None:
        settings['MaxCategoricalSplitPoints'] = try_set(
            obj=max_categorical_split_points,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if min_docs_percentage_for_categorical_split is not None:
        settings['MinDocsPercentageForCategoricalSplit'] = try_set(
            obj=min_docs_percentage_for_categorical_split,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if min_docs_for_categorical_split is not None:
        settings['MinDocsForCategoricalSplit'] = try_set(
            obj=min_docs_for_categorical_split,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if bias is not None:
        settings['Bias'] = try_set(
            obj=bias,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if bundling is not None:
        settings['Bundling'] = try_set(
            obj=bundling, none_acceptable=True, is_of_type=str, values=[
                'None', 'AggregateLowPopulation', 'Adjacent'])
    if max_bins is not None:
        settings['MaxBins'] = try_set(
            obj=max_bins,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if sparsify_threshold is not None:
        settings['SparsifyThreshold'] = try_set(
            obj=sparsify_threshold,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if feature_first_use_penalty is not None:
        settings['FeatureFirstUsePenalty'] = try_set(
            obj=feature_first_use_penalty,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if feature_reuse_penalty is not None:
        settings['FeatureReusePenalty'] = try_set(
            obj=feature_reuse_penalty,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if gain_confidence_level is not None:
        settings['GainConfidenceLevel'] = try_set(
            obj=gain_confidence_level,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if softmax_temperature is not None:
        settings['SoftmaxTemperature'] = try_set(
            obj=softmax_temperature,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if execution_times is not None:
        settings['ExecutionTimes'] = try_set(
            obj=execution_times, none_acceptable=True, is_of_type=bool)
    if feature_fraction is not None:
        settings['FeatureFraction'] = try_set(
            obj=feature_fraction,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if bagging_size is not None:
        settings['BaggingSize'] = try_set(
            obj=bagging_size,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if bagging_train_fraction is not None:
        settings['BaggingTrainFraction'] = try_set(
            obj=bagging_train_fraction,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if split_fraction is not None:
        settings['SplitFraction'] = try_set(
            obj=split_fraction,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if smoothing is not None:
        settings['Smoothing'] = try_set(
            obj=smoothing,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if allow_empty_trees is not None:
        settings['AllowEmptyTrees'] = try_set(
            obj=allow_empty_trees, none_acceptable=True, is_of_type=bool)
    if feature_compression_level is not None:
        settings['FeatureCompressionLevel'] = try_set(
            obj=feature_compression_level,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if compress_ensemble is not None:
        settings['CompressEnsemble'] = try_set(
            obj=compress_ensemble, none_acceptable=True, is_of_type=bool)
    if max_trees_after_compression is not None:
        settings['MaxTreesAfterCompression'] = try_set(
            obj=max_trees_after_compression,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if print_test_graph is not None:
        settings['PrintTestGraph'] = try_set(
            obj=print_test_graph, none_acceptable=True, is_of_type=bool)
    if print_train_valid_graph is not None:
        settings['PrintTrainValidGraph'] = try_set(
            obj=print_train_valid_graph, none_acceptable=True, is_of_type=bool)
    if test_frequency is not None:
        settings['TestFrequency'] = try_set(
            obj=test_frequency,
            none_acceptable=True,
            is_of_type=numbers.Real)

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='FastTreeTrainer')
    return component
