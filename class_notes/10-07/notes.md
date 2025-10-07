* Project 2 proposals due today, I will return comments on these by thursday morning.

* [Useful discussion of monte-carlo integration](https://people.duke.edu/~ccc14/sta-663/MonteCarlo.html#monte-carlo-integration)

* [To be done today and Thursday]
   * Do these in groups of 2-3. If you group gets stuck
     please discuss with other groups.
   * (1) implement inverse CDF and rejection sampling with a simple exponential function defined on the range from 0 to 1.
         * try with a uniform distribution
         * check that with both methods the resulting samples have\
           the correct distribution.
   * (2) Monte-carlo integration: Ellipses
         * Determine how you will estimate the uncertainty of the integral\
           for a chosen size N. Consider that if you estimate the integral\
           multiple times and use independent random numbers in each instance,\
           each estimate will itself be unbiased. Estimate the uncertainties\
           by looking at the distribution independent integral estimates.
         * Consider where the ellipse parameters are a=5, b=2
         * Calculating the area of the ellipse. Compare to the analytic\
           answer. Verify that the uncertainty in this estimates scales\
           with N^(1/2). 
         * Calculating the circumference of the ellipse.
         * How does the uncertainty scale with the number of samples?\
           Plot the statistical uncertainty as a function of the number of\
           samples.
         * What can you do to improve the overall efficiency (but not\
           the scaling with N samples) of the calculation? Compare a\
           naive (say uniform over the space) proposal distribution\
           to one you design to improve the variance of the estimates.
            
* Timing
   * Use %timit in the python intepretor
   * Time your script or algorithm that demonstrates your high-precision type
* profiling
   * https://docs.python.org/3/library/profile.html#module-cProfile
