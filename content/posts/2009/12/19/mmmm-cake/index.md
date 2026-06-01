---
title: Mmmm, Cake
date: '2009-12-19T12:23:29+00:00'
format: image
service: flickr
tags:
- cake
- Chile
- dessert
- Santiago
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2009/12/4202749997_69e2a6397b_o.jpg?resize=607%2C455
---

[![Mmmm, Cake](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2009/12/4202749997_69e2a6397b_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2009/12/19/mmmm-cake/) 
# [Mmmm, Cake](http://dentedreality.com.au/2009/12/19/mmmm-cake/)





* #[cake](http://dentedreality.com.au/tags/cake/)
* #[Chile](http://dentedreality.com.au/tags/chile/)
* #[dessert](http://dentedreality.com.au/tags/dessert/)
* #[Santiago](http://dentedreality.com.au/tags/santiago/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4202749997/) [12:23 pm, December 19, 2009](http://dentedreality.com.au/2009/12/19/mmmm-cake/ "12:23 pm") 
jQuery(document).ready(function(){
var gmap\_m5f05342e73f502ecc3246b8309b92415 = {
positions : {
251 : new google.maps.LatLng( '-33.425667', '-70.618334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5f05342e73f502ecc3246b8309b92415' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5f05342e73f502ecc3246b8309b92415.positions ) {
gmap\_m5f05342e73f502ecc3246b8309b92415.bounds.extend( gmap\_m5f05342e73f502ecc3246b8309b92415.positions[m] );
}
// Render markers
for ( var m in gmap\_m5f05342e73f502ecc3246b8309b92415.positions ) {
gmap\_m5f05342e73f502ecc3246b8309b92415.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5f05342e73f502ecc3246b8309b92415.map,
position : gmap\_m5f05342e73f502ecc3246b8309b92415.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5f05342e73f502ecc3246b8309b92415.map.setCenter( gmap\_m5f05342e73f502ecc3246b8309b92415.positions[251] );
});