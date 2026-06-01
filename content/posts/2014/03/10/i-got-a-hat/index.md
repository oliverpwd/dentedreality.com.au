---
title: I got a hat
date: '2014-03-10T09:10:54+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- hat
- me
- perth
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904701096_52f0e6a2a4_o.jpg?resize=607%2C809
---

[![I got a hat](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904701096_52f0e6a2a4_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2014/03/10/i-got-a-hat/) 
# [I got a hat](http://dentedreality.com.au/2014/03/10/i-got-a-hat/)

Perth, Mooloolaba and Melbourne





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[hat](http://dentedreality.com.au/tags/hat/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904701096/) [9:10 am, March 10, 2014](http://dentedreality.com.au/2014/03/10/i-got-a-hat/ "9:10 am") 
jQuery(document).ready(function(){
var gmap\_m3e0fcce98a0e491d568d3fbaed370b2c = {
positions : {
887 : new google.maps.LatLng( '-32.053317', '115.84655' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3e0fcce98a0e491d568d3fbaed370b2c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3e0fcce98a0e491d568d3fbaed370b2c.positions ) {
gmap\_m3e0fcce98a0e491d568d3fbaed370b2c.bounds.extend( gmap\_m3e0fcce98a0e491d568d3fbaed370b2c.positions[m] );
}
// Render markers
for ( var m in gmap\_m3e0fcce98a0e491d568d3fbaed370b2c.positions ) {
gmap\_m3e0fcce98a0e491d568d3fbaed370b2c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3e0fcce98a0e491d568d3fbaed370b2c.map,
position : gmap\_m3e0fcce98a0e491d568d3fbaed370b2c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3e0fcce98a0e491d568d3fbaed370b2c.map.setCenter( gmap\_m3e0fcce98a0e491d568d3fbaed370b2c.positions[887] );
});