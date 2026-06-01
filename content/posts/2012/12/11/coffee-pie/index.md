---
title: Coffee + Pie
date: '2012-12-11T11:06:19+00:00'
format: image
tags:
- coffee
- pie
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8460375900_926384024c_o.jpg?resize=607%2C452
---

[![Coffee + Pie](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8460375900_926384024c_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/12/11/coffee-pie/) 
# [Coffee + Pie](http://dentedreality.com.au/2012/12/11/coffee-pie/)

At Four and Twenty Blackbirds.





* #[coffee](http://dentedreality.com.au/tags/coffee/)
* #[pie](http://dentedreality.com.au/tags/pie/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460375900/) [11:06 am, December 11, 2012](http://dentedreality.com.au/2012/12/11/coffee-pie/ "11:06 am") 
jQuery(document).ready(function(){
var gmap\_m267dd2c13ddb51f99955ab10ab648071 = {
positions : {
653 : new google.maps.LatLng( '40.672', '-73.9905' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m267dd2c13ddb51f99955ab10ab648071' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m267dd2c13ddb51f99955ab10ab648071.positions ) {
gmap\_m267dd2c13ddb51f99955ab10ab648071.bounds.extend( gmap\_m267dd2c13ddb51f99955ab10ab648071.positions[m] );
}
// Render markers
for ( var m in gmap\_m267dd2c13ddb51f99955ab10ab648071.positions ) {
gmap\_m267dd2c13ddb51f99955ab10ab648071.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m267dd2c13ddb51f99955ab10ab648071.map,
position : gmap\_m267dd2c13ddb51f99955ab10ab648071.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m267dd2c13ddb51f99955ab10ab648071.map.setCenter( gmap\_m267dd2c13ddb51f99955ab10ab648071.positions[653] );
});