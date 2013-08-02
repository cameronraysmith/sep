/*
  This povray file was created using polymake.
  It may be rendered using the following command:

  >povray +Iinput.pov +Ooutput.tga /opt/polymake/share/polymake/povray/polypov.ini
*/
#include "/opt/polymake/share/polymake/povray/polymake-scene.pov"

#declare MIN_EXTENT = <0,0>;
#declare MAX_EXTENT = <1,1>;
#declare ORIGIN     = MIN_EXTENT + (MAX_EXTENT-MIN_EXTENT)/2;
#declare SCALE      = 1/vlength((MAX_EXTENT-MIN_EXTENT)/2);

//  ---BEGIN
#declare vertex_list_unnamed__1 = array[3] {
<0,0>,
<1,0>,
<0,1>}

#declare vertices_of_unnamed__1 = object {
  #local pth = 0.06/SCALE;
  union {
    sphere { vertex_list_unnamed__1[0], pth }
    sphere { vertex_list_unnamed__1[1], pth }
    sphere { vertex_list_unnamed__1[2], pth }
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
    polygon { 4, vertex_list_unnamed__1[0], vertex_list_unnamed__1[1], vertex_list_unnamed__1[2], vertex_list_unnamed__1[0] }
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
    capsule ( vertex_list_unnamed__1[2], vertex_list_unnamed__1[1], eth )
    capsule ( vertex_list_unnamed__1[1], vertex_list_unnamed__1[0], eth )
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
