---
title: E.H. Taylor Rye
date: '2013-06-11T18:49:39+00:00'
format: image
service: flickr
tags:
- rye
- taylor
- whiskey
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9439831770_3d127d23a4_o.jpg?resize=607%2C813
---

[![E.H. Taylor Rye](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9439831770_3d127d23a4_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2013/06/11/e-h-taylor-rye/) 
# [E.H. Taylor Rye](http://dentedreality.com.au/2013/06/11/e-h-taylor-rye/)

Delicious





* #[rye](http://dentedreality.com.au/tags/rye/)
* #[taylor](http://dentedreality.com.au/tags/taylor/)
* #[whiskey](http://dentedreality.com.au/tags/whiskey/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9439831770/) [6:49 pm, June 11, 2013](http://dentedreality.com.au/2013/06/11/e-h-taylor-rye/ "6:49 pm") 
jQuery(document).ready(function(){
var gmap\_mc7fdbc67917827810a9b1a673d1692f9 = {
positions : {
305 : new google.maps.LatLng( '45.516999', '-122.673834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc7fdbc67917827810a9b1a673d1692f9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc7fdbc67917827810a9b1a673d1692f9.positions ) {
gmap\_mc7fdbc67917827810a9b1a673d1692f9.bounds.extend( gmap\_mc7fdbc67917827810a9b1a673d1692f9.positions[m] );
}
// Render markers
for ( var m in gmap\_mc7fdbc67917827810a9b1a673d1692f9.positions ) {
gmap\_mc7fdbc67917827810a9b1a673d1692f9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc7fdbc67917827810a9b1a673d1692f9.map,
position : gmap\_mc7fdbc67917827810a9b1a673d1692f9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc7fdbc67917827810a9b1a673d1692f9.map.setCenter( gmap\_mc7fdbc67917827810a9b1a673d1692f9.positions[305] );
});