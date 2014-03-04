#!/bin/sh

wget -P ~ http://polymake.org/lib/exe/fetch.php/download/polymake-2.12-rc3.tar.bz2
tar xf ~/polymake-2.12-rc3.tar.bz2
mkdir -p ~/polymake
cd ~/polymake-2.12
./configure --prefix=~/polymake
make
make install
cd -
sudo ln -s ~/polymake/bin/polymake /usr/local/bin/polymake
