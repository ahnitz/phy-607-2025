* project 1 discussion
* how can you find resources on programming?
    * documentation of libraries
    * `google` / `stackoverflow`
* python environments
    * `venv` / `conda`
    * See e.g. [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install)
* packages
    * `matplotlib` / `numpy` / `scipy`
* Style guide
    * `pep 8` styles
        * https://peps.python.org/pep-0008/
    * automatic formatters
        * `black`
* numerical precision
    * error example 1
    * error analysis with numerical error (standard error propagation!)
    * error example 2
* semi-implicit / symplectic euler integral
* In class exercise
    * implement a spring oscillator
        * Choose your own initial condition (do not choose a case where no evolution occurs)
        * Recall the force equation and substitute into your existing code
    * try the euler explicit, and symplectic forms
    * implement a second order runge kutte algorithm
    * compare the accuracy of all techniques
        * How well is energy conserved over long periods? What the differences
          between the various methods.
* Out of class review
    * [Python Numerical Methods](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html)
    * Review chapter 21 / 22
