/*
  This povray file was created using polymake.
  It may be rendered using the following command:

  >povray +Iinput.pov +Ooutput.tga /opt/polymake/share/polymake/povray/polypov.ini
*/
#include "/opt/polymake/share/polymake/povray/polymake-scene.pov"

#declare MIN_EXTENT = <-0.586811,-0.896881,-0.998026>;
#declare MAX_EXTENT = <0.483599,-0.0464902,0.356511>;
#declare ORIGIN     = MIN_EXTENT + (MAX_EXTENT-MIN_EXTENT)/2;
#declare SCALE      = 1/vlength((MAX_EXTENT-MIN_EXTENT)/2);

//  ---BEGIN
#declare vertex_list_unnamed__1 = array[5] {
<-0.042216,-0.0464902,-0.998026>,
<-0.344432,-0.214557,-0.913965>,
<0.483599,-0.839236,-0.248624>,
<-0.586811,-0.727016,0.356511>,
<-0.422917,-0.896881,0.129405>}

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
    polygon { 4, vertex_list_unnamed__1[3], vertex_list_unnamed__1[1], vertex_list_unnamed__1[4], vertex_list_unnamed__1[3] }
    polygon { 4, vertex_list_unnamed__1[0], vertex_list_unnamed__1[1], vertex_list_unnamed__1[3], vertex_list_unnamed__1[0] }
    polygon { 4, vertex_list_unnamed__1[2], vertex_list_unnamed__1[1], vertex_list_unnamed__1[0], vertex_list_unnamed__1[2] }
    polygon { 4, vertex_list_unnamed__1[4], vertex_list_unnamed__1[1], vertex_list_unnamed__1[2], vertex_list_unnamed__1[4] }
    polygon { 4, vertex_list_unnamed__1[3], vertex_list_unnamed__1[2], vertex_list_unnamed__1[0], vertex_list_unnamed__1[3] }
    polygon { 4, vertex_list_unnamed__1[3], vertex_list_unnamed__1[4], vertex_list_unnamed__1[2], vertex_list_unnamed__1[3] }
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
    capsule ( vertex_list_unnamed__1[4], vertex_list_unnamed__1[1], eth )
    capsule ( vertex_list_unnamed__1[1], vertex_list_unnamed__1[3], eth )
    capsule ( vertex_list_unnamed__1[3], vertex_list_unnamed__1[4], eth )
    capsule ( vertex_list_unnamed__1[3], vertex_list_unnamed__1[1], eth )
    capsule ( vertex_list_unnamed__1[1], vertex_list_unnamed__1[0], eth )
    capsule ( vertex_list_unnamed__1[0], vertex_list_unnamed__1[3], eth )
    capsule ( vertex_list_unnamed__1[0], vertex_list_unnamed__1[1], eth )
    capsule ( vertex_list_unnamed__1[1], vertex_list_unnamed__1[2], eth )
    capsule ( vertex_list_unnamed__1[2], vertex_list_unnamed__1[0], eth )
    capsule ( vertex_list_unnamed__1[2], vertex_list_unnamed__1[1], eth )
    capsule ( vertex_list_unnamed__1[1], vertex_list_unnamed__1[4], eth )
    capsule ( vertex_list_unnamed__1[4], vertex_list_unnamed__1[2], eth )
    capsule ( vertex_list_unnamed__1[0], vertex_list_unnamed__1[2], eth )
    capsule ( vertex_list_unnamed__1[2], vertex_list_unnamed__1[3], eth )
    capsule ( vertex_list_unnamed__1[3], vertex_list_unnamed__1[0], eth )
    capsule ( vertex_list_unnamed__1[2], vertex_list_unnamed__1[4], eth )
    capsule ( vertex_list_unnamed__1[4], vertex_list_unnamed__1[3], eth )
    capsule ( vertex_list_unnamed__1[3], vertex_list_unnamed__1[2], eth )
  }
  texture { T_Polytope_wires pigment { color rgb <0,0,0> } }
}
object {
  edges_unnamed__1
  translate -ORIGIN
  scale SCALE
}

//  ---END
