## C Theoretical Coverage Details

Definition C.1 (Theoretical Coverage) A schema is considered theoretically covered if all of its features are supported by the grammar engine.

The theoretical coverage , noted as C Theoretical, measures the proportion of JSON schemas that a grammar engine supports based on its implementation. It doesn't involve any model inference or experiments and is solely based on the grammar engine's implementation. C Theoretical is an upper bound of the true coverage , which cannot be empirically measured due to the infinite number of possible generations under the schema constraints.

Overall, the theoretical coverage provides a good indication of the grammar engine's capability to support a wide range of schema constraints.

In our experiment, the theoretical coverage for each framework was determined based on the documentation and resources listed in Table 11.

Table 11: Grammar Engine Documentation and Resources

| Frameworks   | Lib Version   | Release Date   | JSON Schema Support Documentation        |
|--------------|---------------|----------------|------------------------------------------|
| Guidance     | 0.2.0rc       | 2024.11.26     | LLGuidance Documentation                 |
| Llamacpp     | 0.3.2         | 2024.11.16     | llama.cpp JSON Schema to gbnf Conversion |
| XGrammar     | 0.1.6         | 2024.12.07     | XGrammar JSON Schema to gbnf Conversion  |
| Outlines     | 0.1.8         | 2024.12.06     | Outlines JSON Schema to Regex Conversion |
| OpenAI       | UNK           | UNK            | OpenAI Structured Output API             |
| Gemini       | 0.8.3         | 2024.10.31     | Gemini Structured Output Content Types   |

Feature required

items additionalProperties

enum

$ref pattern

format oneOf

@minmaxLength

@siblingKeys

@minmaxinteger

@minmaxltems additionalProperties:object

anyof patternProperties

allOf not

@minmaxProperties additionalltems

const dependencies

multipleOf

@minmaxNumber uniqueltems

if propertyNames

contains unevaluatedProperties

@recursiveSchemas

Schemas supported

Schemas

7473

4703

4290

3898

Gemini

V

V

Figure 4: Feature checklist for different structured output engines

<!-- image -->

The theoretical support for each feature in JSON Schema is summarized in Figure 4

Table 12: Theoretical coverage across datasets.

| Dataset         |   LM only |   Guidance |   Llamacpp |   Outlines | XGrammar   |   OpenAI | Gemini   |
|-----------------|-----------|------------|------------|------------|------------|----------|----------|
| GlaiveAI        |         0 |       0.96 |       0.95 |       0.95 | 0.87       |     0.87 | 0.87     |
| GitHub Easy     |         0 |       0.87 |       0.83 |       0.75 | 0.65       |     0.31 | 0.31     |
| Snowplow        |         0 |       0.8  |       0.74 |       0.58 | NA         |     0.29 | NA       |
| GitHub Medium   |         0 |       0.73 |       0.69 |       0.57 | 0.49       |     0.22 | NA       |
| Kubernetes      |         0 |       0.58 |       0.58 |       0.58 | 0.58       |     0.4  | NA       |
| Washington Post |         0 |       0.7  |       0.64 |       0.63 | 0.62       |     0.29 | NA       |
| GitHub Hard     |         0 |       0.54 |       0.49 |       0.38 | 0.33       |     0    | NA       |
| JsonSchemaStore |         0 |       0.31 |       0.24 |       0.2  | 0.13       |     0    | NA       |

The theoretical coverage of each grammar engine is summarized in Table 12.

LLGuidance llama.cpp

Outlines

Grammar

OpenAl

All possible outputs

Over-
