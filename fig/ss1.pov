/*
  This povray file was created using polymake.
  It may be rendered using the following command:

  >povray +Iinput.pov +Ooutput.tga /opt/polymake/share/polymake/povray/polypov.ini
*/
#include "/opt/polymake/share/polymake/povray/polymake-scene.pov"

#declare MIN_EXTENT = <-0.820475,-0.723115,-0.679339>;
#declare MAX_EXTENT = <0.984894,0.665458,0.522657>;
#declare ORIGIN     = MIN_EXTENT + (MAX_EXTENT-MIN_EXTENT)/2;
#declare SCALE      = 1/vlength((MAX_EXTENT-MIN_EXTENT)/2);

//  ---BEGIN
#declare vertex_list_unnamed__1 = array[5] {
<-0.635805,0.665458,0.391046>,
<0.124914,-0.723115,-0.679339>,
<0.984894,0.100383,-0.141095>,
<0.969629,-0.213163,-0.119921>,
<-0.820475,0.231625,0.522657>}

#declare vertices_of_unnamed__1 = object {
  #local pth = 0.06/SCALE;
  union {
    sphere { vertex_list_unnamed__1[0], pth }
    sphere { vertex_list_unnamed__1[1], pth }
    sphere { vertex_list_unnamed__1[2], pth }
    sphere { vertex_list_unnamed__1[3], pth }
    sphere { vertex_list_unnamed__1[4], pth }
  }
  texture { T_Polytope_nodes pigment { color rgb <1,0,0> } }
}
object {
  vertices_of_unnamed__1
  translate -ORIGIN
  scale SCALE
}

#declare faces_unnamed__1 = object {
  union {
    polygon { 4, vertex_list_unnamed__1[1], vertex_list_unnamed__1[4], vertex_list_unnamed__1[0], vertex_list_unnamed__1[1] }
    polygon { 4, vertex_list_unnamed__1[3], vertex_list_unnamed__1[4], vertex_list_unnamed__1[1], vertex_list_unnamed__1[3] }
    polygon { 4, vertex_list_unnamed__1[1], vertex_list_unnamed__1[2], vertex_list_unnamed__1[3], vertex_list_unnamed__1[1] }
    polygon { 4, vertex_list_unnamed__1[1], vertex_list_unnamed__1[0], vertex_list_unnamed__1[2], vertex_list_unnamed__1[1] }
    polygon { 4, vertex_list_unnamed__1[2], vertex_list_unnamed__1[4], vertex_list_unnamed__1[3], vertex_list_unnamed__1[2] }
    polygon { 4, vertex_list_unnamed__1[0], vertex_list_unnamed__1[4], vertex_list_unnamed__1[2], vertex_list_unnamed__1[0] }
  }
  texture { T_Polytope_solid pigment { color rgbt <0.4667,0.9255,0.6196,0> } }
}
object {
  faces_unnamed__1
  translate -ORIGIN
  scale SCALE
}

#declare edges_unnamed__1 = object {
  #local eth = 0.03/SCALE;
  union {
    capsule ( vertex_list_unnamed__1[0], vertex_list_unnamed__1[4], eth )
    capsule ( vertex_list_unnamed__1[4], vertex_list_unnamed__1[1], eth )
    capsule ( vertex_list_unnamed__1[1], vertex_list_unnamed__1[0], eth )
    capsule ( vertex_list_unnamed__1[1], vertex_list_unnamed__1[4], eth )
    capsule ( vertex_list_unnamed__1[4], vertex_list_unnamed__1[3], eth )
    capsule ( vertex_list_unnamed__1[3], vertex_list_unnamed__1[1], eth )
    capsule ( vertex_list_unnamed__1[3], vertex_list_unnamed__1[2], eth )
    capsule ( vertex_list_unnamed__1[2], vertex_list_unnamed__1[1], eth )
    capsule ( vertex_list_unnamed__1[1], vertex_list_unnamed__1[3], eth )
    capsule ( vertex_list_unnamed__1[2], vertex_list_unnamed__1[0], eth )
    capsule ( vertex_list_unnamed__1[0], vertex_list_unnamed__1[1], eth )
    capsule ( vertex_list_unnamed__1[1], vertex_list_unnamed__1[2], eth )
    capsule ( vertex_list_unnamed__1[3], vertex_list_unnamed__1[4], eth )
    capsule ( vertex_list_unnamed__1[4], vertex_list_unnamed__1[2], eth )
    capsule ( vertex_list_unnamed__1[2], vertex_list_unnamed__1[3], eth )
    capsule ( vertex_list_unnamed__1[2], vertex_list_unnamed__1[4], eth )
    capsule ( vertex_list_unnamed__1[4], vertex_list_unnamed__1[0], eth )
    capsule ( vertex_list_unnamed__1[0], vertex_list_unnamed__1[2], eth )
  }
  texture { T_Polytope_wires pigment { color rgb <0,0,0> } }
}
object {
  edges_unnamed__1
  translate -ORIGIN
  scale SCALE
}

//  ---END
