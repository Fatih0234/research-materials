## D JSON Schema Test Suite Experiment Details

constrained

Truely Valid

Outputs constrained

Framework

Figure 5: Illustration of over-constrained and under-constrained.

<!-- image -->

We evaluated each constrained decoding framework's performance on the JSON Schema Test Suite using the following criteria: a framework is considered to pass a test case if it permits generating every valid instance in the test case while preventing the generation of every invalid instance. Some test cases consist exclusively of invalid instances, such as those involving unsatisfiable schemas, i.e., schemas for which no valid instances exist. In these cases, engines raising compile-time errors were allowed to pass.

Cleaning We removed the 'format' category of tests, as the current JSON Schema standard mandates that this keyword be ignored entirely by default. The test suite comes bundled with an 'optional' set of tests, including tests for each officially recognized value of the 'format' keyword. We hope to extend this work to include these optional tests in a follow-up.

Furthermore, some tests require external resources in the form of JSON schemas available at a remote URL. We dropped these tests from the analysis, as the constrained decoding libraries discussed in the current work do not fetch these resources by default. After filtering out these tests, we are left with 43 of the original 45 test categories.

Implementation To check whether a given framework accepts or blocks the generation of a particular JSON instance, we tokenize 7 JSON-serialized form of the instance and walk the framework's constraints forward one token at a time, essentially simulating the generation process of an LLM attempting to produce the given token sequence:

- XGrammar directly expose an interface for updating the token mask after inserting a token and checking validity.
- Outlines does not expose a public interface for interacting with the token mask, but outlines-core , which outlines is built on top of, is easily adapted for this purpose.
- Similarly, Guidance does not expose a public interface for interacting with the token mask, but llguidance , which guidance is built on top of, is easily adapted for this purpose.
- Llamacpp does not expose this interface, but it shares a common grammarspecification language with XGrammar. We use llamacpp to generate GGML BNF and check token-sequence validity using xgrammar 's interface.

7 The particular choice of tokenizer is not particularly important, but we use the Llama 3.1 tokenizer for consistency with our other experiments.

Category additionalProperties -

allof - anchor-

anyof- boolean schema

const - contains -

content- default

defs - dependentRequired -

dependentSchemas - dynamicRef -

enum exclusiveMaximum

exclusiveMinimum if-then-else

infinite-loop-detection items

maxContains - maxitems

maxLength maxProperties-

maximum minContains

minitems not -

oneOf pattern

propertyNames - ref-

required type

unevaluateditems - unevaluatedProperties

uniqueltems

Outlines

0.22

0.42

0.00

JSON Schema Test Suite Coverage

Framework

Llamacpp

0.56

0.17

0.00

<!-- image -->

| 0.38 0.25      | 0.50   | 0.50                     | 0.50   | 0.50   |
|----------------|--------|--------------------------|--------|--------|
| 0.50 0.50      |        |                          |        |        |
| 0.33 0.60*     |        |                          |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.67 0.67      |        | - 0.8                    |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.50 0.50      |        |                          |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.00 1.00*     |        | - 0.6                    |        |        |
| 0.10 0.20      |        |                          |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.00           |        |                          |        |        |
| 0.00 0.00 0.00 |        | Fraction of Tests Passed |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.12 0.12      |        |                          |        |        |
| 0.00 0.00      |        | - 0.4                    |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.40* 0.40*    |        |                          |        |        |
| 0.22* 0.22*    |        |                          |        |        |
| 0.45* 0.45*    |        |                          |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.25 0.25      |        | - 0.2                    |        |        |
| 0.17 0.17      |        |                          |        |        |
| 0.00 0.00      |        |                          |        |        |
| 0.34 0.26      |        |                          |        |        |
| 0.40 0.40      |        |                          |        |        |
| 0.55 0.91*     |        |                          |        |        |
| 0.15 0.19      |        |                          |        |        |
| 0.25** 0.20    |        |                          |        |        |
| 0.17 0.17      |        |                          |        |        |
|                |        | - 0.0                    |        |        |

XGrammar

0.22

Guidance

0.67**

0.25

0.75**
