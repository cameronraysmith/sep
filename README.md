A copy of this repository can be downloaded following installation of [git][git] by running:
```
/ $ git pull git@github.com:cameronraysmith/sep.git
```
Use of the virtual machine requires [VirtualBox][vbox] (including the extension pack) and [Vagrant][vagrant]. These prerequisites can be installed in Ubuntu 12.04 by running the script `bootstraplocal.sh`. The virtual machine can then be provisioned and booted by running `vagrant up` in the root directory of this repository.
```
/sep [master] $ ./bootstraplocal.sh && vagrant up
```

[git]: http://git-scm.com/downloads
[vbox]: https://www.virtualbox.org/wiki/Downloads
[vagrant]: http://www.vagrantup.com/downloads.html

<!-- 1. See PLOS Computational Biology [LaTeX submission guidelines][1]
1. A [short math guide][2] from AMS.

[1]: http://www.ploscompbiol.org/static/latexGuidelines
[2]: ftp://ftp.ams.org/pub/tex/doc/amsmath/short-math-guide.pdf
 -->
