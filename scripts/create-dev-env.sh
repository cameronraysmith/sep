#!/usr/bin/env bash

#Exit if any commands return a non-zero status
set -e

# posix compliant sanity check
if [ -z $BASH ] || [  $BASH = "/bin/sh" ]; then
    echo "Please use the bash interpreter to run this script"
    exit 1
fi

trap "ouch" ERR

ouch() {
    printf '\E[31m'

    cat<<EOL

    !! ERROR !!

    The last command did not complete successfully,
    For more details or trying running the
    script again with the -v flag.

    Output of the script is recorded in $LOG

EOL
    printf '\E[0m'

}

#Setting error color to red before reset
error() {
      printf '\E[31m'; echo "$@"; printf '\E[0m'
}

#Setting warning color to magenta before reset
warning() {
      printf '\E[35m'; echo "$@"; printf '\E[0m'
}

#Setting output color to cyan before reset
output() {
      printf '\E[36m'; echo "$@"; printf '\E[0m'
}

usage() {
    cat<<EO

    Usage: $PROG [-c] [-v] [-h]

            -y        non interactive mode (no prompt, proceed immediately)
            -c        compile scipy and numpy
            -n        do not attempt to pull sep repository
            -s        give access to global site-packages for virtualenv
            -q        be more quiet (removes info at beginning & end)
            -v        set -x + spew
            -p        compile polymake
            -h        this

EO
    info
}

info() {
    cat<<EO
    base dir : $BASE
    Python virtualenv dir : $PYTHON_DIR

EO
}

change_git_push_defaults() {

    #Set git push defaults to upstream rather than master
    output "Changing git defaults"
    git config --global push.default upstream

}

clone_repos() {

    cd "$BASE"

    if [[ ! $nopull ]]; then
        change_git_push_defaults

        if [[ -d "$BASE/sep/.git" ]]; then
            output "Pulling sep"
            cd "$BASE/sep"
            git pull
        else
            output "Cloning sep"
            if [[ -d "$BASE/sep" ]]; then
                output "Creating backup for existing sep"
                mv "$BASE/sep" "${BASE}/sep.bak.$$"
            fi
            git clone https://github.com/cameronraysmith/sep.git
        fi
    fi
}

set_base_default() {  # if PROJECT_HOME not set
    # 2 possibilities: this is from cloned repo, or not

    # See if remote's url is named sep (this works for forks too, but
    # not if the name was changed).
    cd "$( dirname "${BASH_SOURCE[0]}" )"
    this_repo=$(basename $(git ls-remote --get-url 2>/dev/null) 2>/dev/null) ||
        echo -n ""

    if [[ "x$this_repo" = "xsep.git" ]]; then
        # We are in the sep repo and already have git installed. Let git do the
        # work of finding base dir:
        echo "$(dirname $(git rev-parse --show-toplevel))"
    else
        echo "$HOME/sep"
    fi
}


### START

PROG=${0##*/}

# Adjust this to wherever you'd like to place the codebase
BASE="${PROJECT_HOME:-$(set_base_default)}"

# Use a sensible default (~/.virtualenvs) for your Python virtualenvs
# unless you've already got one set up with virtualenvwrapper.
PYTHON_DIR=${WORKON_HOME:-"$HOME/.virtualenvs"}

LOG="/var/tmp/install-$(date +%Y%m%d-%H%M%S).log"

# Make sure the user's not about to do anything dumb
if [[ $EUID -eq 0 ]]; then
    error "This script should not be run using sudo or as the root user"
    usage
    exit 1
fi

# If in an existing virtualenv, bail
if [[ "x$VIRTUAL_ENV" != "x" ]]; then
    envname=`basename $VIRTUAL_ENV`
    error "Looks like you're already in the \"$envname\" virtual env."
    error "Run \`deactivate\` and then re-run this script."
    usage
    exit 1
fi

# Read arguments
ARGS=$(getopt "cvhsynq" "$*")
if [[ $? != 0 ]]; then
    usage
    exit 1
fi
eval set -- "$ARGS"
while true; do
    case $1 in
        -c)
            compile=true
            shift
            ;;
        -s)
            systempkgs=true
            shift
            ;;
        -v)
            set -x
            verbose=true
            shift
            ;;
        -y)
            noninteractive=true
            shift
            ;;
        -q)
            quiet=true
            shift
            ;;
        -n)
            nopull=true
            shift
            ;;
        # -p)
        #     polymake=true
        #     shift
        #     ;;
        -h)
            usage
            exit 0
            ;;
        --)
            shift
            break
            ;;
    esac
done

if [[ ! $quiet ]]; then
    cat<<EO

  This script will setup a local sep environment, this
  includes

       * Django
       * A local copy of Python and library dependencies
       * A local copy of Ruby and library dependencies

  It will also attempt to install operating system dependencies
  with apt(debian) or brew(OSx).

  To compile scipy and numpy from source use the -c option

  !!! Do not run this script from an existing virtualenv !!!

  If you are in a ruby/python virtualenv please start a new
  shell.

EO
fi
    info

if [[ ! $noninteractive ]]; then
    output "Press return to begin or control-C to abort"
    read dummy
fi

# Log all stdout and stderr

exec > >(tee $LOG)
exec 2>&1


# Install basic system requirements

mkdir -p $BASE
case `uname -s` in
    [Ll]inux)
        command -v lsb_release &>/dev/null || {
            error "Please install lsb-release."
            exit 1
        }

        distro=`lsb_release -cs`
        case $distro in
            wheezy|jessie|maya|olivia|nadia|precise|quantal)
                if [[ ! $noninteractive ]]; then
                    warning "
                            Debian support is not fully debugged. Assuming you have standard
                            development packages already working like scipy, the
                            installation should go fine, but this is still a work in progress.

                            Please report issues you have and let us know if you are able to figure
                            out any workarounds or solutions

                            Press return to continue or control-C to abort"

                    read dummy
                fi
                sudo apt-get install -yq git ;;
            squeeze|lisa|katya|oneiric|natty|raring)
                if [[ ! $noninteractive ]]; then
                    warning "
                              It seems like you're using $distro which has been deprecated.
                              While we don't technically support this release, the install
                              script will probably still work.

                              Press return to continue or control-C to abort"
                    read dummy
                fi
                sudo apt-get install -yq git
                ;;

            *)
                error "Unsupported distribution - $distro"
                exit 1
               ;;
        esac
        ;;
esac


# Clone sep repositories

clone_repos

# Sanity check to make sure the repo layout hasn't changed
if [[ -d $BASE/scripts ]]; then
    output "Installing system-level dependencies"
    bash $BASE/scripts/install-system-req.sh
else
    error "It appears that our directory structure has changed and somebody failed to update this script.
            raise an issue on Github and someone should fix it."
    exit 1
fi

# Install Python virtualenv
output "Installing python virtualenv"

# virtualenvwrapper uses the $WORKON_HOME env var to determine where to place
# virtualenv directories. Make sure it matches the selected $PYTHON_DIR.
export WORKON_HOME=$PYTHON_DIR

# Load in the mkvirtualenv function if needed
if [[ `type -t mkvirtualenv` != "function" ]]; then
    case `uname -s` in

        [Ll]inux)
        if [[ -f "/etc/bash_completion.d/virtualenvwrapper" ]]; then
            source /etc/bash_completion.d/virtualenvwrapper
        else
            error "Could not find virtualenvwrapper"
            exit 1
        fi
        ;;
    esac
fi

# Create sep virtualenv and link it to repo
# virtualenvwrapper automatically sources the activation script
if [[ $systempkgs ]]; then
    mkvirtualenv -q -a "$WORKON_HOME" --system-site-packages sep || {
      error "mkvirtualenv exited with a non-zero error"
      return 1
    }
else
    # default behavior for virtualenv>1.7 is
    # --no-site-packages
    mkvirtualenv -q -a "$WORKON_HOME" sep || {
      error "mkvirtualenv exited with a non-zero error"
      return 1
    }
fi


# compile numpy and scipy if requested

NUMPY_VER="1.6.2"
SCIPY_VER="0.10.1"

if [[ -n $compile ]]; then
    output "Downloading numpy and scipy"
    curl -sSL -o numpy.tar.gz http://downloads.sourceforge.net/project/numpy/NumPy/${NUMPY_VER}/numpy-${NUMPY_VER}.tar.gz
    curl -sSL -o scipy.tar.gz http://downloads.sourceforge.net/project/scipy/scipy/${SCIPY_VER}/scipy-${SCIPY_VER}.tar.gz
    tar xf numpy.tar.gz
    tar xf scipy.tar.gz
    rm -f numpy.tar.gz scipy.tar.gz
    output "Compiling numpy"
    cd "$BASE/numpy-${NUMPY_VER}"
    python setup.py install
    output "Compiling scipy"
    cd "$BASE/scipy-${SCIPY_VER}"
    python setup.py install
    cd "$BASE"
    rm -rf numpy-${NUMPY_VER} scipy-${SCIPY_VER}
fi

output "Installing sep Python requirements"
pip install -r $BASE/requirements/sep/devset.eggs
#pip install matplotlib
pip install git+https://github.com/ezod/hypergraph.git

# Configure Git

output "Fixing your git default settings"
git config --global push.default current


# Install polymake
# this takes a long time
# eventually create ppa

# if [[ -n $polymake ]]; then
wget -P ~ http://polymake.org/lib/exe/fetch.php/download/polymake-2.12-rc3.tar.bz2
tar xf ~/polymake-2.12-rc3.tar.bz2 -C ~
mkdir -p ~/polymake
cd ~/polymake-2.12
./configure --prefix=~/polymake
make
make install
cd -
sudo ln -s ~/polymake/bin/polymake /usr/local/bin/polymake
# fi

### DONE

if [[ ! $quiet ]]; then
    cat<<END
   Success!!

END
fi

exit 0
