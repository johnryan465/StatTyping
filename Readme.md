# StatTyping

With how complicated machine learning codebases are getting now it is upsettingly easy for slight statistical bugs to slip through the cracks.

## What is this?

The purpose of this project is to annotate variables and types which statistical information which we can use to verify our code is doing what we want it to and as a sort of proof checker.

For example lets say we have a simple function that take the mean of a set of values.

If we know that these values are taken from a MVN, using the CLT we can annotate the return type as a sample from a MVN with with the same mean and reduced variance.

