$Verbose::credits=0;

use application "polytope";

#open(INPUT, "< k5ndaffinehull.vert");
open(INPUT, "< k5nc.vert");
my $k5ncpoints=new Matrix<Rational>(<INPUT>);
close(INPUT);
print $k5ncpoints;

#my $k5nd=new Polytope<Rational>(EQUATIONS=>$k5ndeq,INEQUALITIES=>$k5ndineq);

my $nc=new Polytope<Rational>(POINTS=>$k5ncpoints);

# http://www.polymake.org/doku.php/tutorial/lattice_polytopes_tutorial
my $g=vertex_lattice_normalization($nc);

print "volume: \n";
print $g->VOLUME; print "\n";

# print "linear span: \n";
# print $k5nd->LINEAR_SPAN; print "\n";

# print "vertices: \n";
# print $k5nd->RAYS; print "\n";

# print "facets: \n";
# print $k5nd->FACETS; print "\n";
# print $k5nd->N_FACETS; print "\n";

# print "vertices: \n";
# print $k5nd->VERTICES; print "\n\n";

# print "vertices in facets: \n";
# print $k5nd->VERTICES_IN_FACETS; print "\n\n";

# print "dimension: \n";
# print $k5nd->DIM; print "\n\n";

# print "bounded?: \n";
# print $k5nd->BOUNDED; print "\n\n";

# print "volume: \n";
# print $k5nd->VOLUME; print "\n";

#$k5nd->VISUAL_FACE_LATTICE;
