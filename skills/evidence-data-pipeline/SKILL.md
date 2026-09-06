---
name: evidence-data-pipeline
description: Build or review traceable scientific and public-data pipelines with explicit provenance, uncertainty, validation, and reproducibility. Use for ingestion, normalization, statistical analysis, MCMC or ML experiments, dashboards, or derived datasets.
---

# Evidence Data Pipeline

Preserve the distinction between source evidence, transformations, analysis, and interpretation.

## Data layers

- Keep raw, interim, and processed data separate. Never silently overwrite source material with normalized output.
- Preserve source URLs, retrieval dates, document or page versions, extraction method, confidence, scenario, and other useful metadata.
- Mark fictitious or demonstration data explicitly and prevent it from being presented as observed data.
- Version schemas, configurations, corrections, and model inputs that materially affect results.

## Ingestion and normalization

- Make parsers source-specific and normalize into a stable internal schema.
- Validate required fields, units, date ranges, identifiers, duplicates, completeness, and impossible values at boundaries.
- Quarantine or report malformed records instead of silently coercing them.
- Keep transformations deterministic and record assumptions used to reconstruct missing or ambiguous values.

## Analysis

- Distinguish aggregation, correction, inference, forecasting, and experimental modeling.
- Quantify uncertainty and sensitivity where the method permits it.
- For sampling pipelines, inspect convergence and effective sample information with diagnostics appropriate to the method, such as R-hat and ESS.
- Compare heterogeneous pipelines on common inputs and metrics before interpreting differences.
- Do not present a model output as a certain prediction.

## Validation and reproducibility

- Add unit tests for transformations and regression tests for representative datasets and known edge cases.
- Record random seeds, dependency versions, configuration, source versions, and commands needed to reproduce results.
- Check invariants across raw counts, normalized counts, joins, aggregates, and exports.
- Keep performance TODOs open until measurements, scenarios, and measurable targets are recorded.
- Make dashboard labels distinguish observed, reconstructed, adjusted, smoothed, and simulated values.

## Reporting

Document what is sourced, transformed, reconstructed, uncertain, experimental, or missing. Link conclusions to evidence and state limitations next to the result they qualify.
