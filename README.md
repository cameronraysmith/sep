A copy of this repository can be downloaded following installation of [git][git] by running:
```
~/$ git clone git@github.com:cameronraysmith/sep.git
~/$ cd sep
~/sep [master] $
```
### Ubuntu
Use of the virtual machine requires [VirtualBox][vbox] (including the extension pack) and [Vagrant][vagrant]. These prerequisites can be installed in Ubuntu 12.04 by running the script `bootstraplocal.sh`. The virtual machine can then be provisioned and booted by running `vagrant up` in the root directory of this repository.
```
~/sep [master] $ ./bootstraplocal.sh && vagrant up
```
...this will take some time (about 30 minutes) and 3GB of hard drive space...
```
~/sep [master] $ vagrant ssh
(sep)vagrant@precise64:/opt/sep$ cd code/python/
(sep)vagrant@precise64:/opt/sep/code/python$ python runfourgraphs.py
```

### Mac OSX

Use of the virtual machine requires [VirtualBox][vbox] (including the extension pack) and [Vagrant][vagrant]. These prerequisites can be installed manually from the links given above. The virtual machine can then be provisioned and booted by running `vagrant up` in the root directory of this repository.
```
~/sep [master] $ vagrant up
```
...this will take some time (about 30 minutes) and 3GB of hard drive space...
```
~/sep [master] $ vagrant ssh
(sep)vagrant@precise64:/opt/sep$ cd code/python/
(sep)vagrant@precise64:/opt/sep/code/python$ python runfourgraphs.py
```

### Windows

Use of the virtual machine requires [VirtualBox][vbox] (including the extension pack) and [Vagrant][vagrant]. These prerequisites can be installed manually from the links given above. The virtual machine can then be provisioned and booted by running `vagrant up` in the root directory of this repository.
```
C:\sep [master] $ vagrant up
```
...this will take some time (about 30 minutes) and 3GB of hard drive space...
```
C:\sep [master] $ vagrant ssh
(sep)vagrant@precise64:/opt/sep$ cd code/python/
(sep)vagrant@precise64:/opt/sep/code/python$ python runfourgraphs.py
```


[git]: http://git-scm.com/downloads
[vbox]: https://www.virtualbox.org/wiki/Downloads
[vagrant]: http://www.vagrantup.com/downloads.html

<!-- 1. See PLOS Computational Biology [LaTeX submission guidelines][1]
1. A [short math guide][2] from AMS.

[1]: http://www.ploscompbiol.org/static/latexGuidelines
[2]: ftp://ftp.ams.org/pub/tex/doc/amsmath/short-math-guide.pdf
 -->
