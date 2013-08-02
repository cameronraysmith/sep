/*
  This povray file was created using polymake.
  It may be rendered using the following command:

  >povray +Iinput.pov +Ooutput.tga /opt/polymake/share/polymake/povray/polypov.ini
*/
#include "/opt/polymake/share/polymake/povray/polymake-scene.pov"

#declare MIN_EXTENT = <-0.25,-0.25,-0.25>;
#declare MAX_EXTENT = <0.75,0.75,0.75>;
#declare ORIGIN     = MIN_EXTENT + (MAX_EXTENT-MIN_EXTENT)/2;
#declare SCALE      = 1/vlength((MAX_EXTENT-MIN_EXTENT)/2);

//  ---BEGIN
#declare vertex_list_unnamed__1 = array[5] {
<-0.25,-0.25,-0.25>,
<0,0,0>,
<0.75,-0.25,-0.25>,
<-0.25,0.75,-0.25>,
<-0.25,-0.25,0.75>}

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

#declare lines_unnamed__1 = object {
  #local lth = 0.03/SCALE;
  #local al = 0.3;
  #local aw = 2;
  union {
    object { capsule (vertex_list_unnamed__1[1], vertex_list_unnamed__1[0], lth) texture { T_Polytope_wires pigment { color rgb <0.4667,0.9255,0.6196> } } }
    object { capsule (vertex_list_unnamed__1[2], vertex_list_unnamed__1[0], lth) texture { T_Polytope_wires pigment { color rgb <0,0,0> } } }
    object { capsule (vertex_list_unnamed__1[2], vertex_list_unnamed__1[1], lth) texture { T_Polytope_wires pigment { color rgb <0.4667,0.9255,0.6196> } } }
    object { capsule (vertex_list_unnamed__1[3], vertex_list_unnamed__1[0], lth) texture { T_Polytope_wires pigment { color rgb <0,0,0> } } }
    object { capsule (vertex_list_unnamed__1[3], vertex_list_unnamed__1[1], lth) texture { T_Polytope_wires pigment { color rgb <0.4667,0.9255,0.6196> } } }
    object { capsule (vertex_list_unnamed__1[3], vertex_list_unnamed__1[2], lth) texture { T_Polytope_wires pigment { color rgb <0,0,0> } } }
    object { capsule (vertex_list_unnamed__1[4], vertex_list_unnamed__1[0], lth) texture { T_Polytope_wires pigment { color rgb <0,0,0> } } }
    object { capsule (vertex_list_unnamed__1[4], vertex_list_unnamed__1[1], lth) texture { T_Polytope_wires pigment { color rgb <0.4667,0.9255,0.6196> } } }
    object { capsule (vertex_list_unnamed__1[4], vertex_list_unnamed__1[2], lth) texture { T_Polytope_wires pigment { color rgb <0,0,0> } } }
    object { capsule (vertex_list_unnamed__1[4], vertex_list_unnamed__1[3], lth) texture { T_Polytope_wires pigment { color rgb <0,0,0> } } }
}}
object {
  lines_unnamed__1
  translate -ORIGIN
  scale SCALE
}

//  ---END
