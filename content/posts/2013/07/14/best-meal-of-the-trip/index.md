---
title: Best Meal of the Trip
date: '2013-07-14T13:10:38+00:00'
format: image
service: flickr
tags:
- costarica
- fish
- food
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440191170_7ddeef3720_o.jpg?resize=607%2C455
---

[![Best Meal of the Trip](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440191170_7ddeef3720_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/07/14/best-meal-of-the-trip/) 
# [Best Meal of the Trip](http://dentedreality.com.au/2013/07/14/best-meal-of-the-trip/)

Local steak and a fresh caught, whole-grilled fish.





* #[costarica](http://dentedreality.com.au/tags/costarica/)
* #[fish](http://dentedreality.com.au/tags/fish/)
* #[food](http://dentedreality.com.au/tags/food/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9440191170/) [1:10 pm, July 14, 2013](http://dentedreality.com.au/2013/07/14/best-meal-of-the-trip/ "1:10 pm") 
jQuery(document).ready(function(){
var gmap\_mf9571d9d8b00af2690922822fd36ff45 = {
positions : {
666 : new google.maps.LatLng( '9.880088', '-85.529825' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf9571d9d8b00af2690922822fd36ff45' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf9571d9d8b00af2690922822fd36ff45.positions ) {
gmap\_mf9571d9d8b00af2690922822fd36ff45.bounds.extend( gmap\_mf9571d9d8b00af2690922822fd36ff45.positions[m] );
}
// Render markers
for ( var m in gmap\_mf9571d9d8b00af2690922822fd36ff45.positions ) {
gmap\_mf9571d9d8b00af2690922822fd36ff45.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf9571d9d8b00af2690922822fd36ff45.map,
position : gmap\_mf9571d9d8b00af2690922822fd36ff45.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf9571d9d8b00af2690922822fd36ff45.map.setCenter( gmap\_mf9571d9d8b00af2690922822fd36ff45.positions[666] );
});