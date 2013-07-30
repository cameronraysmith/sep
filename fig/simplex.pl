$Verbose::credits=0;
use application "polytope";
my $ss2 = simplex(2);
my $ss3 = simplex(3);
my $ss4 = simplex(3);

print "2-simplex";
print "-------------------------";
print "volume:";
print "\n";
print $ss2->VOLUME;
print "\n";
print "\n";
print "vertices:";
print "\n";
print $ss2->VERTICES;
print "\n";
print "facets:";
print "\n";
print $ss2->FACETS;
print "\n";
print "\n";
print "constraints:";
print "\n";
print_constraints($ss2);
print "\n";
print "\n";
print "render POVray...";
povray($ss2->VISUAL, File=>'simplex2.pov');
$ss2->VISUAL(FacetTransparency=>'0.5',VertexThickness=>'0.3');
print "\n";
print "\n";

print "3-simplex";
print "-------------------------";
print "volume:";
print "\n";
print $ss3->VOLUME;
print "\n";
print "\n";
print "vertices:";
print "\n";
print $ss3->VERTICES;
print "\n";
print "facets:";
print "\n";
print $ss3->FACETS;
print "\n";
print "\n";
print "constraints:";
print "\n";
print_constraints($ss3);
print "\n";
print "\n";
print "render POVray...";
povray($ss3->VISUAL, File=>'simplex3.pov');
$ss3->VISUAL(FacetTransparency=>'0.5',VertexThickness=>'0.3');
print "\n";
print "\n";
