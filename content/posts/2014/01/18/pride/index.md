---
title: Pride
date: '2014-01-18T17:26:37+00:00'
format: image
service: flickr
tags:
- erika
- pride
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13927393624_b102e9dbd5_o.jpg?resize=607%2C455
---

[![Pride](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13927393624_b102e9dbd5_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/01/18/pride/) 
# [Pride](http://dentedreality.com.au/2014/01/18/pride/)





* #[erika](http://dentedreality.com.au/tags/erika/)
* #[pride](http://dentedreality.com.au/tags/pride/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927393624/) [5:26 pm, January 18, 2014](http://dentedreality.com.au/2014/01/18/pride/ "5:26 pm") 
jQuery(document).ready(function(){
var gmap\_m81890ea0ae55651f23b52d5fb3fa6696 = {
positions : {
998 : new google.maps.LatLng( '40.686986', '-73.977609' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m81890ea0ae55651f23b52d5fb3fa6696' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m81890ea0ae55651f23b52d5fb3fa6696.positions ) {
gmap\_m81890ea0ae55651f23b52d5fb3fa6696.bounds.extend( gmap\_m81890ea0ae55651f23b52d5fb3fa6696.positions[m] );
}
// Render markers
for ( var m in gmap\_m81890ea0ae55651f23b52d5fb3fa6696.positions ) {
gmap\_m81890ea0ae55651f23b52d5fb3fa6696.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m81890ea0ae55651f23b52d5fb3fa6696.map,
position : gmap\_m81890ea0ae55651f23b52d5fb3fa6696.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m81890ea0ae55651f23b52d5fb3fa6696.map.setCenter( gmap\_m81890ea0ae55651f23b52d5fb3fa6696.positions[998] );
});