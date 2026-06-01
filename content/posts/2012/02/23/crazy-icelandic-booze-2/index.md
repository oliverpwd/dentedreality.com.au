---
title: Crazy Icelandic Booze
date: '2012-02-23T17:58:19+00:00'
format: image
service: flickr
tags:
- alcohol
- iceland
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813461396_a35ac57a5a_o.jpg?resize=607%2C813
---

[![Crazy Icelandic Booze](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813461396_a35ac57a5a_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/02/23/crazy-icelandic-booze-2/) 
# [Crazy Icelandic Booze](http://dentedreality.com.au/2012/02/23/crazy-icelandic-booze-2/)





* #[alcohol](http://dentedreality.com.au/tags/alcohol/)
* #[iceland](http://dentedreality.com.au/tags/iceland/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813461396/) [5:58 pm, February 23, 2012](http://dentedreality.com.au/2012/02/23/crazy-icelandic-booze-2/ "5:58 pm") 
jQuery(document).ready(function(){
var gmap\_md8bf37317a9f457c22dfd664d99c41d0 = {
positions : {
163 : new google.maps.LatLng( '37.766666', '-122.433' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md8bf37317a9f457c22dfd664d99c41d0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md8bf37317a9f457c22dfd664d99c41d0.positions ) {
gmap\_md8bf37317a9f457c22dfd664d99c41d0.bounds.extend( gmap\_md8bf37317a9f457c22dfd664d99c41d0.positions[m] );
}
// Render markers
for ( var m in gmap\_md8bf37317a9f457c22dfd664d99c41d0.positions ) {
gmap\_md8bf37317a9f457c22dfd664d99c41d0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md8bf37317a9f457c22dfd664d99c41d0.map,
position : gmap\_md8bf37317a9f457c22dfd664d99c41d0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md8bf37317a9f457c22dfd664d99c41d0.map.setCenter( gmap\_md8bf37317a9f457c22dfd664d99c41d0.positions[163] );
});