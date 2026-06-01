---
title: ''
date: '2012-11-29T22:26:19+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/52ed4c603a9511e2b17a22000a1fa432_7.jpg?resize=607%2C607
---

[![Sazerac. Delicious.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/52ed4c603a9511e2b17a22000a1fa432_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/11/29/sazerac-delicious/) 

Sazerac. Delicious.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/SowlqmCmO0/) [10:26 pm, November 29, 2012](http://dentedreality.com.au/2012/11/29/sazerac-delicious/ "10:26 pm") 
jQuery(document).ready(function(){
var gmap\_m0518927b59224745a122406796b3870c = {
positions : {
974 : new google.maps.LatLng( '29.935063', '-90.104307' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0518927b59224745a122406796b3870c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0518927b59224745a122406796b3870c.positions ) {
gmap\_m0518927b59224745a122406796b3870c.bounds.extend( gmap\_m0518927b59224745a122406796b3870c.positions[m] );
}
// Render markers
for ( var m in gmap\_m0518927b59224745a122406796b3870c.positions ) {
gmap\_m0518927b59224745a122406796b3870c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0518927b59224745a122406796b3870c.map,
position : gmap\_m0518927b59224745a122406796b3870c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0518927b59224745a122406796b3870c.map.setCenter( gmap\_m0518927b59224745a122406796b3870c.positions[974] );
});