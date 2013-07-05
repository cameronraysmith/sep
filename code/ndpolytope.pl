use application "polytope";

# no-disturbance polytope
my $ndpoints=new Matrix<Rational>([[1, -1, -1, -1, -1, 1, 1, 1, 1],
 [1, -1, -1, -1, 1, 1, 1, -1, -1],
 [1, -1, -1, 1, -1, 1, -1, -1, 1],
 [1, -1, -1, 1, 1, 1, -1, 1, -1],
 [1, -1, 1, -1, -1, -1, -1, 1, 1],
 [1, -1, 1, -1, 1, -1, -1, -1, -1],
 [1, -1, 1, 1, -1, -1, 1, -1, 1],
 [1, -1, 1, 1, 1, -1, 1, 1, -1],
 [1, 1, -1, -1, -1, -1, 1, 1, -1],
 [1, 1, -1, -1, 1, -1, 1, -1, 1],
 [1, 1, -1, 1, -1, -1, -1, -1, -1],
 [1, 1, -1, 1, 1, -1, -1, 1, 1],
 [1, 1, 1, -1, -1, 1, -1, 1, -1],
 [1, 1, 1, -1, 1, 1, -1, -1, 1],
 [1, 1, 1, 1, -1, 1, 1, -1, -1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 0, -1, 1, 1, 1],
 [1, 0, 0, 0, 0, 1, -1, 1, 1],
 [1, 0, 0, 0, 0, 1, 1, -1, 1],
 [1, 0, 0, 0, 0, 1, 1, 1, -1],
 [1, 0, 0, 0, 0, -1, -1, -1, 1],
 [1, 0, 0, 0, 0, -1, -1, 1, -1],
 [1, 0, 0, 0, 0, -1, 1, -1, -1],
 [1, 0, 0, 0, 0, 1, -1, -1, -1]]);

my $nd=new Polytope<Rational>(POINTS=>$ndpoints);

print "\nNo-disturbance polytope\n";
print "------------------------------\n";

print "constraints: \n";
print_constraints($ndpoints);

print "vertices: \n";
print $nd->VERTICES; print "\n";

print "facets: \n";
print $nd->FACETS; print "\n";

print "vertices in facets: \n";
print $nd->VERTICES_IN_FACETS; print "\n\n";

print "dimension: \n";
print $nd->DIM; print "\n\n";

print "bounded?: \n";
print $nd->BOUNDED; print "\n\n";

print "volume: \n";
print $nd->VOLUME; print "\n";
