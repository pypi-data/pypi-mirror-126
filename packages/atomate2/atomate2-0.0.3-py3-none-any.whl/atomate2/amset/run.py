"""Module defining functions to run amset."""

from __future__ import annotations

import logging
import warnings

import numpy as np
from amset.core.run import Runner
from monty.serialization import dumpfn
from pydash import get
from ruamel.yaml.error import MantissaNoDotYAML1_1Warning

__all__ = ["run_amset", "check_converged"]

logger = logging.getLogger(__name__)
_CONVERGENCE_PROPERTIES = ("mobility.overall", "seebeck")


def run_amset(**kwargs):
    """
    Run amset in the current directory.

    Parameters
    ----------
    **kwargs
        Keyword arguments that will get passed to ``Runner.from_directory``.

    Returns
    -------
    AmsetData, dict
        A tuple of the amset data object and the usage statistics.
    """
    warnings.simplefilter("ignore", MantissaNoDotYAML1_1Warning)

    if "directory" not in kwargs:
        kwargs["directory"] = "."
    runner = Runner.from_directory(**kwargs)

    amset_data, usage_stats = runner.run(return_usage_stats=True)
    dumpfn(usage_stats, "timing.json.gz")
    return amset_data, usage_stats


def check_converged(
    new_transport: dict,
    old_transport: dict,
    properties: tuple[str, ...] = _CONVERGENCE_PROPERTIES,
    tolerance: float = 0.1,
) -> bool:
    """
    Check if all transport properties (averaged) are converged within the tol.

    Parameters
    ----------
    new_transport : dict
        The new transport data.
    old_transport : dict
        The old transport data.
    properties : tuple of str
        List of properties for which convergence is assessed. The calculation is only
        flagged as converged if all properties pass the convergence checks. Options are:
        "conductivity", "seebeck", "mobility.overall", "electronic thermal conductivity.
    tolerance : float
        Relative convergence tolerance. Default is ``0.1`` (i.e. 10 %).

    Returns
    -------
    bool
        Whether the new transport data is converged.
    """
    converged = True
    for prop in properties:
        new_prop = get(new_transport, prop, None)
        old_prop = get(old_transport, prop, None)
        if new_prop is None or old_prop is None:
            logger.info(f"'{prop}' not in new or old transport data, skipping...")
            continue

        new_avg = tensor_average(new_prop)
        old_avg = tensor_average(old_prop)
        diff = np.abs((new_avg - old_avg) / new_avg)
        diff[~np.isfinite(diff)] = 0

        # don't check convergence of very small numbers due to numerical noise
        less_than_one = (np.abs(new_avg) < 1) & (np.abs(old_avg) < 1)
        element_converged = less_than_one | (diff <= tolerance)
        if not np.all(element_converged):
            logger.info(f"{prop} is not converged - max diff: {np.max(diff) * 100} %")
            converged = False

    if converged:
        logger.info("amset calculation is converged.")

    return converged


def tensor_average(tensor: list | np.ndarray) -> float | np.ndarray:
    """Calculate the average of the tensor eigenvalues.

    Parameters
    ----------
    tensor : list or numpy array
        A tensor

    Returns
    -------
    float or numpy array
        The average of the eigenvalues.
    """
    return np.average(np.linalg.eigvalsh(tensor), axis=-1)
