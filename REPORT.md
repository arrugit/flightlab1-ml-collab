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
