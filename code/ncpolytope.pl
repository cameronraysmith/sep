use application "polytope";

# non-contextual polytope
my $ncpoints=new Matrix<Rational>([[1,-1,-1,-1,-1,1,1,1,1],
								 [1,-1,-1,-1,1,1,1,-1,-1],
								 [1,-1,-1,1,-1,1,-1,-1,1],
								 [1,-1,-1,1,1,1,-1,1,-1],
								 [1,-1, 1,-1,-1,-1,-1,1,1],
								 [1,-1, 1,-1,1,-1,-1,-1,-1],
								 [1,-1, 1,1,-1,-1,1,-1,1],
								 [1,-1, 1,1,1,-1,1,1,-1],
								 [1, 1,-1,-1,-1,-1,1,1,-1],
								 [1, 1,-1,-1,1,-1,1,-1,1],
								 [1, 1,-1,1,-1,-1,-1,-1,-1],
								 [1, 1,-1,1,1,-1,-1,1,1],
								 [1, 1, 1,-1,-1,1,-1,1,-1],
								 [1, 1, 1,-1,1,1,-1,-1,1],
								 [1, 1, 1,1,-1,1,1,-1,-1],
								 [1, 1, 1,1,1,1,1,1,1]]);

my $nc=new Polytope<Rational>(POINTS=>$ncpoints);

print "\nNon-contextual polytope\n";
print "------------------------------\n";

print "constraints: \n";
print_constraints($ncpoints);

print "vertices: \n";
print $nc->VERTICES; print "\n";

print "facets: \n";
print $nc->FACETS; print "\n";

print "vertices in facets: \n";
print $nc->VERTICES_IN_FACETS; print "\n\n";

print "dimension: \n";
print $nc->DIM; print "\n\n";

print "bounded?: \n";
print $nc->BOUNDED; print "\n\n";

print "volume: \n";
print $nc->VOLUME; print "\n";
