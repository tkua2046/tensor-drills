# Flatten logical values and inspect sharing rubric

## Ground truth

Logical traversal is independent of physical storage order. A flattening operation can copy or share depending on the operation and input layout.

## Assessment

Fixed cases assess values and shape, not a preferred ownership choice. Review the submitted mutation probe for the actual chosen operation on a transpose and a regular stepped slice. Do not conclude source sharing merely from a nonempty base attribute. Accept explicit copying with a correct explanation; reject Python element loops under the stated native-operation requirement.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

[Fixed cases](tests.json)
