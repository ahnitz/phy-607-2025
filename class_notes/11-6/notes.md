* Project 3 intro
* Comparison of models
* MCMC
    * metropolis hastings
    * burn-in
    * autocorrelation
    * convergence
        * Gelman-Rubin statistic
    * ensemble sampling
* in-class work, work in groups of 2-3 [If not finished, already]
    * Write a likelihood assuming the data contains your model plus additive
      Gaussian (unit variance) noise.
    * write a 500 walker ensemble MCMC and run for 1000 iterations
    * Plot the distribution of the walker positons after every 100 iterations.
      How does the distribution evolve?
      Has the distribution converged?
* in-class, examining correlations and convergence
    * Install the packages in requirements.txt
    * Use the 'corner' package to make a plot for the MCMC chains from your model.
    * Examine 'corre.py' in the class folder for today. This demonstrates
      how to calculate the autocorrelation time for an mcmc chain. Note that
      the ACT/ACL only applies to a specific parameter of a chain, and a 
      different value may be associated with every parameter. 
    * Verify that you recover a reasonable ACL when you change the noise
      mixing parameter (phi) in the script compared to the theoretical 
      prediction. 
    * Examine the autocorrelation function vs chain lag / offset and see
      what happens if you change the a) mixing fraction and b) the number
      of samples in the chain.
    * Apply these methods (both the emcee library method and the direct one)
      to your model for *each parameter* of the walkers independently.
        * With an ensemble sampler, there are several methods to think about the
          ACL. First apply this to a specific walker and then multiple. Compare
          the values you get between walkers. Can you think of a potential
          test for convergence based on this kind of comparison?
    * For your model, examine the chains visually. Do they appear to have 
      converged? You should notice a distinct burn-in period.
    * Considering only period have you've identified the burn-in, calculate
      the ACL. If the ACL is ~ the length of your chain, for the purposes of 
      the following test, assuming it is 1/100 of the chain length. Take
      a sample every ACL length from a single chain. Use this to calculate
      the variance within the chain. Do this for each chain. 
      Separately, take the final sample from each chain and calculate the
      variance of that set. How do these variances compare? Is it consistent
      with the chains having converged?
