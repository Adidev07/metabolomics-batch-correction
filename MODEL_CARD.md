# Model / system card

## Intended use

Estimate technical batch offsets while retaining a fictional biological condition effect. Educational local experiment; no production deployment is implied.

## Data

Synthetic arrays, manually written documents or replayed JSON. No real user records. Seeds and sample inputs are recorded in app.py and sample_input.json.

## Method

Fit each feature against intercept, condition and batch indicators on training samples. Subtract only fitted batch offsets. Preserve the condition component rather than centering entire groups indiscriminately.

## Evaluation protocol

Use held-out samples from known batches and compare estimated technical-effect removal with naive centering. Hidden clean profiles are available only because the data is synthetic.

## Known limits

Condition labels are used for fitting training batch effects; test condition labels are not used by correction. New unseen batches and confounded batch-condition designs need separate treatment.

## Verification status

Local tests and default experiment are executed during packaging. Live model generation is not exercised in the build. A successful validation result is limited to the checks implemented in code.

## Further work

Check design identifiability, evaluate biological signal preservation, include pooled controls and compare established methods on a licensed metabolomics dataset.
