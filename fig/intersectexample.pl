$Verbose::credits=0;
use application "polytope";
my $ss1 = rand_sphere(3,5);
my $ss2 = rand_sphere(3,5);
#my $ss1 = simplex(3);
#my $ss2 = cube(3);

my $ss3 = intersection($ss1,$ss2);

print $ss1->VOLUME;
print "\n";
print $ss1->VERTICES;
print "\n";
print $ss1->FACETS;
print "\n";
#$ss1->VISUAL(FacetTransparency=>'0.5',VertexThickness=>'0.3');
print "\n";

print $ss2->VOLUME;
print "\n";
print $ss2->VERTICES;
print "\n";
print $ss2->FACETS;
print "\n";
#$ss2->VISUAL(FacetTransparency=>'0.5',VertexThickness=>'0.3');
print "\n";

print $ss3->VOLUME;
print "\n";
print $ss3->VERTICES;
print "\n";
print $ss3->FACETS;
print "\n";
#$ss3->VISUAL(FacetTransparency=>'0.5',VertexThickness=>'0.3');
print "\n";

povray($ss1->VISUAL, File=>'ss1.pov');
povray($ss2->VISUAL, File=>'ss2.pov');
povray($ss3->VISUAL, File=>'ss3.pov');

