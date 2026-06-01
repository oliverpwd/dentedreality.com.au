---
title: Descent
date: '2008-04-04T21:49:40+00:00'
format: image
service: flickr
tags:
- australia
- beach
- ocean
- path
- renniewedding
- timswedding
- westernaustraliadenmark
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433429196_9273be5bfc_o.jpg?resize=607%2C808
---

[![Descent](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433429196_9273be5bfc_o.jpg?resize=607%2C808)](http://dentedreality.com.au/2008/04/04/descent/) 
# [Descent](http://dentedreality.com.au/2008/04/04/descent/)

Down to the beach to take wedding photos!





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[ocean](http://dentedreality.com.au/tags/ocean/)
* #[path](http://dentedreality.com.au/tags/path/)
* #[renniewedding](http://dentedreality.com.au/tags/renniewedding/)
* #[timswedding](http://dentedreality.com.au/tags/timswedding/)
* #[westernaustraliadenmark](http://dentedreality.com.au/tags/westernaustraliadenmark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2433429196/) [9:49 pm, April 4, 2008](http://dentedreality.com.au/2008/04/04/descent/ "9:49 pm") 
jQuery(document).ready(function(){
var gmap\_md237c4d0eb248a19e49a82b0ac89bfcd = {
positions : {
970 : new google.maps.LatLng( '-35.03604', '117.329177' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md237c4d0eb248a19e49a82b0ac89bfcd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md237c4d0eb248a19e49a82b0ac89bfcd.positions ) {
gmap\_md237c4d0eb248a19e49a82b0ac89bfcd.bounds.extend( gmap\_md237c4d0eb248a19e49a82b0ac89bfcd.positions[m] );
}
// Render markers
for ( var m in gmap\_md237c4d0eb248a19e49a82b0ac89bfcd.positions ) {
gmap\_md237c4d0eb248a19e49a82b0ac89bfcd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md237c4d0eb248a19e49a82b0ac89bfcd.map,
position : gmap\_md237c4d0eb248a19e49a82b0ac89bfcd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md237c4d0eb248a19e49a82b0ac89bfcd.map.setCenter( gmap\_md237c4d0eb248a19e49a82b0ac89bfcd.positions[970] );
});