#!/usr/bin/env bash

#-----------------------
# install virtualbox and vagrant
# on ubuntu 12.04x64 (precise)
# prior to bootstrapping the
# virtualmachine with
# $ vagrant up
#-----------------------

#Setting output color to cyan before reset
output() {
      printf '\E[36m'; echo "$@"; printf '\E[0m'
}

output "This script will download and install
    virtualbox: 4.3.8-92456 for ubuntu 12.04x64 (precise)
    vbox-extpack: 4.3.8-92456
    vagrant:    1.4.3 for ubuntu x64
"

sudo apt-get -y install nfs-kernel-server

#---------------------
# download packages:
#   virtualbox: 4.3.8-92456 for ubuntu 12.04x64 (precise)
#   vbox-extpack: 4.3.8-92456
#   vagrant:    1.4.3 for ubuntu x64
#---------------------

mkdir -p ~/Downloads
output "downloading virtualbox: 4.3.8-92456...
"
wget -P ~/Downloads http://download.virtualbox.org/virtualbox/4.3.8/virtualbox-4.3_4.3.8-92456~Ubuntu~precise_amd64.deb

output "downloading vbox-extpack: 4.3.8-92456...
"
wget -P ~/Downloads http://download.virtualbox.org/virtualbox/4.3.8/Oracle_VM_VirtualBox_Extension_Pack-4.3.8-92456.vbox-extpack

output "downloading vagrant: 1.4.3...
"
wget -P ~/Downloads https://dl.bintray.com/mitchellh/vagrant/vagrant_1.4.3_x86_64.deb

#---------------------
# install packages:
#---------------------

output "installing virtualbox: 4.3.8-92456...
"
DEBIAN_FRONTEND=noninteractive sudo dpkg -i ~/Downloads/virtualbox-4.3_4.3.8-92456~Ubuntu~precise_amd64.deb
DEBIAN_FRONTEND=noninteractive sudo dpkg -i ~/Downloads/vagrant_1.4.3_x86_64.deb
sudo apt-get -fy install

output "uninstalling Oracle VM VirtualBox Extension Pack...
"
vboxmanage list extpacks
vboxmanage extpack uninstall "Oracle VM VirtualBox Extension Pack"

output "installing vbox-extpack: 4.3.8-92456...
"
vboxmanage extpack install ~/Downloads/Oracle_VM_VirtualBox_Extension_Pack-4.3.8-92456.vbox-extpack
vboxmanage list extpacks

output "removing installation packages...
"
rm ~/Downloads/virtualbox-4.3_4.3.8-92456~Ubuntu~precise_amd64.deb
rm ~/Downloads/Oracle_VM_VirtualBox_Extension_Pack-4.3.8-92456.vbox-extpack
rm ~/Downloads/vagrant_1.4.3_x86_64.deb

output "Run

    \$ vagrant up

to provision and boot virtual machine.

Then run

    \$ vagrant ssh

to log in.
"
#vagrant up
