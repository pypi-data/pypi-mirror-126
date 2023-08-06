# Discrust

## _Binary supervised discretization in Rust_

The `discrust` package provides a supervised discretization algorithm. Under the hood it implements a decision tree, using information value to find the optimal splits, and provides several different methods to control the final discretization scheme.

_The package draws heavily from the [ivpy](https://github.com/gravesee/ivpy) package, both in the algorithm and the parameter controls._

### Additional TODOs

[ ] Support for exception values
[ ] Support for missing values in both the dependant and independent variables
