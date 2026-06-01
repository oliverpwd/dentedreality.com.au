---
title: WordCamp Minnesota
date: '2010-11-13T03:53:46+00:00'
format: image
service: flickr
tags:
- minnesota
- snow
- wcmsp
- wordcamp
- wordcampmsp
- wordpress
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5183807212_8b704501d0_o.jpg?resize=607%2C452
---

[![WordCamp Minnesota](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5183807212_8b704501d0_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/11/13/wordcamp-minnesota-4/) 
# [WordCamp Minnesota](http://dentedreality.com.au/2010/11/13/wordcamp-minnesota-4/)

This is what happens when you tell everyone that you hope it snows in Minnesota





* #[minnesota](http://dentedreality.com.au/tags/minnesota/)
* #[snow](http://dentedreality.com.au/tags/snow/)
* #[wcmsp](http://dentedreality.com.au/tags/wcmsp/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)
* #[wordcampmsp](http://dentedreality.com.au/tags/wordcampmsp/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183807212/) [3:53 am, November 13, 2010](http://dentedreality.com.au/2010/11/13/wordcamp-minnesota-4/ "3:53 am") 
jQuery(document).ready(function(){
var gmap\_mf159d9ce68249b9aad220d5f2597872e = {
positions : {
917 : new google.maps.LatLng( '44.8635', '-93.287667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf159d9ce68249b9aad220d5f2597872e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf159d9ce68249b9aad220d5f2597872e.positions ) {
gmap\_mf159d9ce68249b9aad220d5f2597872e.bounds.extend( gmap\_mf159d9ce68249b9aad220d5f2597872e.positions[m] );
}
// Render markers
for ( var m in gmap\_mf159d9ce68249b9aad220d5f2597872e.positions ) {
gmap\_mf159d9ce68249b9aad220d5f2597872e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf159d9ce68249b9aad220d5f2597872e.map,
position : gmap\_mf159d9ce68249b9aad220d5f2597872e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf159d9ce68249b9aad220d5f2597872e.map.setCenter( gmap\_mf159d9ce68249b9aad220d5f2597872e.positions[917] );
});