## E Efficiency Experiment Details

For efficiency experiments, the results depend on both the size of the model and the tokenizer's vocabulary size. We used Llama-3.1-8B-Instruct (quantized to Q8bit) with

a 128K token vocabulary to achieve a balance between computational efficiency and model capability.

Below, we outline specific considerations related to grammar and prefix caching:

- Grammar Cache (Compilation): Since each schema in the dataset is unique, caching grammar compilations does not offer any benefits.
- Prefix Cache (LLM Inference): We implement prefix caching during LLM inference for all cases to enhance efficiency by reusing computed results where applicable.

Table 13: Efficiency metrics for different engines with LlamaCpp as the inference engine. GCT : Grammar Compilation Time, TTFT : Time to First Token, TPOT : Time Per Output Token, TGT : Total Generation Time, FF : Fast-Forwarded output tokens. Bold values indicate the smallest in each column for GCT, TTFT, TPOT, and TGT. All values are median of the samples.

| Dataset       | Framework   | GCT (s)   |   TTFT (s) |   TPOT (ms) |   TGT (s) | Output Tokens (FF)   |
|---------------|-------------|-----------|------------|-------------|-----------|----------------------|
| GlaiveAI      | LLM only    | NA        |       0.1  |       15.4  |      1.08 | 64.94 (00.00)        |
|               | Guidance    | 0.00      |       0.24 |        6.37 |      0.5  | 41.56 (15.70)        |
|               | Llamacpp    | 0.05      |       0.2  |       29.98 |      1.47 | 43.18 (00.00)        |
|               | Outlines    | 3.48      |       3.65 |       30.33 |      4.84 | 40.39 (00.00)        |
| GitHub Easy   | LLM only    | NA        |       0.1  |       15.83 |      0.95 | 53.91 (00.00)        |
|               | Guidance    | 0.00      |       0.34 |        7.44 |      0.6  | 34.92 (10.02)        |
|               | Llamacpp    | 0.05      |       0.18 |       27.22 |      1.1  | 33.93 (00.00)        |
|               | Outlines    | 3.71      |       3.97 |       39.78 |      5.29 | 34.19 (00.00)        |
| Snowplow      | LLM only    | NA        |       0.11 |       16.23 |      1.01 | 55.31 (00.00)        |
|               | Guidance    | 0.00      |       0.28 |        6.55 |      0.51 | 36.77 (14.50)        |
|               | Llamacpp    | 0.05      |       0.2  |       28.9  |      1.24 | 37.21 (00.00)        |
|               | Outlines    | 3.91      |       4.14 |       42.66 |      5.65 | 35.65 (00.00)        |
| GitHub Medium | LLM only    | NA        |       0.2  |       16.68 |      2.56 | 142.10 (00.00)       |
|               | Guidance    | 0.01      |       0.54 |        7.57 |      1.29 | 99.66 (31.42)        |
|               | Llamacpp    | 0.06      |       0.3  |       29.08 |      2.85 | 87.71 (00.00)        |
|               | Outlines    | 8.05      |       8.38 |       46.57 |     12.23 | 84.64 (00.00)        |
| Kubernetes    | LLM only    | NA        |       0.16 |       15.32 |      0.84 | 44.38 (00.00)        |
|               | Guidance    | 0.01      |       0.45 |        9.47 |      0.71 | 28.75 (04.40)        |
|               | Llamacpp    | 0.05      |       0.28 |       28.04 |      1.06 | 28.09 (00.00)        |
|               | Outlines    | 5.29      |       5.55 |       46.1  |      6.56 | 22.26 (00.00)        |

Table 14: Efficiency metrics for different engines with Hugging Face Transformers as the inference engine. All values are median of the samples.

| Dataset       | Framework   |   GCT (s) |   TTFT (s) |   TPOT (ms) |   TGT (s) | Output Tokens (FF)   |
|---------------|-------------|-----------|------------|-------------|-----------|----------------------|
| GlaiveAI      | Guidance    |      0.01 |       0.36 |       36.92 |      1.87 | 41.45(16.76)         |
|               | XGrammar    |      0.12 |       0.3  |       66.78 |      2.87 | 39.47(00.00)         |
| GitHub Easy   | Guidance    |      0.01 |       0.37 |       42.03 |      1.6  | 27.67(06.75)         |
| GitHub Easy   | XGrammar    |      0.11 |       0.33 |       65.57 |      4.07 | 59.45(00.00)         |
| GitHub Medium | Guidance    |      0.01 |       0.55 |       44.21 |      4.84 | 96.31(26.93)         |
| GitHub Medium | XGrammar    |      0.2  |       0.48 |       65.51 |      6.53 | 92.93(00.00)         |
| GitHub Hard   | Guidance    |      0.01 |       0.73 |       35.88 |     10.25 | 211.40(101.40)       |
| GitHub Hard   | XGrammar    |      0.3  |       0.65 |       65.2  |     14.99 | 221.40(00.00)        |
