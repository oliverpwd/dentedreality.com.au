---
title: IMG_0181
date: '2009-09-29T19:37:42+00:00'
format: image
service: flickr
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2009/09/4123186826_da6a8ec466_o.jpg?resize=607%2C455
---

[![IMG_0181](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2009/09/4123186826_da6a8ec466_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2009/09/29/img_0181/) 
# [IMG\_0181](http://dentedreality.com.au/2009/09/29/img_0181/)





Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4123186826/) [7:37 pm, September 29, 2009](http://dentedreality.com.au/2009/09/29/img_0181/ "7:37 pm") 
jQuery(document).ready(function(){
var gmap\_m1271607a03899f5859a14d15c45b69ce = {
positions : {
90 : new google.maps.LatLng( '37.766999', '-122.4295' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1271607a03899f5859a14d15c45b69ce' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1271607a03899f5859a14d15c45b69ce.positions ) {
gmap\_m1271607a03899f5859a14d15c45b69ce.bounds.extend( gmap\_m1271607a03899f5859a14d15c45b69ce.positions[m] );
}
// Render markers
for ( var m in gmap\_m1271607a03899f5859a14d15c45b69ce.positions ) {
gmap\_m1271607a03899f5859a14d15c45b69ce.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1271607a03899f5859a14d15c45b69ce.map,
position : gmap\_m1271607a03899f5859a14d15c45b69ce.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1271607a03899f5859a14d15c45b69ce.map.setCenter( gmap\_m1271607a03899f5859a14d15c45b69ce.positions[90] );
});