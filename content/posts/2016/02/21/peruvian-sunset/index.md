---
title: ''
date: '2016-02-21T16:22:21+00:00'
format: image
service: instagram
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/02/12728683_1652000248387071_1351612746_n.jpg?fit=640%2C640
---

[![Peruvian Sunset.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/02/12728683_1652000248387071_1351612746_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/02/21/peruvian-sunset/) 

Peruvian Sunset.





Posted on [Instagram](https://www.instagram.com/p/BCEQv_dimOH/) [4:22 pm, February 21, 2016](http://dentedreality.com.au/2016/02/21/peruvian-sunset/ "4:22 pm") 
jQuery(document).ready(function(){
var gmap\_mb90ec0e34653bcdf1e1a1c7c5527b967 = {
positions : {
201 : new google.maps.LatLng( '-12.09977354', '-77.042277521' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb90ec0e34653bcdf1e1a1c7c5527b967' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb90ec0e34653bcdf1e1a1c7c5527b967.positions ) {
gmap\_mb90ec0e34653bcdf1e1a1c7c5527b967.bounds.extend( gmap\_mb90ec0e34653bcdf1e1a1c7c5527b967.positions[m] );
}
// Render markers
for ( var m in gmap\_mb90ec0e34653bcdf1e1a1c7c5527b967.positions ) {
gmap\_mb90ec0e34653bcdf1e1a1c7c5527b967.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb90ec0e34653bcdf1e1a1c7c5527b967.map,
position : gmap\_mb90ec0e34653bcdf1e1a1c7c5527b967.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb90ec0e34653bcdf1e1a1c7c5527b967.map.setCenter( gmap\_mb90ec0e34653bcdf1e1a1c7c5527b967.positions[201] );
});