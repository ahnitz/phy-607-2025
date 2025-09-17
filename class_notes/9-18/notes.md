* numerical precision
    * error example 1
    * error analysis with numerical error (standard error propagation!)
    * error example 2
* python types
* classes
* packages
    * matplotlib / numpy / scipy
* In class exercise
    * implement a spring oscillator
        * Choose your own initial condition (do not choose a case where no evolution occurs)
        * Recall the force equation and substitute into your existing code
    * try the euler explicit, and symplectic forms
    * implement a second order runge kutte algorithm
    * compare the accuracy of all techniques
        * How well is energy conserved over long periods? What the differences
          between the various methods.
* Pending time: In groups of 3-4
    * Plan pseudocode for high precision floating point object
    * should include methods for arithmatic +,-,*,/ and comparisons.
    * Choose any algorithm where you can demonstrate the numerical precision
      is a limiting factor for standard double precision floating point objects
      and compare to your class.
* For next Tuesday
    * Determine what the modified hamiltonian is for the 1d spring oscillator when
      using the Euler symplectic integrator method.
          * Hint, compare the unmodified energy at each time step. What would
            you have to add to get a conserved form?
