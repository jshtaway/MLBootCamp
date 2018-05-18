# Automated Conda setup

Michelle L. Gill  
2016/07/26  
Regularly updated Gist located [here](https://gist.github.com/mlgill/4302c24ad1c8999577fd2f6cd03d8d2b/edit).

This bash script will download and setup a Conda environment on Mac OS X or Linux using a specified Python version (2.7, 3.4, 3.5) and packages. The Conda installation path and environment name can also be specified. All settings are input at the beginning of the script (see below).

If the Conda directory exists and can be determined to be a Conda installation, a new environment will be created. If the directory does not appear to be a Conda installation, the script will quit.

###Running the Script

The script can be downloaded and run from any directory to which you have write access. To run the script, set the variables below. The Conda installation path (`env_path`) can be relative or absolute. Then make the script executable with `chmod +x setup_conda.sh` and run the script from the command line with `./setup_conda.sh`.


```bash
# set environment path--use $HOME, not ~, if you want to use absolute path
env_path="$HOME/miniconda"

# set environment name
# NOTE: there's not an easy way to determine if an existing environment
# has the same name. Conda itself will throw an error during installation
# of second environment.
# env_name="datasci2"
env_name="datasci3"

# set python version: 2.7, 3.6, etc
# python_ver=2.7
python_ver=3.6

# set packages to be installed (do not list python itself)
# be sure to name/spell them exactly as Conda does or installation will fail
packages="psutil numpy scipy matplotlib seaborn pandas statsmodels jupyter ipython notebook nbconvert sqlalchemy psycopg2 beautifulsoup4 html5lib lxml ipykernel requests flask nltk gensim"
```

###Confirming Installation

Once your installation is complete, you will see the following message:
```bash
# To activate this environment, use:
# $ source activate datasci35
#
# To deactivate this environment, use:
# $ source deactivate
#
Finished creating Conda environment.
$
```

###Navigating the Conda Environment

As an example, if the installation directory is:
```
env_path="$HOME/miniconda"
```

You can run the script twice, creating two virtual environments, one for each version of Python:
```bash
$ pwd
/Users/myname/miniconda/envs
$ ls
total 0
drwxr-xr-x  14   476 Jul 31 11:30 datasci27
drwxr-xr-x  15   510 Jul 31 11:47 datasci35
$
```

You can create a directory for your notebooks:
```bash
$ cd /Users/myname/miniconda/envs/datasci35
$ mkdir _my_notebooks
```

You should see the following:  
```bash
$ pwd
/Users/myname/miniconda/envs/datasci35
$ ls
total 8
drwxr-xr-x    2     68 Jul 31 11:47 _my_notebooks
drwxr-xr-x   91   3094 Jul 31 11:32 bin
drwxr-xr-x   70   2380 Jul 31 11:32 conda-meta
drwxr-xr-x    4    136 Jul 31 11:32 imports
drwxr-xr-x   31   1054 Jul 31 11:32 include
drwxr-xr-x  204   6936 Jul 31 11:32 lib
drwxr-xr-x  114   3876 Jul 31 11:32 mkspecs
drwxr-xr-x   12    408 Jul 31 11:32 plugins
drwxr-xr-x    3    102 Jul 31 11:32 python.app
drwxr-xr-x    8    272 Jul 31 11:32 share
drwxr-xr-x    6    204 Jul 31 11:32 ssl
$
```

###Activating virtual environment

`cd` into the appropriate folder to activate this virtual environment:
```
$ cd /Users/reshamashaikh/miniconda/envs
$ source activate datasci35
```

You will see the following prompt (notice the virtual environment name now appears in front of the `$`):
```
(datasci35) $ 
```

Voila!  You can now run the Jupyter notebook.
```
(datasci35) $ jupyter notebook
```

Try the following in the Jupyter notebook:
Notice that the first print will not work because it is Py2, but the second one will.  
```
!python --version
print "hello world"
print("hello world")
```

