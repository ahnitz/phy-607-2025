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


**Assignment Title:** (Thursday) N-Body Simulation of Particle Interactions in a Fluid to Model Drag

**Objective:** The aim of this project is to create a primitive n-body simulation to model the interactions between a projectile and particles in a fluid.

**Split into 2 groups

1. **Joint Discussion and Pseudocode Planning (30 minutes):**
    - Understand the basic principles of n-body simulations and how they can be used to model fluid dynamics and drag forces.
    - Decide on the simulation parameters, including the number of fluid particles, mass of the projectile, and initial conditions.
    - Draft pseudocode for the simulation, focusing on the interaction between the projectile and fluid particles, how the code can be modularized, and what
    the function interfaces should be.

2. **Division ofWork:**
    - **High-Level Analysis Script Writer (1 person):**
        - Develops the main control script that initializes the system, runs the simulation loop, and collects data for analysis.
    - **Post-Processing/Plotting Script Writer (1 person):**
        - Creates scripts for visualizing the trajectory of the projectile and the fluid particles, plotting the velocity and drag force over time.
    - **Module Developer(s) (1-2 people):**
        - Writes the core module(s) for calculating forces between particles, updating positions and velocities, and handling boundary conditions.
    - **Unit Test Developer (1 person):**
        - Designs and implements unittests to verify the accuracy and stability of the force calculations and the integration scheme.
        
 3. Each group will submit a summary of the days activity and plan at the end of class on Thursday. 
