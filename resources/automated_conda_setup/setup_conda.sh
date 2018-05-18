#!/usr/bin/env bash

# Michelle L. Gill
# Updated: 2016/11/16
# https://gist.github.com/mlgill/4302c24ad1c8999577fd2f6cd03d8d2b

################# OVERVIEW #################
# This script will setup and install all Conda packages 
# in a given path with a given python version
# and environment name. If a conda installation already
# exists at this path, then a new environment with 
# the required python version and packages will be created.

################# INSTRUCTIONS #################
# 1. Set the path for the conda environment below.
#    This can be a non-existent path for a new
#    installation or an existent path to simply create
#    a new environment.
# 2. Specify the environment name and python version below.
#    This step can be repeated to create multiple environments
#    with different python versions and names, for example.
# 3. Set the list of packages to be installed for the 
#    given environment.
# 4. Run this script!


################# USER SET VARIABLES #####################

# set environment path
# can use $HOME (for shortcut to your home directory)
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
packages="psutil numpy scipy matplotlib seaborn pandas statsmodels jupyter ipython notebook nbconvert beautifulsoup4 html5lib lxml ipykernel requests flask scikit-learn"

################# USER SET VARIABLES ABOVE THIS LINE #####################

# BASH prompt colors
blue='\033[1;34m'
red='\033[1;31m'
nc='\033[0m'

# get python major version (2 or 3)
python_base_ver=`echo $python_ver | cut -d'.' -f1`

echo -e $blue"Using Python $python_ver."$nc

if [[ -e $env_path ]]; then

    if [[ ! -e $env_path/bin/conda ]]; then

        # the destination directory does not seem to contain a Conda installation
        # don't want to risk overwriting files, so time to bail...

        echo -e $red"There doesn't appear to be a Conda installation at $env_path."$nc
        echo -e $red"Quitting without installing anything."$nc

        exit 0

    fi

elif [[ ! -e $env_path ]]; then

    echo -e $blue"Conda does not seem to be installed at $env_path. Installing now."$nc

    # set Linux/Darwin url
    if [[ `uname` == "Darwin" ]]; then
        echo -e $blue"Detected Mac OS X."$nc
        os_ver="MacOSX"
    else
        echo -e $blue"Detected Linux."$nc
        os_ver="Linux"
    fi

    url="https://repo.continuum.io/miniconda/Miniconda${python_base_ver}-latest-${os_ver}-x86_64.sh"

    # set install script name
    script_name="miniconda.sh"

    # download the installation script
    echo -e $blue"Downloading Conda installation script."$nc

    if [[ -e $script_name ]]; then
        rm $script_name
    fi

    curl -s -o $script_name $url 

    # create temporary conda installation
    echo -e $blue"Creating Conda installation at $env_path."$nc

    if [[ -e $env_path ]]; then
        rm -rf $env_path
    fi

    bash $script_name -b -f -p $env_path >> /dev/null

    rm $script_name

else

    # setup path and create environment
    echo -e $blue"Conda seems to be installed already. Skipping installation."$nc

fi

# Setup the environment

unset PYTHONHOME
unset PYTHONPATH

export PATH=$env_path:$PATH

echo -e $blue"Python environment will be based on version $python_ver"$nc

packages="python=$python_ver $packages"

#$env_path/bin/conda create --quiet -y -n $env_name $packages >> /dev/null
$env_path/bin/conda create -y -n $env_name $packages

if [[ $?==0 ]]; then
    echo -e $blue"Finished creating Conda environment. Any errors directly above regarding psutil or \"command not found\" can probably be ignored."$nc
else
    echo -e $red"There was an error creating the Conda environment."$nc
fi
