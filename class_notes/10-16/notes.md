* monte-carlo integration wrapup
* Python things
    * numpy
        * https://numpy.org/devdocs/user/quickstart.html
    * argument parsing
    * packages/distributions
        * https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
    * requirements.txt files
* optimization [to continue next class]
    * brute force / explicit exploration
    * gradient descent
        * how to calculate a gradient numerically?
            * https://en.wikipedia.org/wiki/Finite_difference_coefficient#Forward_and_backward_finite_difference
        * How to ensure convergence?
    * newtons method
    * failure modes?
        * global vs local
    * transforming to other problems
    * nelder-mead (optional)
* In-class assignment [to continue next class]
    * Use explicit gradient descent and newton's method to
      find the minima of the 2-d rosenbrock function
        * Use the provided script to see how to generate the rosenbrock function
          with scipy use the same explicit ranges as in the script
          (e.g. x is (-2, 2), y is (-1, 3)).
        * Choose how you'll set the step size for gradient descent. How
          can you make it likely to converge to an extrema?
    * Start each method at each of the 4 corners? How many iterations does
      it take for each method to get within 1e-10 of the minimum value (0).
         * Does it get stuck at any other locations?
    * Plot the the path that each iteration traverses through
        * Compare the path that gradient descent vs newton's method takes
