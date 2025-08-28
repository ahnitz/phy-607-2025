# Bash Scripting Assignment: Automate a Task

Write a short script in bash to automate a task. Either implement the following or come up with your own.

Everyone should carefully read through the set of basic linux commands (https://www.geeksforgeeks.org/linux-unix/basic-linux-commands/). However, you may need to use commands not in the list so be prepared to discover additional commands. 


---

## Option 1: Create Your Own

If you come up with your own, it should include at least a few commands, control statements, and make use of either arguments or options passed to the script.

---

## Option 2: Tar Backup Script

Write a shell script to make `tar` backups of one directory into another.

1.  For your development, create directories `backups` and `src` as sub-directories of some empty working directory. As all operations should be relative to this working directory, the path of the working directory is not relevant.

2.  Populate the sub-directory `src` with at least 5 files for testing purposes. The actual content or names of the files is not important, but your shell script should not depend upon knowing the file names.

3.  Create a shell script `do_full_backup` in the working directory.
    1.  When the command `./do_full_backup` is executed from the working directory, the shell script should create a `tar` file in the `backups` sub-directory with a name that includes the time/date to at least second precision.
    2.  It should also create the `backups` directory if it does not exist.
    3.  Additionally, the script should remove all but the most recent 3 backup files.
    4.  The `tar` file should be formatted such that extracting files from it while in the working directory will restore the `src` directory.

---

### Hint

There are many solutions using common commands. One of them makes use of pipes and includes the use of the commands `date` and `xargs`.
