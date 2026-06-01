---
title: Samurai Armor
date: '2011-01-10T11:38:16+00:00'
format: image
service: flickr
tags:
- armor
- samurai
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434722034_0192fae788_o.jpg?resize=607%2C813
---

[![Samurai Armor](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434722034_0192fae788_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/01/10/samurai-armor-2/) 
# [Samurai Armor](http://dentedreality.com.au/2011/01/10/samurai-armor-2/)





* #[armor](http://dentedreality.com.au/tags/armor/)
* #[samurai](http://dentedreality.com.au/tags/samurai/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434722034/) [11:38 am, January 10, 2011](http://dentedreality.com.au/2011/01/10/samurai-armor-2/ "11:38 am") 
jQuery(document).ready(function(){
var gmap\_mb4365f08d45347f6a5364eb2e3db7102 = {
positions : {
823 : new google.maps.LatLng( '-32.063', '115.9355' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb4365f08d45347f6a5364eb2e3db7102' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb4365f08d45347f6a5364eb2e3db7102.positions ) {
gmap\_mb4365f08d45347f6a5364eb2e3db7102.bounds.extend( gmap\_mb4365f08d45347f6a5364eb2e3db7102.positions[m] );
}
// Render markers
for ( var m in gmap\_mb4365f08d45347f6a5364eb2e3db7102.positions ) {
gmap\_mb4365f08d45347f6a5364eb2e3db7102.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb4365f08d45347f6a5364eb2e3db7102.map,
position : gmap\_mb4365f08d45347f6a5364eb2e3db7102.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb4365f08d45347f6a5364eb2e3db7102.map.setCenter( gmap\_mb4365f08d45347f6a5364eb2e3db7102.positions[823] );
});