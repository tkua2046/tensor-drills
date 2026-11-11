# Inline validation rubric

## Ground truth

1. **Training mode is set only before the loop.** Validation switches the model to evaluation mode and the next batch inherits that mode. Each training forward should use the model's training behavior, even after validation.
2. **Gradients carry over between training batches.** The starter never clears the gradients before backpropagation, so later optimizer steps also use gradients from earlier batches. Each update should use only the current batch's gradients.

## Assessment

- For the mode transition, use `validation between two updates`. Check that training and inference modes alternate across the forwards, with gradients disabled during validation. Ask what changes during validation and how the next batch restores training behavior.
- For gradient carryover, use `validation over three batches`. It disables dropout and checks the expected parameters after every optimizer step. Look for an explanation of how the repair gives each step only its batch's gradients.
- Check that each returned validation logit tensor corresponds to the parameters after its update and that the results are in batch order. Accept the fixed check output or equivalent evidence from an interleaved run. [Fixed cases](tests.json)
