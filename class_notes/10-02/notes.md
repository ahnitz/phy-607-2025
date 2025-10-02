* Project 1 discussion
* Project 2 proposals due Next Tuesday, I will return comments on these by
    * thursday morning.
* Next Tuesday: Work on the inclass monte-carlo exercises. The final plots / code will be collected.
* Next Thursday: Work in your groups on Project 2. A summary of progress in class will be collected.
* Variance reduction in monte-carlo methods / sampling
    * An example with rejection sampling
    * Importance sampling
* Timing
   * Use %timit in the python intepretor
   * Time your script or algorithm that demonstrates your high-precision type
* profiling
   * https://docs.python.org/3/library/profile.html#module-cProfile
* numpy arrays

* [in-class group work]
    Implement sorting algorithm that works with your extended precision class.
    * Implement both a bubble sort and a merger sort
    * Plot the time it takes to sort a list for both algorithms as a function of list length.
    * Profile your code and identify the key bottlenecks.

* [To be done next Tuesday]
   * try inverse CDF and rejection sampling with exponential function 
     * try with a uniform distribution
   * Monte-carlo integration
     * Ellipses
     * Do this in groups of two. First discuss how you'll go about this calculation
       and put together the pseudo code.
        * Consider two cases, where the ellipse parameters are a=5, b=2
            * Calculating the areas of an ellipse. Compare to the analytic
              answer.
            * Calculating the circumference of an ellipse.
                * How do you estimate the uncertainty in this calculation?
                * How does the uncertainty scale with the number of samples?
                  Plot the statistical uncertainty as a function of the number of
                  samples.
                * What can you do to improve the overall efficiency (but not
                  the scaling with N samples) of the calculation? Compare a 
                  naive proposal distribution to one you design to improve
                  the variance of the estimates.
            

