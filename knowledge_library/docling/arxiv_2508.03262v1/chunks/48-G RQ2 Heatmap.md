## G RQ2 Heatmap

This section presents response distribution heatmaps for each experimental condition under RQ2. Figures from 9 to 14 visualize how LLM-generated willingness-to-pay responses vary depending on persona format (Survey vs. Storytelling) and prompting method (Base, CoT, RAG, Fewshot). Each figure corresponds to a specific combination

Table 3: Regression outcomes of Structure Condition on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o    | GPT-4o   | LLaMA   | LLaMA     | LLaMA   | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|-----------|----------|---------|-----------|---------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value   | z value  | coeff   | std error | p value | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |           |          |         |           |         |         |        |           |            |         |
| edu f            | 0.01     | 0.01      | 0.21      | 1.26     | 0.04    | 21694.32  | 1.00    | 0.00    | 0.01   | 0.02      | 0.51       | 0.66    |
| edu m            | -0.01    | 0.01      | 0.12      | -1.57    | -0.03   | 25017.10  | 1.00    | 0.00    | 0.00   | 0.02      | 0.90       | 0.13    |
| mus act dum      | 0.02     | 0.01      | p < 0.05  | 2.00     | -0.02   | 303822.33 | 1.00    | 0.00    | 0.06   | 0.03      | p < 0.05   | 2.38    |
| mus att ave      | 0.02     | 0.02      | 0.24      | 1.18     | 0.19    | 22875.96  | 1.00    | 0.00    | 0.26   | 0.03      | p < 0.0001 | 0.02    |
| mus ca edu a19   | 0.00     | 0.01      | 0.52      | 0.64     | -0.03   | 24289.04  | 1.00    | 0.00    | 0.03   | 0.02      | 0.19       | 10.00   |
| mus ca edu b18   | 0.00     | 0.01      | 0.64      | 0.47     | 0.06    | 18689.85  | 1.00    | 0.00    | 0.00   | 0.02      | 0.86       | 1.31    |
| mus qz tot sco   | 0.01     | 0.01      | 0.42      | 0.81     | 0.12    | 25466.45  | 1.00    | 0.00    | 0.05   | 0.02      | p < 0.05   | 0.18    |
| moral n ave      | 0.00     | 0.01      | 0.90      | 0.12     | 0.04    | 21456.43  | 1.00    | 0.00    | 0.04   | 0.02      | p < 0.05   | 2.12    |
| social n ave     | 0.00     | 0.01      | 0.65      | -0.46    | 0.04    | 19449.28  | 1.00    | 0.00    | 0.00   | 0.02      | 0.94       | 0.08    |
| inc mo           | 0.00     | 0.00      | 0.87      | -0.16    | 0.03    | 7365.53   | 1.00    | 0.00    | 0.00   | 0.01      | 0.65       | 0.45    |
| matarial dum     | 0.00     | 0.01      | 0.71      | 0.37     | 0.08    | 27206.99  | 1.00    | 0.00    | 0.04   | 0.02      | 0.66       | 1.88    |
| constant         | 8.98     | 0.08      | p < 0.001 | 106.26   | 7.33    | 103897.22 | 1.00    | 0.00    | 7.28   | 0.12      | p < 0.0001 | 61.51   |
| Model Statistics |          |           |           |          |         |           |         |         |        |           |            |         |
| Wald χ 2         |          | 9.59      |           |          |         | 3.1 × 10  | - 10    |         |        | 183.19    |            |         |
| ρ                |          | 0.69      |           |          |         | 1         |         |         |        | 0.73      |            |         |
| σ                |          | 0.07      |           |          |         | 299218.13 |         |         |        | 0.25      |            |         |
| Log Likelihood   |          | -201.81   |           |          |         | -         |         |         |        | -83.74    |            |         |
| McFadden R 2     |          | 0.44      |           |          |         | -         |         |         |        | 0.59      |            |         |
| N nonselected    |          | 268       |           |          |         | 1         |         |         |        |           | 69         |         |
| N selected       |          | 254       |           |          |         | 521       |         |         |        | 453       |            |         |

Table 4: Regression outcomes of Structure Condition on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   | LLaMA   | LLaMA     | LLaMA     | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|---------|-----------|-----------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff   | std error | p value   | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |         |           |           |         |        |           |            |         |
| edu f            | -0.01    | 0.02      | 0.64       | -0.47    | 0.04    | 21694.32  | 1.00      | 0.00    | 0.01   | 0.02      | 0.51       | 0.66    |
| edu m            | 0.00     | 0.03      | 0.10       | 0.01     | -0.03   | 25017.10  | 1.00      | 0.00    | 0.00   | 0.02      | 0.90       | 0.13    |
| mus act dum      | 0.05     | 0.04      | 0.19       | 1.30     | -0.02   | 30822.33  | 1.00      | 0.00    | 0.06   | 0.03      | p < 0.05   | 2.38    |
| mus att ave      | 0.19     | 0.06      | p < 0.01   | 3.17     | 0.19    | 22875.96  | 1.00      | 0.00    | 0.26   | 0.03      | p < 0.0001 | 10.00   |
| mus ca edu a19   | 0.00     | 0.02      | 0.92       | -0.11    | -0.03   | 24289.04  | 1.00      | 0.00    | 0.03   | 0.02      | 0.19       | 1.31    |
| mus ca edu b18   | 0.03     | 0.02      | 0.16       | -1.39    | 0.06    | 18689.85  | 1.00      | 0.00    | 0.00   | 0.02      | 0.86       | 0.18    |
| mus qz tot sco   | 0.00     | 0.02      | 0.85       | -0.19    | 0.12    | 25466.48  | 1.00      | 0.00    | 0.05   | 0.02      | p < 0.05   | 2.15    |
| moral n ave      | 0.04     | 0.02      | 0.09       | 1.67     | 0.04    | 21456.43  | 1.00      | 0.00    | 0.04   | 0.02      | p < 0.05   | 2.12    |
| social n ave     | 0.01     | 0.02      | 0.08       | 0.51     | 0.04    | 19449.28  | 1.00      | 0.00    | 0.00   | 0.02      | 0.94       | 0.08    |
| inc mo           | 0.01     | 0.01      | 0.71       | 1.74     | 0.03    | 7365.53   | 1.00      | 0.00    | 0.00   | 0.01      | 0.65       | 0.45    |
| matarial dum     | 0.01     | 0.03      | p < 0.05   | 0.36     | 0.08    | 27206.99  | 1.00      | 0.00    | 0.04   | 0.02      | 0.06       | 1.88    |
| constant         | 8.87     | 0.24      | p < 0.0001 | 36.91    | 7.33    | 103897.22 | 1.00      | 0.00    | 7.28   | 0.12      | p < 0.0001 | 61.51   |
| Model Statistics |          |           |            |          |         |           |           |         |        |           |            |         |
| Wald χ 2         |          | 9.59      |            |          |         | 3.1 ×     | 10 - 10   |         |        |           | 183.19     |         |
| ρ                |          | 0.69      |            |          |         | 1         |           |         |        |           | 0.73       |         |
| σ                |          | 0.07      |            |          |         |           | 299218.13 |         |        |           | 0.25       |         |
| Log Likelihood   |          | -201.81   |            |          |         | -         |           |         |        |           | -83.74     |         |
| McFadden R 2     |          | 0.44      |            |          |         | -         |           |         |        |           | 0.59       |         |
| N nonselected    |          | 268       |            |          |         | 1         |           |         |        |           | 69         |         |
| N selected       |          | 254       |            |          |         |           | 521       |         |        |           | 453        |         |

Table 5: Regression outcomes of Human-Guided Condition on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   |       |           |            |         | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|-------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |       |           |            |         |        |           |            |         |
| edu f            | -0.02    | 0.05      | 0.73       | -0.34    | 0.03  | 0.08      | 0.71       | 0.37    | -0.09  | 0.17      | 0.58       | -0.55   |
| edu m            | 0.04     | 0.06      | 0.47       | 0.72     | -0.02 | 0.09      | 0.82       | -0.22   | 0.12   | 0.20      | 0.53       | 0.62    |
| mus act dum      | -0.04    | 0.12      | 0.73       | -0.34    | 0.14  | 0.19      | 0.47       | -0.72   | -0.25  | 0.41      | 0.54       | -0.62   |
| mus att ave      | 0.07     | 0.11      | 0.48       | 0.70     | 0.11  | 0.17      | 0.55       | 0.60    | -0.25  | 0.37      | 0.50       | -0.67   |
| mus ca edu a19   | 0.01     | 0.04      | 0.75       | 0.32     | 0.04  | 0.05      | 0.50       | 0.68    | -0.06  | 0.13      | 0.63       | -0.48   |
| mus ca edu b18   | -0.04    | 0.05      | 0.40       | -0.84    | -0.03 | 0.08      | 0.76       | -0.31   | -0.12  | 0.18      | 0.50       | -0.68   |
| mus qz tot sco   | -0.02    | 0.05      | 0.67       | -0.43    | 0.03  | 0.08      | 0.72       | 0.35    | -0.08  | 0.17      | 0.62       | -0.50   |
| moral n ave      | 0.04     | 0.03      | 0.19       | 1.30     | 0.10  | 0.05      | p < 0.05   | 2.07    | -0.02  | 0.10      | 0.87       | -0.17   |
| social n ave     | 0.00     | 0.03      | 0.93       | 0.08     | 0.03  | 0.05      | 0.49       | 0.69    | 0.07   | 0.09      | 0.46       | 0.74    |
| inc mo           | 0.01     | 0.01      | 0.28       | 1.09     | 0.03  | 0.07      | 0.05       | 1.93    | -0.01  | 0.04      | 0.76       | -0.31   |
| matarial dum     | 0.01     | 0.05      | 0.90       | 0.13     | 0.00  | 0.92      | 0.94       | 0.07    | -0.03  | 0.16      | 0.83       | -0.22   |
| constant         | 8.50     | 0.56      | p < 0.0001 | 15.28    | 7.68  | 1.65      | p < 0.0001 | 8.32    | 9.91   | 1.95      | p < 0.0001 | 5.08    |
| Model Statistics |          |           |            |          |       |           |            |         |        |           |            |         |
| Wald χ 2         |          | 20.11     |            |          |       |           | 17.88      |         |        | 2.04      |            |         |
| ρ                |          | -1        |            |          |       |           | 0.02       |         |        |           | -1         |         |
| σ                |          | 0.46      |            |          |       |           | 0.62       |         |        | 1.60      |            |         |
| Log Likelihood   |          | -250.78   |            |          |       |           | -250.78    |         |        | -250.78   |            |         |
| McFadden R 2     |          | 0.08      |            |          |       |           | 0.08       |         |        | 0.08      |            |         |
| N nonselected    |          | 113       |            |          |       |           | 113        |         |        | 113       |            |         |
| N selected       |          | 409       |            |          |       |           | 409        |         |        | 409       |            |         |

Table 6: Regression outcomes of Human-Guided Condition on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   | LLaMA   | LLaMA     | LLaMA      | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|---------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff   | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |         |           |            |         |        |           |            |         |
| edu f            | -0.09    | 0.05      | 0.05       | -1.95    | -0.05   | 0.06      | 0.41       | -0.82   | -0.04  | 0.03      | 0.20       | -1.29   |
| edu m            | -0.03    | 0.05      | 0.54       | 0.61     | -0.02   | 0.05      | 0.65       | -0.46   | -0.02  | 0.03      | 0.63       | -0.48   |
| mus act dum      | -0.09    | 0.11      | 0.39       | -0.85    | -0.02   | 0.12      | 0.89       | -0.13   | -0.03  | 0.07      | 0.70       | -0.38   |
| mus att ave      | -0.08    | 0.14      | 0.57       | -0.57    | -0.10   | 0.17      | 0.57       | -0.57   | 0.00   | 0.10      | 0.98       | -0.02   |
| mus ca edu a19   | 0.02     | 0.04      | 0.69       | 0.40     | 0.04    | 0.05      | 0.38       | 0.88    | 0.03   | 0.03      | 0.38       | 0.87    |
| mus ca edu b18   | 0.00     | 0.04      | 0.91       | 0.11     | -0.02   | 0.05      | 0.61       | -0.51   | -0.02  | 0.03      | 0.51       | -0.66   |
| mus qz tot sco   | 0.05     | 0.05      | 0.30       | 1.04     | 0.11    | 0.06      | p < 0.05   | 2.03    | 0.06   | 0.03      | 0.07       | 1.84    |
| moral n ave      | 0.13     | 0.03      | p < 0.0001 | 3.95     | 0.13    | 0.04      | p < 0.0001 | 2.99    | 0.02   | 0.02      | 0.37       | -0.90   |
| social n ave     | -0.01    | 0.03      | 0.73       | -0.34    | -0.02   | 0.04      | 0.70       | -0.39   | 0.02   | 0.02      | 0.38       | 0.88    |
| inc mo           | 0.03     | 0.01      | p < 0.05   | 2.27     | -0.03   | 0.02      | 0.09       | 1.70    | 0.01   | 0.01      | 0.44       | 0.78    |
| matarial dum     | -0.04    | 0.05      | 0.46       | -0.73    | -0.04   | 0.06      | 0.46       | -0.75   | 0.01   | 0.04      | 0.82       | 0.23    |
| constant         | 9.61     | 0.59      | p < 0.0001 | 16.24    | 9.75    | 0.72      | p < 0.0001 | 13.52   | 9.77   | 0.42      | p < 0.0001 | 23.22   |
| Model Statistics |          |           |            |          |         |           |            |         |        |           |            |         |
| Wald χ 2         |          | 39.04     |            |          |         |           | 31.44      |         |        | 20.32     |            |         |
| ρ                |          | -0.98     |            |          |         |           | -0.54      |         |        | -0.87     |            |         |
| σ                |          | 0.49      |            |          |         |           | 0.53       |         |        | 0.34      |            |         |
| Log Likelihood   |          | -290.01   |            |          |         |           | 290.01     |         |        | -290.01   |            |         |
| McFadden R 2     |          | 0.16      |            |          |         |           | 0.16       |         |        | 0.16      |            |         |
| N nonselected    |          | 195       |            |          |         |           | 195        |         |        | 195       |            |         |
| N selected       |          | 327       |            |          |         |           | 327        |         |        | 327       |            |         |

Table 7: Regression outcomes of Survey CoT on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   |       |           |            |         | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|-------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |       |           |            |         |        |           |            |         |
| edu f            | 0.00     | 0.05      | 0.99       | -0.01    | -0.01 | 0.02      | 0.60       | -0.52   | 0.03   | 0.03      | 0.31       | 1.01    |
| edu m            | 0.01     | 0.06      | 0.92       | 0.10     | 0.04  | 0.03      | 0.15       | 1.44    | -0.01  | 0.03      | 0.84       | -0.20   |
| mus act dum      | 0.08     | 0.13      | 0.51       | 0.66     | 0.00  | 0.05      | 0.95       | 0.06    | 0.08   | 0.06      | 0.19       | 1.32    |
| mus att ave      | 0.21     | 0.11      | 0.07       | 1.81     | 0.05  | 0.05      | 0.29       | 1.05    | 0.14   | 0.06      | p < 0.05   | 2.47    |
| mus ca edu a19   | 0.00     | 0.04      | 0.97       | -0.04    | 0.00  | 0.02      | 0.80       | 0.25    | 0.01   | 0.02      | 0.75       | 0.32    |
| mus ca edu b18   | 0.03     | 0.05      | 0.56       | 0.58     | -0.01 | 0.02      | 0.75       | -0.32   | -0.01  | 0.03      | 0.74       | -0.33   |
| mus qz tot sco   | 0.04     | 0.05      | 0.48       | 0.71     | -0.02 | 0.02      | 0.32       | -0.99   | 0.01   | 0.03      | 0.72       | 0.36    |
| moral n ave      | 0.04     | 0.03      | 0.16       | 1.42     | 0.03  | 0.01      | 0.07       | 1.79    | 0.01   | 0.02      | 0.43       | 0.80    |
| social n ave     | -0.01    | 0.03      | 0.79       | -0.27    | 0.00  | 0.01      | 0.80       | 0.25    | 0.00   | 0.01      | 0.78       | -0.28   |
| inc mo           | 0.01     | 0.01      | 0.48       | 0.70     | 0.00  | 0.01      | 0.38       | 0.88    | 0.00   | 0.01      | 0.79       | -0.27   |
| matarial dum     | 0.04     | 0.05      | 0.39       | 0.86     | 0.01  | 0.02      | 0.58       | 0.55    | 0.01   | 0.02      | 0.53       | 0.62    |
| constant         | 7.71     | 0.60      | p < 0.0001 | 12.85    | 8.62  | 0.27      | p < 0.0001 | 32.51   | 8.11   | 0.29      | p < 0.0001 | 27.55   |
| Model Statistics |          |           |            |          |       |           |            |         |        |           |            |         |
| Wald χ 2         |          | 16.42     |            |          |       |           | 37.77      |         |        | 26.87     |            |         |
| ρ                |          | 1.00      |            |          |       |           | -0.43      |         |        | 0.86      |            |         |
| σ                |          | 0.49      |            |          |       |           | 0.18       |         |        | 0.23      |            |         |
| Log Likelihood   |          | -250.78   |            |          |       |           | -250.78    |         |        | -250.78   |            |         |
| McFadden R 2     |          | 0.08      |            |          |       |           | 0.08       |         |        | 0.08      |            |         |
| N nonselected    |          | 113       |            |          |       |           | 113        |         |        | 113       |            |         |
| N selected       |          | 409       |            |          |       |           | 409        |         |        | 409       |            |         |

Table 8: Regression outcomes of Survey CoT on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   | LLaMA   | LLaMA     | LLaMA      | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|---------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff   | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |         |           |            |         |        |           |            |         |
| edu f            | -0.10    | 0.07      | 0.13       | -1.50    | -0.03   | 0.06      | 0.53       | -0.63   | -0.06  | 0.05      | 0.28       | -1.08   |
| edu m            | 0.03     | 0.07      | 0.62       | 0.49     | -0.02   | 0.05      | 0.64       | -0.46   | 0.00   | 0.05      | 0.93       | -0.08   |
| mus act dum      | -0.16    | 0.15      | 0.29       | -1.07    | -0.02   | 0.12      | 0.89       | -0.14   | -0.03  | 0.12      | 0.81       | -0.24   |
| mus att ave      | -0.07    | 0.20      | 0.71       | -0.37    | -0.12   | 0.17      | 0.50       | -0.68   | -0.16  | 0.16      | 0.34       | -0.96   |
| mus ca edu a19   | 0.03     | 0.06      | 0.60       | 0.52     | 0.03    | 0.05      | 0.50       | 0.68    | 0.03   | 0.05      | 0.55       | 0.61    |
| mus ca edu b18   | -0.04    | 0.06      | 0.53       | -0.62    | -0.02   | 0.05      | 0.63       | -0.48   | -0.03  | 0.05      | 0.52       | -0.64   |
| mus qz tot sco   | 0.04     | 0.07      | 0.53       | 0.63     | 0.11    | 0.06      | 0.05       | 1.95    | 0.11   | 0.06      | p < 0.05   | 2.05    |
| moral n ave      | 0.07     | 0.05      | 0.10       | 1.63     | 0.13    | 0.04      | p < 0.0001 | 3.12    | 0.09   | 0.04      | p < 0.05   | 2.20    |
| social n ave     | 0.02     | 0.04      | 0.59       | 0.54     | -0.02   | 0.04      | 0.71       | -0.38   | 0.04   | 0.04      | 0.32       | 0.98    |
| inc mo           | 0.02     | 0.02      | 0.31       | 1.01     | 0.02    | 0.02      | 0.14       | 1.48    | 0.02   | 0.02      | 0.29       | 1.06    |
| matarial dum     | 0.01     | 0.07      | 0.92       | 0.10     | -0.07   | 0.06      | 0.27       | -1.11   | -0.03  | 0.06      | 0.58       | -0.56   |
| constant         | 9.69     | 0.83      | p < 0.0001 | 11.68    | 9.80    | 0.72      | p < 0.0001 | 13.65   | 10.00  | 0.69      | p < 0.0001 | 14.43   |
| Model Statistics |          |           |            |          |         |           |            |         |        |           |            |         |
| Wald χ 2         |          | 14.54     |            |          |         |           | 29.98      |         |        | 23.01     |            |         |
| ρ                |          | -1.00     |            |          |         |           | -0.58      |         |        | -0.90     |            |         |
| σ                |          | 0.70      |            |          |         |           | 0.53       |         |        | 0.56      |            |         |
| Log Likelihood   |          | -290.01   |            |          |         |           | -290.01    |         |        | -290.01   |            |         |
| McFadden R 2     |          | 0.16      |            |          |         |           | 0.16       |         |        | 0.16      |            |         |
| N nonselected    |          | 195       |            |          |         |           | 195        |         |        | 195       |            |         |
| N selected       |          | 327       |            |          |         |           | 327        |         |        | 327       |            |         |

Table 9: Regression outcomes of Survey RAG on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   |       |           |            |         | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|-------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |       |           |            |         |        |           |            |         |
| edu f            | 0.01     | 0.04      | 0.75       | -0.32    | 0.02  | 0.02      | 0.46       | 0.73    | 0.00   | 0.01      | 0.97       | -0.04   |
| edu m            | -0.01    | 0.04      | 0.84       | -0.21    | 0.02  | 0.02      | 0.51       | 0.65    | 0.01   | 0.01      | 0.39       | 0.85    |
| mus act dum      | 0.08     | 0.09      | 0.36       | -1.59    | -0.03 | 0.05      | 0.56       | -0.58   | 0.00   | 0.02      | 0.88       | 0.15    |
| mus att ave      | 0.13     | 0.08      | 0.11       | -0.37    | 0.06  | 0.05      | 0.21       | 1.26    | 0.00   | 0.02      | 0.81       | 0.25    |
| mus ca edu a19   | -0.01    | 0.03      | 0.71       | -0.57    | 0.00  | 0.02      | 0.98       | 0.03    | -0.01  | 0.01      | 0.08       | -1.73   |
| mus ca edu b18   | 0.02     | 0.04      | 0.57       | -0.17    | -0.02 | 0.02      | 0.32       | -0.99   | 0.00   | 0.01      | 0.92       | -0.10   |
| mus qz tot sco   | -0.01    | 0.04      | 0.86       | 0.14     | 0.00  | 0.02      | 0.83       | -0.21   | -0.01  | 0.01      | 0.05       | -1.96   |
| moral n ave      | 0.00     | 0.02      | 0.89       | -0.03    | -0.01 | 0.01      | 0.45       | -0.76   | 0.00   | 0.00      | 0.32       | -0.99   |
| social n ave     | 0.00     | 0.02      | 0.97       | -0.06    | 0.00  | 0.01      | 0.81       | -0.24   | 0.01   | 0.00      | 0.17       | 1.36    |
| inc mo           | 0.00     | 0.01      | 0.95       | 0.36     | 0.00  | 0.00      | 0.70       | -0.39   | 0.00   | 0.00      | 0.38       | 0.87    |
| matarial dum     | 0.01     | 0.04      | 0.72       | 0.36     | 0.01  | 0.02      | 0.70       | -0.38   | 0.00   | 0.01      | 0.83       | -0.21   |
| constant         | 8.35     | 0.44      | p < 0.0001 | 19.19    | 8.41  | 0.26      | p < 0.0001 | -32.65  | 8.51   | 0.09      | p < 0.0001 | -95.45  |
| Model Statistics |          |           |            |          |       |           |            |         |        |           |            |         |
| Wald χ 2         |          | 10.45     |            |          |       |           | 28.81      |         |        | 15.87     |            |         |
| ρ                |          | 1.00      |            |          |       |           | -0.25      |         |        | -0.33     |            |         |
| σ                |          | 0.36      |            |          |       |           | 0.18       |         |        | 0.06      |            |         |
| Log Likelihood   |          | -250.78   |            |          |       |           | -250.78    |         |        | -250.78   |            |         |
| McFadden R 2     |          | 0.08      |            |          |       |           | 0.08       |         |        | 0.08      |            |         |
| N nonselected    |          | 113       |            |          |       |           | 113        |         |        | 113       |            |         |
| N selected       |          | 409       |            |          |       |           | 409        |         |        | 409       |            |         |

Table 10: Regression outcomes of Survey RAG on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   | LLaMA   | LLaMA     | LLaMA      | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|---------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff   | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |         |           |            |         |        |           |            |         |
| edu f            | -0.05    | 0.03      | 0.14       | -1.49    | -0.06   | 0.03      | 0.06       | -1.85   | -0.08  | 0.06      | 0.14       | -1.48   |
| edu m            | 0.00     | 0.03      | 0.97       | -0.03    | 0.02    | 0.03      | 0.56       | 0.58    | -0.01  | 0.05      | 0.86       | -0.18   |
| mus act dum      | -0.03    | 0.07      | 0.70       | -0.38    | -0.06   | 0.07      | 0.39       | -0.85   | -0.24  | 0.12      | p < 0.05   | -2.02   |
| mus att ave      | 0.02     | 0.10      | 0.82       | 0.23     | -0.05   | 0.10      | 0.61       | -0.51   | 0.11   | 0.17      | 0.53       | -0.63   |
| mus ca edu a19   | 0.03     | 0.03      | 0.23       | 1.21     | 0.02    | 0.03      | 0.58       | 0.55    | -0.05  | 0.05      | 0.27       | -1.11   |
| mus ca edu b18   | -0.01    | 0.03      | 0.71       | -0.38    | -0.04   | 0.03      | 0.14       | -1.49   | 0.00   | 0.05      | 0.95       | -0.06   |
| mus qz tot sco   | 0.06     | 0.03      | p < 0.05   | 2.05     | 0.03    | 0.03      | 0.30       | 1.04    | 0.00   | 0.06      | 0.94       | -0.07   |
| moral n ave      | 0.04     | 0.02      | 0.13       | 1.51     | 0.03    | 0.02      | 0.26       | 1.12    | -0.07  | 0.05      | 0.13       | -1.51   |
| social n ave     | 0.03     | 0.02      | 0.22       | 1.22     | 0.02    | 0.02      | 0.31       | 1.02    | 0.07   | 0.04      | 0.09       | -1.68   |
| inc mo           | 0.01     | 0.01      | 0.14       | 1.49     | 0.00    | 0.01      | 0.65       | 0.46    | 0.01   | 0.02      | 0.38       | -0.88   |
| matarial dum     | 0.01     | 0.03      | 0.82       | 0.23     | 0.01    | 0.04      | 0.88       | 0.15    | -0.06  | 0.06      | 0.35       | -0.93   |
| constant         | 9.32     | 0.41      | p < 0.0001 | 22.70    | 10.08   | 0.41      | p < 0.0001 | 24.34   | 9.81   | 0.73      | p < 0.0001 | -13.47  |
| Model Statistics |          |           |            |          |         |           |            |         |        |           |            |         |
| Wald χ 2         |          | 30.46     |            |          |         |           | 14.85      |         |        | 22.56     |            |         |
| ρ                |          | -0.45     |            |          |         |           | -1.00      |         |        | -0.11     |            |         |
| σ                |          | 0.30      |            |          |         |           | 0.35       |         |        | 0.51      |            |         |
| Log Likelihood   |          | -290.01   |            |          |         |           | -290.01    |         |        | -590.01   |            |         |
| McFadden R 2     |          | 0.16      |            |          |         |           | 0.16       |         |        | 0.16      |            |         |
| N nonselected    |          | 195       |            |          |         |           | 195        |         |        | 195       |            |         |
| N selected       |          | 327       |            |          |         |           | 327        |         |        | 327       |            |         |

Table 11: Regression outcomes of Survey few-shot on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o   | GPT-4o   |       |           |          |         | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|----------|----------|-------|-----------|----------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value  | z value  | coeff | std error | p value  | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |          |          |       |           |          |         |        |           |            |         |
| edu f            | -0.22    | 0.34      | 0.53     | -0.63    | -0.04 | 0.40      | 0.92     | -0.10   | 0.03   | 0.03      | 0.46       | 0.74    |
| edu m            | 0.26     | 0.40      | 0.51     | -0.66    | 0.05  | 0.46      | 0.91     | 0.11    | -0.03  | 0.04      | 0.51       | -0.65   |
| mus act dum      | -0.48    | 0.82      | 0.56     | -0.59    | 0.32  | 0.98      | 0.75     | 0.32    | 0.04   | 0.08      | 0.62       | -0.50   |
| mus att ave      | -0.10    | 0.75      | 0.89     | -0.14    | -0.32 | 0.89      | 0.72     | -0.35   | 0.09   | 0.08      | 0.24       | 1.17    |
| mus ca edu a19   | -0.02    | 0.27      | 0.95     | -0.06    | -0.29 | 0.30      | 0.33     | -0.97   | 0.00   | 0.03      | 0.97       | -0.04   |
| mus ca edu b18   | -0.21    | 0.36      | 0.55     | -0.60    | -0.12 | 0.42      | 0.78     | -0.28   | 0.02   | 0.04      | 0.53       | 0.63    |
| mus qz tot sco   | 0.12     | 0.34      | 0.73     | 0.34     | 0.16  | 0.40      | 0.68     | 0.41    | 0.02   | 0.03      | 0.55       | 0.59    |
| moral n ave      | 0.21     | 0.20      | 0.31     | 1.02     | -0.25 | 0.25      | 0.32     | -0.99   | 0.00   | 0.02      | 0.93       | -0.08   |
| social n ave     | -0.05    | 0.19      | 0.79     | -0.26    | 0.23  | 0.23      | 0.32     | 0.99    | 0.02   | 0.02      | 0.36       | 0.92    |
| inc mo           | 0.03     | 0.08      | 0.70     | 0.38     | -0.09 | 0.09      | 0.35     | -0.94   | 0.00   | 0.01      | 0.57       | 0.56    |
| matarial dum     | -0.03    | 0.32      | 0.92     | -0.09    | -0.75 | 0.36      | p < 0.05 | -2.07   | 0.00   | 0.03      | 0.95       | 0.06    |
| constant         | 9.01     | 3.93      | p < 0.05 | 2.30     | -8.45 | 4.71      | 0.07     | 1.79    | 8.44   | 0.40      | p < 0.0001 | 21.17   |
| Model Statistics |          |           |          |          |       |           |          |         |        |           |            |         |
| Wald χ 2         |          | 3.82      |          |          |       | 21.44     |          |         |        | 5.55      |            |         |
| rho              |          | -1.00     |          |          |       | -0.76     |          |         |        | 1.00      |            |         |
| σ                |          | 3.23      |          |          |       |           | 3.53     |         |        | 0.33      |            |         |
| Log Likelihood   |          | -250.78   |          |          |       | -250.78   |          |         |        | -250.78   |            |         |
| McFadden R 2     |          | 0.08      |          |          |       | 0.08      |          |         |        | 0.08      |            |         |
| N nonselected    |          | 113       |          |          |       |           | 113      |         |        | 113       |            |         |
| N selected       |          | 409       |          |          |       |           | 409      |         |        | 409       |            |         |

Table 12: Regression outcomes of Survey few-shot on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   | LLaMA   | LLaMA     | LLaMA      | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|---------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff   | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |         |           |            |         |        |           |            |         |
| edu f            | -0.14    | 0.12      | 0.24       | -1.17    | -0.04   | 0.21      | 0.84       | -0.20   | -0.03  | 0.02      | 0.14       | -1.47   |
| edu m            | 0.05     | 0.12      | 0.68       | -0.41    | -0.02   | 0.21      | 0.94       | -0.07   | 0.01   | 0.02      | 0.78       | 0.27    |
| mus act dum      | -0.21    | 0.28      | 0.45       | -0.75    | -0.36   | 0.47      | 0.45       | -0.75   | -0.01  | 0.05      | 0.90       | -0.13   |
| mus att ave      | -0.27    | 0.36      | 0.46       | -0.74    | -0.54   | 0.62      | 0.39       | -0.87   | 0.06   | 0.07      | 0.44       | 0.77    |
| mus ca edu a19   | 0.01     | 0.12      | 0.93       | 0.09     | 0.01    | 0.20      | 0.98       | 0.03    | 0.04   | 0.02      | 0.08       | 1.74    |
| mus ca edu b18   | -0.05    | 0.11      | 0.67       | -0.43    | -0.10   | 0.18      | 0.59       | -0.54   | -0.02  | 0.02      | 0.42       | -0.80   |
| mus qz tot sco   | -0.01    | 0.12      | 0.96       | -0.05    | 0.11    | 0.21      | 0.60       | 0.52    | 0.04   | 0.02      | 0.07       | 1.78    |
| moral n ave      | 0.11     | 0.08      | 0.20       | 1.29     | 0.18    | 0.14      | 0.21       | 1.25    | 0.03   | 0.02      | 0.06       | 1.85    |
| social n ave     | 0.01     | 0.08      | 0.91       | 0.11     | 0.08    | 0.14      | 0.57       | 0.57    | 0.01   | 0.02      | 0.45       | 0.76    |
| inc mo           | 0.03     | 0.04      | 0.39       | 0.86     | 0.02    | 0.06      | 0.73       | -0.34   | 0.03   | 0.01      | p < 0.0001 | 4.12    |
| matarial dum     | 0.05     | 0.13      | 0.71       | 0.38     | -0.03   | 0.23      | 0.90       | -0.13   | -0.02  | 0.03      | 0.41       | -0.83   |
| constant         | 10.52    | 1.54      | p < 0.0001 | 6.85     | 11.30   | 2.63      | p < 0.0001 | 4.29    | 9.52   | 0.30      | p < 0.0001 | -31.25  |
| Model Statistics |          |           |            |          |         |           |            |         |        |           |            |         |
| Wald χ 2         |          | 5.72      |            |          |         |           | 3.92       |         |        | 45.74     |            |         |
| rho              |          | -1.00     |            |          |         |           | -1.00      |         |        | -0.55     |            |         |
| σ                |          | 1.29      |            |          |         |           | 2.21       |         |        | 0.22      |            |         |
| Log Likelihood   |          | -290.01   |            |          |         |           | -290.01    |         |        | -290.01   |            |         |
| McFadden R 2     |          | 0.16      |            |          |         |           | 0.16       |         |        | 0.16      |            |         |
| N nonselected    |          | 195       |            |          |         |           | 195        |         |        | 195       |            |         |
| N selected       |          | 327       |            |          |         |           | 327        |         |        | 327       |            |         |

Table 13: Regression outcomes of Storytelling Base on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   |       |           |            |         | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|-------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |       |           |            |         |        |           |            |         |
| edu f            | 0.02     | 0.07      | 0.76       | 0.30     | -0.07 | 0.08      | 0.38       | -0.87   | 0.00   | 0.00      | 0.73       | -0.35   |
| edu m            | -0.01    | 0.08      | 0.91       | -0.11    | 0.09  | 0.09      | 0.30       | 1.03    | 0.00   | 0.00      | 0.20       | 1.27    |
| mus act dum      | 0.12     | 0.17      | 0.48       | 0.71     | -0.13 | 0.19      | 0.50       | -0.68   | 0.00   | 0.00      | 0.42       | -0.80   |
| mus att ave      | 0.19     | 0.15      | 0.21       | 1.25     | 0.04  | 0.17      | 0.82       | 0.22    | 0.00   | 0.00      | 0.36       | -0.92   |
| mus ca edu a19   | -0.03    | 0.05      | 0.53       | -0.63    | 0.01  | 0.06      | 0.82       | 0.22    | 0.00   | 0.00      | 0.13       | 1.53    |
| mus ca edu b18   | 0.05     | 0.07      | 0.50       | 0.68     | -0.03 | 0.08      | 0.74       | -0.33   | 0.00   | 0.00      | 0.75       | -0.32   |
| mus qz tot sco   | 0.01     | 0.07      | 0.90       | 0.12     | -0.06 | 0.08      | 0.46       | -0.74   | 0.00   | 0.00      | 0.90       | -0.12   |
| moral n ave      | 0.00     | 0.04      | 0.94       | -0.08    | -0.02 | 0.05      | 0.72       | -0.36   | 0.00   | 0.00      | 0.07       | 1.79    |
| social n ave     | 0.00     | 0.04      | 0.91       | -0.11    | -0.01 | 0.04      | 0.83       | -0.21   | 0.00   | 0.00      | 0.63       | -0.48   |
| inc mo           | -0.01    | 0.02      | 0.63       | -0.48    | 0.01  | 0.02      | 0.70       | 0.39    | 0.00   | 0.00      | 0.19       | -1.31   |
| matarial dum     | 0.01     | 0.06      | 0.91       | 0.12     | -0.02 | 0.07      | 0.83       | -0.21   | 0.00   | 0.00      | 0.62       | -0.49   |
| constant         | 8.14     | 0.79      | p < 0.0001 | 10.30    | 8.84  | 0.89      | p < 0.0001 | 9.90    | 8.52   | 0.02      | p < 0.0001 | 505.52  |
| Model Statistics |          |           |            |          |       |           |            |         |        |           |            |         |
| Wald χ 2         |          | 3.85      |            |          |       |           | 6.29       |         |        | 14.58     |            |         |
| ρ                |          | 1.00      |            |          |       |           | -1.00      |         |        | -1.00     |            |         |
| σ                |          | 0.65      |            |          |       |           | 0.74       |         |        | 0.01      |            |         |
| Log Likelihood   |          | -250.78   |            |          |       |           | -250.78    |         |        | -250.78   |            |         |
| McFadden R 2     |          | 0.08      |            |          |       |           | 0.08       |         |        | 0.08      |            |         |
| N nonselected    |          | 113       |            |          |       |           | 113        |         |        | 113       |            |         |
| N selected       |          | 409       |            |          |       |           | 409        |         |        | 409       |            |         |

Table 14: Regression outcomes of Storytelling Base on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   |       |           |            |         | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|-------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |       |           |            |         |        |           |            |         |
| edu f            | -0.03    | 0.03      | 0.32       | -0.99    | -0.03 | 0.05      | 0.53       | -0.63   | -0.07  | 0.03      | p < 0.05   | -2.22   |
| edu m            | -0.01    | 0.03      | 0.66       | -0.44    | -0.02 | 0.05      | 0.72       | -0.36   | -0.01  | 0.03      | 0.85       | -0.19   |
| mus act dum      | 0.00     | 0.06      | 0.97       | -0.03    | 0.02  | 0.12      | 0.87       | -0.17   | -0.06  | 0.07      | 0.43       | -0.79   |
| mus att ave      | 0.11     | 0.09      | 0.20       | 1.27     | -0.11 | 0.16      | 0.52       | -0.64   | -0.04  | 0.10      | 0.66       | -0.44   |
| mus ca edu a19   | 0.04     | 0.03      | 0.08       | 1.74     | 0.04  | 0.05      | 0.45       | 0.75    | 0.01   | 0.03      | 0.66       | 0.44    |
| mus ca edu b18   | 0.00     | 0.02      | 0.95       | 0.06     | -0.03 | 0.05      | 0.49       | -0.69   | -0.02  | 0.03      | 0.48       | -0.71   |
| mus qz tot sco   | 0.05     | 0.03      | 0.07       | 1.81     | 0.12  | 0.05      | p < 0.05   | 2.32    | 0.04   | 0.03      | 0.22       | 1.22    |
| moral n ave      | 0.02     | 0.02      | 0.30       | 1.05     | 0.13  | 0.04      | p < 0.0001 | 3.01    | 0.05   | 0.02      | 0.05       | 2.00    |
| social n ave     | 0.02     | 0.02      | 0.44       | 0.78     | -0.01 | 0.04      | 0.74       | -0.33   | 0.00   | 0.02      | 0.91       | 0.11    |
| inc mo           | 0.01     | 0.01      | 0.26       | 1.13     | 0.02  | 0.02      | 0.23       | 1.21    | 0.01   | 0.01      | 0.34       | 0.96    |
| matarial dum     | 0.01     | 0.03      | 0.77       | 0.30     | -0.06 | 0.06      | 0.32       | -1.00   | -0.03  | 0.03      | 0.34       | -0.95   |
| constant         | 9.07     | 0.37      | p < 0.0001 | 24.47    | 9.77  | 0.70      | p < 0.0001 | 14.05   | 9.91   | 0.40      | p < 0.0001 | -24.67  |
| Model Statistics |          |           |            |          |       |           |            |         |        |           |            |         |
| Wald χ 2         |          | 31.27     |            |          |       |           | 31.22      |         |        | 26.14     |            |         |
| ρ                |          | 0.41      |            |          |       |           | -0.43      |         |        | -0.87     |            |         |
| σ                |          | 0.27      |            |          |       |           | 0.50       |         |        | 0.32      |            |         |
| Log Likelihood   |          | -290.01   |            |          |       |           | -290.01    |         |        | -290.01   |            |         |
| McFadden R 2     |          | 0.16      |            |          |       |           | 0.16       |         |        | 0.16      |            |         |
| N nonselected    |          | 195       |            |          |       |           | 195        |         |        | 195       |            |         |
| N selected       |          | 327       |            |          |       |           | 327        |         |        | 327       |            |         |

Table 15: Regression outcomes of Storytelling CoT on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   |       |           |            |         | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|-------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |       |           |            |         |        |           |            |         |
| edu f            | -0.01    | 0.06      | 0.84       | -0.21    | 0.03  | 0.06      | 0.67       | 0.42    | 0.06   | 0.10      | 0.56       | 0.59    |
| edu m            | 0.02     | 0.06      | 0.71       | 0.37     | 0.00  | 0.07      | 0.98       | -0.03   | -0.04  | 0.12      | 0.70       | -0.38   |
| mus act dum      | -0.07    | 0.13      | 0.58       | -0.55    | 0.15  | 0.15      | 0.31       | 1.01    | 0.20   | 0.24      | 0.41       | 0.82    |
| mus att ave      | 0.02     | 0.12      | 0.86       | 0.18     | 0.14  | 0.14      | 0.29       | 1.05    | 0.21   | 0.22      | 0.34       | 0.95    |
| mus ca edu a19   | 0.00     | 0.04      | 0.96       | 0.05     | -0.01 | 0.05      | 0.82       | -0.23   | 0.03   | 0.08      | 0.71       | 0.37    |
| mus ca edu b18   | -0.03    | 0.06      | 0.57       | -0.57    | 0.05  | 0.07      | 0.45       | 0.75    | 0.09   | 0.10      | 0.37       | 0.90    |
| mus qz tot sco   | -0.01    | 0.06      | 0.79       | -0.27    | 0.01  | 0.06      | 0.88       | 0.15    | 0.01   | 0.10      | 0.90       | 0.13    |
| moral n ave      | 0.03     | 0.03      | 0.44       | 0.77     | 0.02  | 0.04      | 0.58       | 0.55    | 0.00   | 0.06      | 0.97       | -0.03   |
| social n ave     | 0.00     | 0.03      | 0.97       | -0.03    | -0.01 | 0.03      | 0.71       | -0.37   | 0.00   | 0.05      | 0.96       | -0.05   |
| inc mo           | 0.00     | 0.01      | 0.78       | 0.28     | 0.00  | 0.02      | 0.99       | 0.02    | 0.00   | 0.02      | 0.84       | 0.20    |
| matarial dum     | -0.02    | 0.05      | 0.75       | -0.32    | 0.02  | 0.06      | 0.78       | 0.28    | 0.00   | 0.09      | 0.99       | -0.02   |
| constant         | 8.71     | 0.64      | p < 0.0001 | 13.64    | 8.07  | 0.72      | p < 0.0001 | 11.21   | 7.71   | 1.15      | p < 0.0001 | 6.72    |
| Model Statistics |          |           |            |          |       |           |            |         |        |           |            |         |
| Wald χ 2         |          | 3.89      |            |          |       |           | 4.15       |         |        | 2.02      |            |         |
| ρ                |          | -1.00     |            |          |       |           | 1.00       |         |        | 1.00      |            |         |
| σ                |          | 0.53      |            |          |       |           | 0.59       |         |        | 0.94      |            |         |
| Log Likelihood   |          | -250.78   |            |          |       |           | -250.78    |         |        | -280.78   |            |         |
| McFadden R 2     |          | 0.08      |            |          |       |           | 0.08       |         |        | 0.08      |            |         |
| N nonselected    |          | 113       |            |          |       |           | 113        |         |        | 113       |            |         |
| N selected       |          | 409       |            |          |       |           | 409        |         |        | 409       |            |         |

Table 16: Regression outcomes of Storytelling CoT on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   | LLaMA   | LLaMA     | LLaMA      | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|---------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff   | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |         |           |            |         |        |           |            |         |
| edu f            | -0.05    | 0.04      | 0.21       | -1.26    | -0.06   | 0.06      | 0.30       | -1.03   | 0.31   | 0.16      | 0.06       | 1.91    |
| edu m            | 0.03     | 0.04      | 0.46       | 0.74     | -0.03   | 0.05      | 0.61       | -0.50   | -0.46  | 0.16      | p < 0.0001 | -2.86   |
| mus act dum      | -0.01    | 0.08      | 0.90       | -0.12    | -0.03   | 0.12      | 0.78       | -0.27   | 0.15   | 0.36      | 0.67       | -0.42   |
| mus att ave      | 0.04     | 0.11      | 0.71       | 0.37     | -0.07   | 0.17      | 0.68       | -0.42   | 0.69   | 0.50      | 0.17       | -1.37   |
| mus ca edu a19   | 0.04     | 0.03      | 0.27       | 1.09     | 0.01    | 0.05      | 0.77       | 0.29    | 0.22   | 0.15      | 0.14       | -1.47   |
| mus ca edu b18   | 0.00     | 0.03      | 0.98       | -0.03    | -0.02   | 0.05      | 0.61       | -0.51   | 0.06   | 0.14      | 0.68       | -0.41   |
| mus qz tot sco   | 0.07     | 0.04      | 0.05       | 1.93     | 0.12    | 0.06      | p < 0.05   | 2.05    | -0.22  | 0.17      | 0.18       | -1.34   |
| moral n ave      | 0.09     | 0.03      | p < 0.0001 | 2.97     | 0.14    | 0.04      | p < 0.0001 | 3.14    | 0.11   | 0.13      | 0.40       | 0.83    |
| social n ave     | -0.02    | 0.03      | 0.46       | -0.73    | 0.01    | 0.04      | 0.83       | 0.21    | 0.16   | 0.12      | 0.18       | 1.33    |
| inc mo           | 0.01     | 0.01      | 0.21       | 1.25     | 0.03    | 0.02      | 0.07       | 1.78    | -0.02  | 0.05      | 0.75       | -0.32   |
| matarial dum     | -0.03    | 0.04      | 0.50       | -0.67    | 0.06    | 0.06      | 0.32       | -1.00   | -0.15  | 0.18      | 0.40       | -0.84   |
| constant         | 9.19     | 0.48      | p < 0.0001 | -19.15   | 9.50    | 0.73      | p < 0.0001 | 13.00   | 6.44   | 2.12      | p < 0.0001 | 3.03    |
| Model Statistics |          |           |            |          |         |           |            |         |        |           |            |         |
| Wald χ 2         |          | 27.60     |            |          |         |           | 34.69      |         |        | 17.90     |            |         |
| ρ                |          | -0.36     |            |          |         |           | -0.51      |         |        | 0.67      |            |         |
| σ                |          | 0.34      |            |          |         |           | -0.53      |         |        | 1.60      |            |         |
| Log Likelihood   |          | -290.01   |            |          |         |           | -290.01    |         |        | -290.01   |            |         |
| McFadden R 2     |          | 0.16      |            |          |         |           | -16        |         |        | 0.16      |            |         |
| N nonselected    |          | 195       |            |          |         |           | 195        |         |        |           | 195        |         |
| N selected       |          | 327       |            |          |         |           | 327        |         |        |           | 327        |         |

Table 17: Regression outcomes of Storytelling RAG on the art PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions. In Qwen, as all values were measured identitically, statistical analysis becomes impossible.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   |       |           |            |         | Qwen   | Qwen      | Qwen    | Qwen    |
|------------------|----------|-----------|------------|----------|-------|-----------|------------|---------|--------|-----------|---------|---------|
|                  | coeff    | std error | p value    | z value  | coeff | std error | p value    | z value | coeff  | std error | p value | z value |
| Outcome          |          |           |            |          |       |           |            |         |        |           |         |         |
| edu f            | 0.01     | 0.04      | 0.85       | 0.85     | 0.00  | 0.01      | 0.48       | 0.71    | -      | -         | -       | -       |
| edu m            | -0.01    | 0.04      | 0.85       | 0.85     | -0.01 | 0.01      | 0.29       | -1.06   | -      | -         | -       | -       |
| mus act dum      | 0.05     | 0.09      | 0.59       | 0.53     | 0.01  | 0.01      | 0.57       | 0.05    | -      | -         | -       | -       |
| mus att ave      | 0.12     | 0.08      | 0.15       | 1.44     | 0.01  | 0.01      | 0.36       | 0.92    | -      | -         | -       | -       |
| mus ca edu a19   | -0.03    | 0.03      | 0.29       | -1.06    | 0.00  | 0.00      | 0.89       | 0.14    | -      | -         | -       | -       |
| mus ca edu b18   | -0.01    | 0.04      | 0.89       | -0.14    | 0.00  | 0.01      | 0.66       | 0.45    | -      | -         | -       | -       |
| mus qz tot sco   | 0.01     | 0.04      | 0.72       | 0.36     | 0.01  | 0.01      | 0.39       | 0.87    | -      | -         | -       | -       |
| moral n ave      | 0.04     | 0.02      | 0.11       | 1.61     | 0.00  | 0.00      | 0.30       | 1.05    | -      | -         | -       | -       |
| social n ave     | -0.03    | 0.02      | 0.09       | -1.69    | 0.00  | 0.00      | 0.67       | -0.43   | -      | -         | -       | -       |
| inc mo           | 0.01     | 0.01      | 0.38       | 0.88     | 0.00  | 0.00      | 0.86       | 0.18    | -      | -         | -       | -       |
| matarial dum     | -0.01    | 0.03      | 0.72       | -0.36    | 0.00  | 0.01      | 0.81       | 0.24    | -      | -         | -       | -       |
| constant         | 8.31     | 0.42      | p < 0.0001 | 19.63    | 8.44  | 0.07      | p < 0.0001 | 118.37  | -      | -         | -       | -       |
| Model Statistics |          |           |            |          |       |           |            |         |        |           |         |         |
| Wald χ 2         |          | 21.11     |            |          |       |           | 5.10       |         |        |           | -       |         |
| ρ                |          | 0.72      |            |          |       |           | 0.99       |         |        |           | -       |         |
| σ                |          | 0.31      |            |          |       |           | 0.06       |         |        |           | -       |         |
| Log Likelihood   |          | -250.78   |            |          |       |           | -250.78    |         |        |           | -       |         |
| McFadden R 2     |          | 0.08      |            |          |       |           | 0.08       |         |        |           | -       |         |
| N nonselected    |          | 113       |            |          |       |           | 113        |         |        |           | -       |         |
| N selected       |          | 409       |            |          |       |           | 409        |         |        | -         |         |         |

Table 18: Regression outcomes of Storytelling RAG on the music PWYW decision-making task. The table reports coefficients, standard errors, z-values, and p-values from a Heckman two-step model. Bottom panel presents model-level statistics including selection bias correction and sample distributions.

|                  | GPT-4o   | GPT-4o    | GPT-4o     | GPT-4o   | LLaMA   | LLaMA     | LLaMA      | LLaMA   | Qwen   | Qwen      | Qwen       | Qwen    |
|------------------|----------|-----------|------------|----------|---------|-----------|------------|---------|--------|-----------|------------|---------|
|                  | coeff    | std error | p value    | z value  | coeff   | std error | p value    | z value | coeff  | std error | p value    | z value |
| Outcome          |          |           |            |          |         |           |            |         |        |           |            |         |
| edu f            | -0.04    | 0.03      | 0.15       | -1.44    | -0.06   | 0.03      | p < 0.05   | -2.36   | -0.03  | 0.04      | 0.43       | -0.79   |
| edu m            | -0.01    | 0.03      | 0.83       | -0.21    | 0.02    | 0.02      | 0.52       | 0.65    | -0.04  | 0.04      | 0.26       | -1.12   |
| mus act dum      | -0.02    | 0.06      | 0.76       | -0.31    | -0.05   | 0.06      | 0.41       | -0.83   | -0.02  | 0.09      | 0.78       | -0.27   |
| mus att ave      | 0.02     | 0.09      | 0.81       | 0.23     | -0.03   | 0.08      | 0.67       | -0.42   | 0.04   | 0.12      | 0.72       | 0.36    |
| mus ca edu a19   | 0.03     | 0.03      | 0.21       | 1.25     | 0.01    | 0.02      | 0.71       | 0.37    | 0.05   | 0.04      | 0.18       | 1.34    |
| mus ca edu b18   | -0.02    | 0.02      | 0.52       | -0.64    | -0.01   | 0.02      | 0.72       | -0.36   | -0.03  | 0.03      | 0.31       | -1.02   |
| mus qz tot sco   | 0.05     | 0.03      | 0.10       | 1.64     | 0.05    | 0.03      | 0.06       | 1.90    | 0.04   | 0.04      | 0.35       | 0.94    |
| moral n ave      | 0.03     | 0.02      | 0.13       | 1.44     | 0.04    | 0.02      | p < 0.05   | 2.39    | 0.03   | 0.03      | 0.31       | 1.02    |
| social n ave     | 0.02     | 0.01      | 0.22       | 0.77     | 0.01    | 0.02      | 0.65       | 0.45    | 0.02   | 0.03      | 0.41       | 0.98    |
| inc mo           | 0.01     | 0.01      | 0.42       | 0.80     | 0.00    | 0.01      | 0.56       | 0.59    | 0.00   | 0.01      | 0.99       | 0.34    |
| matarial dum     | 0.00     | 0.03      | 0.92       | 0.10     | 0.00    | 0.03      | 0.87       | 0.16    | 0.00   | 0.04      | p < 0.05   | 0.01    |
| constant         | 9.46     | 0.37      | p < 0.0001 | 25.32    | 9.89    | 0.33      | p < 0.0001 | 30.24   | 9.57   | 0.52      | p < 0.0001 | 18.48   |
| Model Statistics |          |           |            |          |         |           |            |         |        |           |            |         |
| Wald χ 2         |          | 23.42     |            |          |         |           | 26.57      |         |        | 22.24     |            |         |
| ρ                |          | -0.39     |            |          |         |           | -0.82      |         |        | -0.29     |            |         |
| σ                |          | 0.27      |            |          |         |           | 0.26       |         |        | 0.37      |            |         |
| Log Likelihood   |          | -290.01   |            |          |         |           | -290.01    |         |        | -290.01   |            |         |
| McFadden R 2     |          | 0.16      |            |          |         |           | 0.16       |         |        | 0.16      |            |         |
| N nonselected    |          | 195       |            |          |         |           | 195        |         |        | 195       |            |         |
| N selected       |          | 327       |            |          |         |           | 327        |         |        | 327       |            |         |

- 국 · 공 립 박 물 관 및 공 연 장 관 람 료 에 대 한 소 비 자 설 문 조 사

Consumer Survey on Admission Fees for National/Public Museums and Performance Halls
