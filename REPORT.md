# FlightLab ML Collaboration Report

## Experiment Drift

The exp/khadija-max-depth branch was intentionally kept unmerged as an experimental branch.

The baseline model used model.max_depth=12. Three DVC experiments were conducted with max_depth values of 8, 16, and 20.

The results were:

| max_depth | Accuracy | Precision | Recall | F1 |
|---:|---:|---:|---:|---:|
| 8 | 0.50395 | 0.39167 | 0.48643 | 0.43394 |
| 12 (baseline) | 0.51104 | 0.39399 | 0.46631 | 0.42711 |
| 16 | 0.51679 | 0.39253 | 0.43140 | 0.41105 |
| 20 | 0.52131 | 0.39126 | 0.40413 | 0.39759 |

The max_depth=8 experiment achieved the highest F1 score (0.43394), so it was selected as the winning experiment and promoted through the eat/promote-max-depth-8 branch.

The exp/khadija-max-depth branch was therefore retained as an unmerged experiment record rather than being merged into dev.

## Retrospective

### What broke

- The pre-commit large-file hook was blocked by a Windows Application Control policy.
- The DVC configuration caused an issue during fresh-clone reproduction because the shared DVC remote configuration was not available correctly.
- The secret scanner flagged a DVC MD5 hash as a potential high-entropy secret; the DVC hash was allowlisted as a false positive.
- Generated DVC files such as dvc.lock and metrics.json required careful handling during commits.
- Git branch protection prevented direct pushes to dev, so changes had to go through pull requests.

### What we would standardize

- Keep the shared DVC remote URL available to all team members while keeping credentials local and secret.
- Use a consistent DVC experiment and promotion workflow.
- Run dvc push before pushing Git changes whenever DVC-tracked data or artifacts change.
- Perform a fresh-clone reproducibility test before every production release.
- Keep dev, staging, and main protected and use pull requests for changes.

### CONTRIBUTING.md updates

As a result of the project, we would standardize:

- Branch naming conventions.
- Commit message conventions.
- Pull request review requirements.
- DVC workflow for data and model changes.
- Experiment and model-promotion workflow.
- Reproducibility checks before release.
- Required CI checks before merging.
