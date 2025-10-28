* function fitting
    * least squares
    * R^2 / adjusted R^2
    * Next class
       * Connection to likelihoods / bayes theorem

* in-class exercise 2 [in groups of 3]
    * (1) develop a model for the data, each group member should try a 
          different model. The model must contain at least 4 parameters.
    * (2) each person should use one of their minimizers to fit the data
    * (3) test the goodness of fit by calculating the adjusted R^2 [next class]
    * (4) compare the ability of each model in the group to fit to the
          data

* incorporating noise in your model
    * fitted peak value --> distribution of fits
        * Resampling
        * Bootstrapping (e.g. https://en.wikipedia.org/wiki/Bootstrapping_(statistics)
        * Propagation of errors (requires assumption of noise model)
    * Next class
        * Bayes theorem
        * markov chain monte carlo
