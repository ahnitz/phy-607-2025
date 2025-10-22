* In-class assignment 1
    * Use brute-force, gradient descent, and newton's method, and nelder-mead to
      find the minima of the 2-d rosenbrock function
        * Use the provided script to see how to generate the rosenbrock function
          with scipy use the same explicit ranges as in the script
          (e.g. x is (-2, 2), y is (-1, 3)).
        * Choose how you'll set the step size for gradient descent. How
          can you make it likely to converge to an extrema?
    * Start each method at each of the 4 corners? How many iterations does
      it take for each method to get within 1e-10 of the minimum value (0).
         * Does it get stuck at any other locations?
         * For gradient descent, try different step size scale factors. How
           does this change the convergence?
    * Plot the the path that each iteration traverses through for all
      methods (except brute-force).
        * Compare the paths that each take
       
* function fitting
    * least squares

* in-class exercise 2 [in groups of 3]
    * (1) develop a model for the data, each group member should try a 
          different model
    * (2) each person should use one of thier minimizers to fit the data
    * (3) test the goodness of fit by calculated the adjusted R^2
    * (4) compare the ability of each model in the group to fit to the
          data

* Next class       
    * goodness of fit
        * adjusted R^2
    * incorporating noise in your model
        * fitted peak value --> distribution of fits
        * bayes theorem
            * likelihood functions
        * markov chain monte carlo
