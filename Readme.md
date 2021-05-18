# StatTyping

With how complicated machine learning codebases are getting now it is upsettingly easy for slight statistical bugs to slip through the cracks.

## What is this?

The purpose of this project is to annotate variables and types which statistical information which we can use to verify our code is doing what we want it to and as a sort of proof checker.

For example lets say we have a simple function that take the mean of a set of values.

If we know that these values are taken from a MVN, using the CLT we can annotate the return type as a sample from a MVN with with the same mean and reduced variance.

The point of this is not to try and retread the great work being done in formal verification in proof assistants such as Issabelle, but to also work from the reverse direction.

We are taking the word of functions about what they do.

While it would be best to have complete bottom up proofs of everything which we are using, we are a bit away from having this ability. The hope would be that this top down approach would be able to meet in the middle with proof assistants at some point in the future and that until then this would be a useful tool.