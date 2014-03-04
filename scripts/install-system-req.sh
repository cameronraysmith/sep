#!/usr/bin/env bash

# posix compliant sanity check
if [ -z $BASH ] || [  $BASH = "/bin/sh" ]; then
    echo "Please use the bash interpreter to run this script"
    exit 1
fi

error() {
      printf '\E[31m'; echo "$@"; printf '\E[0m'
}
output() {
      printf '\E[36m'; echo "$@"; printf '\E[0m'
}


### START

SELF_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REQUIREMENTS_DIR="$SELF_DIR/../requirements/system"
BREW_FILE=$REQUIREMENTS_DIR/"mac_os_x/brew-formulas.txt"
APT_REPOS_FILE=$REQUIREMENTS_DIR/"ubuntu/apt-repos.txt"
APT_PKGS_FILE=$REQUIREMENTS_DIR/"ubuntu/apt-packages.txt"

case `uname -s` in
    [Ll]inux)
        command -v lsb_release &>/dev/null || {
            error "Please install lsb-release."
            exit 1
        }

        distro=`lsb_release -cs`
        case $distro in
            #Tries to install the same
            squeeze|wheezy|jessie|maya|lisa|olivia|nadia|natty|oneiric|precise|quantal|raring)
                output "Installing Debian family requirements"

                # add repositories
                cat $APT_REPOS_FILE | xargs -n 1 sudo add-apt-repository -y
                sudo apt-get -yq update
                sudo DEBIAN_FRONTEND=noninteractive apt-get -yq install gfortran graphviz \
                            libgraphviz-dev graphviz-dev libatlas-dev libblas-dev
                # install packages listed in APT_PKGS_FILE
                cat $APT_PKGS_FILE | xargs sudo DEBIAN_FRONTEND=noninteractive apt-get -yq install
                ;;
            *)
                error "Unsupported distribution - $distro"
                exit 1
               ;;
        esac
        ;;
esac
