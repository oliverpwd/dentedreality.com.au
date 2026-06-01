---
title: SXSW 2011
date: '2011-03-13T09:42:44+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2011
- texas
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802656706_d320faafd2_o.jpg?resize=607%2C452
---

[![SXSW 2011](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802656706_d320faafd2_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/03/13/sxsw-2011-3/) 
# [SXSW 2011](http://dentedreality.com.au/2011/03/13/sxsw-2011-3/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2011](http://dentedreality.com.au/tags/sxsw2011/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802656706/) [9:42 am, March 13, 2011](http://dentedreality.com.au/2011/03/13/sxsw-2011-3/ "9:42 am") 
jQuery(document).ready(function(){
var gmap\_m7339ac89d641be4eb2f02cc653213048 = {
positions : {
901 : new google.maps.LatLng( '30.264', '-97.739834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7339ac89d641be4eb2f02cc653213048' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7339ac89d641be4eb2f02cc653213048.positions ) {
gmap\_m7339ac89d641be4eb2f02cc653213048.bounds.extend( gmap\_m7339ac89d641be4eb2f02cc653213048.positions[m] );
}
// Render markers
for ( var m in gmap\_m7339ac89d641be4eb2f02cc653213048.positions ) {
gmap\_m7339ac89d641be4eb2f02cc653213048.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7339ac89d641be4eb2f02cc653213048.map,
position : gmap\_m7339ac89d641be4eb2f02cc653213048.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7339ac89d641be4eb2f02cc653213048.map.setCenter( gmap\_m7339ac89d641be4eb2f02cc653213048.positions[901] );
});