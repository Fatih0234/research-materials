## B Coverage Experiment Details

The prompting template used for the coverage experiment is shown in Figure 3.

6000

7000

date-time

29%

uri other

17%

2%

3%

topic path

uuid

- Schema Extraction: Extracted schemas embedded within non-root levels of JSON files. 17% 7%

8%

int32

8%

date email

2%

Figure 3: Prompt template used to generate JSON objects in the coverage experiment.

<!-- image -->

Decoding Method We use greedy decoding with no top P or top K sampling for all the experiments. We only get one output from the model, which we will use to validate the schema compliance. It's totally plausible to sample more outputs and validate them all, and it might detect more schema violations. The fact that we only sample the top 1 output may quantify our empirical coverage as Top 1 Empirical Coverage .

Validation We use the jsonschema library with the Draft-2020-12 version of the JSON Schema standard to validate the generated JSON object. We turn on the 'format' checks, which are not enabled by default in Python. Strictly speaking, the jsonschema library doesn't guarantee the validation of all the schema constraints, even with the 'format' checks enabled. It is possible, though very rare, for a schema-noncompliant output to be validated as compliant by the jsonschema library, leading to a slight overestimation of empirical coverage. However, such occurrences are corner cases and happen infrequently.
