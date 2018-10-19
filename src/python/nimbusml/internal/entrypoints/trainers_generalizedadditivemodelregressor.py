# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Trainers.GeneralizedAdditiveModelRegressor
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def trainers_generalizedadditivemodelregressor(
        training_data,
        predictor_model=None,
        num_iterations=9500,
        feature_column='Features',
        min_documents=10,
        label_column='Label',
        learning_rates=0.002,
        weight_column=None,
        normalize_features='Auto',
        caching='Auto',
        pruning_metrics=2,
        entropy_coefficient=0.0,
        gain_confidence_level=0,
        num_threads=None,
        disk_transpose=None,
        max_bins=255,
        max_output=float("inf"),
        get_derivatives_sample_rate=1,
        rng_seed=123,
        feature_flocks=True,
        enable_pruning=True,
        **params):
    """
    **Description**
        Trains a gradient boosted stump per feature, on all features
        simultaneously, to fit target values using least-squares. It
        mantains no interactions between features.

    :param num_iterations: Total number of iterations over all
        features (inputs).
    :param training_data: The data to be used for training (inputs).
    :param feature_column: Column to use for features (inputs).
    :param min_documents: Minimum number of training instances
        required to form a partition (inputs).
    :param label_column: Column to use for labels (inputs).
    :param learning_rates: The learning rate (inputs).
    :param weight_column: Column to use for example weight (inputs).
    :param normalize_features: Normalize option for the feature
        column (inputs).
    :param caching: Whether learner should cache input training data
        (inputs).
    :param pruning_metrics: Metric for pruning. (For regression, 1:
        L1, 2:L2; default L2) (inputs).
    :param entropy_coefficient: The entropy (regularization)
        coefficient between 0 and 1 (inputs).
    :param gain_confidence_level: Tree fitting gain confidence
        requirement (should be in the range [0,1) ). (inputs).
    :param num_threads: The number of threads to use (inputs).
    :param disk_transpose: Whether to utilize the disk or the data's
        native transposition facilities (where applicable) when
        performing the transpose (inputs).
    :param max_bins: Maximum number of distinct values (bins) per
        feature (inputs).
    :param max_output: Upper bound on absolute value of single output
        (inputs).
    :param get_derivatives_sample_rate: Sample each query 1 in k
        times in the GetDerivatives function (inputs).
    :param rng_seed: The seed of the random number generator
        (inputs).
    :param feature_flocks: Whether to collectivize features during
        dataset preparation to speed up training (inputs).
    :param enable_pruning: Enable post-training pruning to avoid
        overfitting. (a validation set is required) (inputs).
    :param predictor_model: The trained model (outputs).
    """

    entrypoint_name = 'Trainers.GeneralizedAdditiveModelRegressor'
    inputs = {}
    outputs = {}

    if num_iterations is not None:
        inputs['NumIterations'] = try_set(
            obj=num_iterations,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if training_data is not None:
        inputs['TrainingData'] = try_set(
            obj=training_data,
            none_acceptable=False,
            is_of_type=str)
    if feature_column is not None:
        inputs['FeatureColumn'] = try_set(
            obj=feature_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if min_documents is not None:
        inputs['MinDocuments'] = try_set(
            obj=min_documents,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if label_column is not None:
        inputs['LabelColumn'] = try_set(
            obj=label_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if learning_rates is not None:
        inputs['LearningRates'] = try_set(
            obj=learning_rates,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if weight_column is not None:
        inputs['WeightColumn'] = try_set(
            obj=weight_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if normalize_features is not None:
        inputs['NormalizeFeatures'] = try_set(
            obj=normalize_features,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'No',
                'Warn',
                'Auto',
                'Yes'])
    if caching is not None:
        inputs['Caching'] = try_set(
            obj=caching,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'Auto',
                'Memory',
                'Disk',
                'None'])
    if pruning_metrics is not None:
        inputs['PruningMetrics'] = try_set(
            obj=pruning_metrics,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if entropy_coefficient is not None:
        inputs['EntropyCoefficient'] = try_set(
            obj=entropy_coefficient,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if gain_confidence_level is not None:
        inputs['GainConfidenceLevel'] = try_set(
            obj=gain_confidence_level,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if num_threads is not None:
        inputs['NumThreads'] = try_set(
            obj=num_threads,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if disk_transpose is not None:
        inputs['DiskTranspose'] = try_set(
            obj=disk_transpose,
            none_acceptable=True,
            is_of_type=bool)
    if max_bins is not None:
        inputs['MaxBins'] = try_set(
            obj=max_bins,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if max_output is not None:
        inputs['MaxOutput'] = try_set(
            obj=max_output,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if get_derivatives_sample_rate is not None:
        inputs['GetDerivativesSampleRate'] = try_set(
            obj=get_derivatives_sample_rate,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if rng_seed is not None:
        inputs['RngSeed'] = try_set(
            obj=rng_seed,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if feature_flocks is not None:
        inputs['FeatureFlocks'] = try_set(
            obj=feature_flocks,
            none_acceptable=True,
            is_of_type=bool)
    if enable_pruning is not None:
        inputs['EnablePruning'] = try_set(
            obj=enable_pruning,
            none_acceptable=True,
            is_of_type=bool)
    if predictor_model is not None:
        outputs['PredictorModel'] = try_set(
            obj=predictor_model, none_acceptable=False, is_of_type=str)

    input_variables = {
        x for x in unlist(inputs.values())
        if isinstance(x, str) and x.startswith("$")}
    output_variables = {
        x for x in unlist(outputs.values())
        if isinstance(x, str) and x.startswith("$")}

    entrypoint = EntryPoint(
        name=entrypoint_name, inputs=inputs, outputs=outputs,
        input_variables=input_variables,
        output_variables=output_variables)
    return entrypoint
