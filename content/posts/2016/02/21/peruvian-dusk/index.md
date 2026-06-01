---
title: ''
date: '2016-02-21T08:07:32+00:00'
format: image
service: instagram
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/02/12729462_503437783197220_511905957_n.jpg?fit=640%2C640
---

[![Peruvian Dusk](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/02/12729462_503437783197220_511905957_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/02/21/peruvian-dusk/) 

Peruvian Dusk





Posted on [Instagram](https://www.instagram.com/p/BCDYHu5imBT/) [8:07 am, February 21, 2016](http://dentedreality.com.au/2016/02/21/peruvian-dusk/ "8:07 am") 
jQuery(document).ready(function(){
var gmap\_m2c2c4ee907c088b6019d5826edbdf536 = {
positions : {
25 : new google.maps.LatLng( '-12.1313066', '-77.0299683' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2c2c4ee907c088b6019d5826edbdf536' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2c2c4ee907c088b6019d5826edbdf536.positions ) {
gmap\_m2c2c4ee907c088b6019d5826edbdf536.bounds.extend( gmap\_m2c2c4ee907c088b6019d5826edbdf536.positions[m] );
}
// Render markers
for ( var m in gmap\_m2c2c4ee907c088b6019d5826edbdf536.positions ) {
gmap\_m2c2c4ee907c088b6019d5826edbdf536.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2c2c4ee907c088b6019d5826edbdf536.map,
position : gmap\_m2c2c4ee907c088b6019d5826edbdf536.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2c2c4ee907c088b6019d5826edbdf536.map.setCenter( gmap\_m2c2c4ee907c088b6019d5826edbdf536.positions[25] );
});