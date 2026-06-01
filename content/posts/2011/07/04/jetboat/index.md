---
title: Jetboat
date: '2011-07-04T13:32:13+00:00'
format: image
service: flickr
tags:
- boat
- jetboat
- speedboat
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6322927389_c88476ef0f_o.jpg?resize=607%2C452
---

[![Jetboat](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6322927389_c88476ef0f_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/07/04/jetboat/) 
# [Jetboat](http://dentedreality.com.au/2011/07/04/jetboat/)





* #[boat](http://dentedreality.com.au/tags/boat/)
* #[jetboat](http://dentedreality.com.au/tags/jetboat/)
* #[speedboat](http://dentedreality.com.au/tags/speedboat/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6322927389/) [1:32 pm, July 4, 2011](http://dentedreality.com.au/2011/07/04/jetboat/ "1:32 pm") 
jQuery(document).ready(function(){
var gmap\_ma24720dfe9175eea57573762b6d4c59b = {
positions : {
70 : new google.maps.LatLng( '37.906833', '-121.593' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma24720dfe9175eea57573762b6d4c59b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma24720dfe9175eea57573762b6d4c59b.positions ) {
gmap\_ma24720dfe9175eea57573762b6d4c59b.bounds.extend( gmap\_ma24720dfe9175eea57573762b6d4c59b.positions[m] );
}
// Render markers
for ( var m in gmap\_ma24720dfe9175eea57573762b6d4c59b.positions ) {
gmap\_ma24720dfe9175eea57573762b6d4c59b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma24720dfe9175eea57573762b6d4c59b.map,
position : gmap\_ma24720dfe9175eea57573762b6d4c59b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma24720dfe9175eea57573762b6d4c59b.map.setCenter( gmap\_ma24720dfe9175eea57573762b6d4c59b.positions[70] );
});