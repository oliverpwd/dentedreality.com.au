---
title: ''
date: '2016-01-10T11:27:56+00:00'
format: image
service: instagram
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/01/12407723_616460098491806_2009500561_n.jpg?fit=640%2C640
---

[![Not bad, South Africa. Not bad.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/01/12407723_616460098491806_2009500561_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/01/10/not-bad-south-africa-not-bad/) 

Not bad, South Africa. Not bad.





Posted on [Instagram](https://www.instagram.com/p/BAXlq2OimHY/) [11:27 am, January 10, 2016](http://dentedreality.com.au/2016/01/10/not-bad-south-africa-not-bad/ "11:27 am") 
jQuery(document).ready(function(){
var gmap\_m83c3f47fc0ff54cacda1816f3cd4984f = {
positions : {
249 : new google.maps.LatLng( '-33.9253', '18.4239' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m83c3f47fc0ff54cacda1816f3cd4984f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m83c3f47fc0ff54cacda1816f3cd4984f.positions ) {
gmap\_m83c3f47fc0ff54cacda1816f3cd4984f.bounds.extend( gmap\_m83c3f47fc0ff54cacda1816f3cd4984f.positions[m] );
}
// Render markers
for ( var m in gmap\_m83c3f47fc0ff54cacda1816f3cd4984f.positions ) {
gmap\_m83c3f47fc0ff54cacda1816f3cd4984f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m83c3f47fc0ff54cacda1816f3cd4984f.map,
position : gmap\_m83c3f47fc0ff54cacda1816f3cd4984f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m83c3f47fc0ff54cacda1816f3cd4984f.map.setCenter( gmap\_m83c3f47fc0ff54cacda1816f3cd4984f.positions[249] );
});