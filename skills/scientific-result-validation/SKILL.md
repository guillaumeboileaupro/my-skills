---
name: scientific-result-validation
description: Validate scientific and statistical results through convergence, sensitivity, regression, provenance, and reproducibility checks. Use for MCMC, signal analysis, model comparison, simulations, or research pipelines.
---

# Scientific Result Validation

Separate numerical success from scientific validity.

- Record data version, configuration, software versions, random seeds, units, priors, and assumptions.
- Verify shapes, units, finite values, parameter bounds, normalization, and conservation or domain invariants.
- For sampling, examine chain traces, warmup, R-hat, effective sample size, autocorrelation, and repeated seeds.
- Compare models and pipelines on common inputs with defined metrics and uncertainty.
- Run null, synthetic injection, edge-case, sensitivity, and regression tests.
- Distinguish measured, reconstructed, inferred, simulated, and illustrative values.
- Do not select only favorable runs or present convergence diagnostics as proof that the model is correct.

Run `python scripts/check_samples.py samples.csv` for basic finite-value and per-column summary checks before deeper domain analysis.
