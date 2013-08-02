/*
  This povray file was created using polymake.
  It may be rendered using the following command:

  >povray +Iinput.pov +Ooutput.tga /opt/polymake/share/polymake/povray/polypov.ini
*/
#include "/opt/polymake/share/polymake/povray/polymake-scene.pov"

#declare MIN_EXTENT = <-0.137391,-0.586815,-0.55352>;
#declare MAX_EXTENT = <0.303886,-0.432849,-0.345837>;
#declare ORIGIN     = MIN_EXTENT + (MAX_EXTENT-MIN_EXTENT)/2;
#declare SCALE      = 1/vlength((MAX_EXTENT-MIN_EXTENT)/2);

//  ---BEGIN
#declare vertex_list_unnamed__1 = array[8] {
<-0.137391,-0.458216,-0.345837>,
<-0.0341058,-0.432849,-0.455587>,
<0.026977,-0.544345,-0.541534>,
<-0.0269479,-0.569751,-0.486257>,
<0.303886,-0.568291,-0.504755>,
<0.275172,-0.525,-0.545679>,
<0.10415,-0.552974,-0.55352>,
<0.149008,-0.586815,-0.517476>}

#declare vertices_of_unnamed__1 = object {
  #local pth = 0.06/SCALE;
  union {
    sphere { vertex_list_unnamed__1[0], pth }
    sphere { vertex_list_unnamed__1[1], pth }
    sphere { vertex_list_unnamed__1[2], pth }
    sphere { vertex_list_unnamed__1[3], pth }
    sphere { vertex_list_unnamed__1[4], pth }
    sphere { vertex_list_unnamed__1[5], pth }
    sphere { vertex_list_unnamed__1[6], pth }
    sphere { vertex_list_unnamed__1[7], pth }
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
    polygon { 5, vertex_list_unnamed__1[0], vertex_list_unnamed__1[1], vertex_list_unnamed__1[2], vertex_list_unnamed__1[3], vertex_list_unnamed__1[0] }
    polygon { 5, vertex_list_unnamed__1[6], vertex_list_unnamed__1[5], vertex_list_unnamed__1[4], vertex_list_unnamed__1[7], vertex_list_unnamed__1[6] }
    polygon { 5, vertex_list_unnamed__1[5], vertex_list_unnamed__1[1], vertex_list_unnamed__1[0], vertex_list_unnamed__1[4], vertex_list_unnamed__1[5] }
    polygon { 5, vertex_list_unnamed__1[0], vertex_list_unnamed__1[3], vertex_list_unnamed__1[7], vertex_list_unnamed__1[4], vertex_list_unnamed__1[0] }
    polygon { 5, vertex_list_unnamed__1[2], vertex_list_unnamed__1[1], vertex_list_unnamed__1[5], vertex_list_unnamed__1[6], vertex_list_unnamed__1[2] }
    polygon { 5, vertex_list_unnamed__1[3], vertex_list_unnamed__1[2], vertex_list_unnamed__1[6], vertex_list_unnamed__1[7], vertex_list_unnamed__1[3] }
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
    capsule ( vertex_list_unnamed__1[3], vertex_list_unnamed__1[2], eth )
    capsule ( vertex_list_unnamed__1[2], vertex_list_unnamed__1[1], eth )
    capsule ( vertex_list_unnamed__1[1], vertex_list_unnamed__1[0], eth )
    capsule ( vertex_list_unnamed__1[0], vertex_list_unnamed__1[3], eth )
    capsule ( vertex_list_unnamed__1[7], vertex_list_unnamed__1[4], eth )
    capsule ( vertex_list_unnamed__1[4], vertex_list_unnamed__1[5], eth )
    capsule ( vertex_list_unnamed__1[5], vertex_list_unnamed__1[6], eth )
    capsule ( vertex_list_unnamed__1[6], vertex_list_unnamed__1[7], eth )
    capsule ( vertex_list_unnamed__1[4], vertex_list_unnamed__1[0], eth )
    capsule ( vertex_list_unnamed__1[0], vertex_list_unnamed__1[1], eth )
    capsule ( vertex_list_unnamed__1[1], vertex_list_unnamed__1[5], eth )
    capsule ( vertex_list_unnamed__1[5], vertex_list_unnamed__1[4], eth )
    capsule ( vertex_list_unnamed__1[4], vertex_list_unnamed__1[7], eth )
    capsule ( vertex_list_unnamed__1[7], vertex_list_unnamed__1[3], eth )
    capsule ( vertex_list_unnamed__1[3], vertex_list_unnamed__1[0], eth )
    capsule ( vertex_list_unnamed__1[0], vertex_list_unnamed__1[4], eth )
    capsule ( vertex_list_unnamed__1[6], vertex_list_unnamed__1[5], eth )
    capsule ( vertex_list_unnamed__1[5], vertex_list_unnamed__1[1], eth )
    capsule ( vertex_list_unnamed__1[1], vertex_list_unnamed__1[2], eth )
    capsule ( vertex_list_unnamed__1[2], vertex_list_unnamed__1[6], eth )
    capsule ( vertex_list_unnamed__1[7], vertex_list_unnamed__1[6], eth )
    capsule ( vertex_list_unnamed__1[6], vertex_list_unnamed__1[2], eth )
    capsule ( vertex_list_unnamed__1[2], vertex_list_unnamed__1[3], eth )
    capsule ( vertex_list_unnamed__1[3], vertex_list_unnamed__1[7], eth )
  }
  texture { T_Polytope_wires pigment { color rgb <0,0,0> } }
}
object {
  edges_unnamed__1
  translate -ORIGIN
  scale SCALE
}

//  ---END
