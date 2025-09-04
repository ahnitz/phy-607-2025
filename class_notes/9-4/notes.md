### **Class Outline & Plan**

* Git continued
    * setting up ssh keys
        * [Example instructions](https://happygitwithr.com/ssh-keys)
    * walk through creating repo
    * resolving merge conflicts
        * [Resolving a merge conflict using the command line](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line)

* python ([general python reference and tutorials](https://docs.python.org/3/tutorial/index.html))
    * modules
    * file i/o
    * plotting
    
* Python Style guide
    * [Python PEP8 Guide](https://realpython.com/python-pep8/)
    * [automatic code formatting (black)](https://black.readthedocs.io/en/stable/)


## In-class Assignment: Falling Cow Simulator

A *spherical cow* with a mass of 1000 kg has fallen off a cliff (or was it pushed?). Simulate its motion under gravity and wind resistance for arbitrary initial conditions and air viscosity.

1.  Write a single program which calls several **sub-functions**. At the top of the program, you should set initial conditions. Make no assumptions about the value of the initial conditions (except that their values are numbers of the appropriate type).
2.  The program should start at `time=0` and progress in fixed time steps until the cow reaches the ground. Use a coordinate system where the ground is at a height of 0. You should assume a two-dimensional Universe (e.g. with an x and y position).
3.  The following functions should be written and then used by the top-level program:
    1.  A function that takes in the cow’s current position and velocity vector and returns the **total force vector**. Assume only gravity (near the earth’s surface) and wind resistance act on the cow. You may assume the magnitude of the wind resistance takes the form `constant * v^2`, where the constant should be selectable. Assume the gravitational acceleration is 9.8 m/s/s and that all units are SI.
    2.  A function which takes the cow’s current position, velocity, and the acting force, and returns a **new position and velocity** some *small* time later. The time step size should also be an input to the function.
    3.  A function to calculate the **potential, kinetic, and total energy** at a given instance.
4.  Create a single **repository for your group’s code on GitHub** and give everyone in the group write access.
    1.  Each person should clone this repository and make changes/commits locally first. Then their changes should be pushed to the remote repository on GitHub.
        1.  Make sure to resolve any merge conflicts before you push.
5.  Form groups of 2-3. Agree on how to divide the work and define the interfaces / API of each function. Start by writing the **english-language pseudocode** before beginning implementation. This must be recorded in a document included in the git repo.
6.  **Plot** the position, velocity, or energy as a function of time.
    1.  *hint: use matplotlib*
7.  Use your code to answer the following questions:
    1.  Is energy conserved as a function of time? To what level of precision?
    2.  How does the trajectory change if you change the time step? What about as you make the time step approach zero?
    3.  How does your trajectory compare to the analytic solution if you set air resistance to zero?

---

### **Useful Git Commands**

* `git clone REPO_URL` - creates a new repository initialized from the repository at the URL.
* `git add FILE_NAME` - adds a file to the staging area (preparing for a commit).
* `git log` - shows the list of commits.
* `git commit` - commits the staged files to the repository.
* `git fetch ORIGIN_NAME` - retrieves any changes from the remote location so that you can work with them locally.
* `git rebase ORIGIN_NAME/branch_name` - applies your local commits on top of the target version.
    * *Git can automatically handle changes in different parts of the same file; however, if a common part is changed, it may require you to manually resolve the conflict.*

