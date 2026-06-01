---
title: ''
date: '2012-08-04T23:01:02+00:00'
format: image
service: instagram
tags:
- photo
- wcsf
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/caa8112edea911e1877122000a1e9e57_7.jpg?resize=607%2C607
---

[![Raawwrrrrrr #wcsf](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/caa8112edea911e1877122000a1e9e57_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/08/04/raawwrrrrrr-wcsf/) 

Raawwrrrrrr #wcsf





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[wcsf](http://dentedreality.com.au/tags/wcsf/)

Posted on [Instagram](http://instagram.com/p/N7jjqfimNQ/) [11:01 pm, August 4, 2012](http://dentedreality.com.au/2012/08/04/raawwrrrrrr-wcsf/ "11:01 pm") 
jQuery(document).ready(function(){
var gmap\_m7ce83ef0d8756b3943e007e0cbbcdf76 = {
positions : {
316 : new google.maps.LatLng( '37.766703027', '-122.402832559' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7ce83ef0d8756b3943e007e0cbbcdf76' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7ce83ef0d8756b3943e007e0cbbcdf76.positions ) {
gmap\_m7ce83ef0d8756b3943e007e0cbbcdf76.bounds.extend( gmap\_m7ce83ef0d8756b3943e007e0cbbcdf76.positions[m] );
}
// Render markers
for ( var m in gmap\_m7ce83ef0d8756b3943e007e0cbbcdf76.positions ) {
gmap\_m7ce83ef0d8756b3943e007e0cbbcdf76.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7ce83ef0d8756b3943e007e0cbbcdf76.map,
position : gmap\_m7ce83ef0d8756b3943e007e0cbbcdf76.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7ce83ef0d8756b3943e007e0cbbcdf76.map.setCenter( gmap\_m7ce83ef0d8756b3943e007e0cbbcdf76.positions[316] );
});