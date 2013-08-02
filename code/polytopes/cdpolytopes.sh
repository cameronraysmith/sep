#!/bin/sh

#polymake --script cdpolytopes.pl > cdpolytopes.txt

polymake --script ncpolytope.pl > cdpolytopes.txt
polymake --script ndpolytope.pl >> cdpolytopes.txt