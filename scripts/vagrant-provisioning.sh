#!/bin/bash -e

###############################################################################

# vagrant-provisioning.sh:
#
# Script to setup base environment on Vagrant, based on `precise64` image
# Runs ./scripts/create-dev-env.sh for the actual setup
#
# This script is run by `$ vagrant up`, see the README for further detail

on_create()
{
    # APT - Packages ##############################################################

    apt-get update
    apt-get install -y python-software-properties vim


    # Curl - No progress bar ######################################################

    [[ -f ~vagrant/.curlrc ]] || echo "silent show-error" > ~vagrant/.curlrc
    chown vagrant.vagrant ~vagrant/.curlrc


    # # SSH - Known hosts ###########################################################

    # # sep - Development environment ###############################################

    mkdir -p /opt/sep
    sudo -u vagrant -i bash -c "cd /opt/sep && PROJECT_HOME=/opt/sep ./scripts/create-dev-env.sh -ysnqp"

    # # Load .bashrc ################################################################
    ([[ -f ~vagrant/.bash_profile ]] && grep ".bashrc" ~vagrant/.bash_profile) || {
        echo ". /home/vagrant/.bashrc" >> ~vagrant/.bash_profile
    }

    # # Virtualenv - Always load ####################################################

    ([[ -f ~vagrant/.bash_profile ]] && grep "sep/bin/activate" ~vagrant/.bash_profile) || {
        echo ". /home/vagrant/.virtualenvs/sep/bin/activate" >> ~vagrant/.bash_profile
    }

    # # Directory ###################################################################

    grep "cd /opt/sep" ~vagrant/.bash_profile || {
        echo "cd /opt/sep" >> ~vagrant/.bash_profile
    }

    # Permissions
    chown vagrant.vagrant ~vagrant/.bash_profile

    cat << EOF
==============================================================================
Success - Created your development environment!
==============================================================================

EOF
}    # End on_create() ########################################################

## only initialize / setup the development environment once:
#   we create the sep virtual environment, so that's a good test:
[[ -d $HOME/.virtualenvs/sep ]] || on_create
#on_create

# grab what the Vagrantfile spec'd our IP to be:
#  expecting:
#  - relevant ip on eth1;
#  - line of interest to look like:
#    inet 192.168.20.40/24 brd 192.168.20.255 scope global eth1
MY_IP=$(ip addr show dev eth1 | sed -n '/inet /{s/.*[ ]\(.*\)\/.*/\1/;p}')

cat << EOF
Connect to your virtual machine with "vagrant ssh".
Some examples you can use from your virtual machine:

See the README for more.

EOF
