---
title: Last Ferry Out of Town
date: '2011-11-25T11:54:48+00:00'
format: image
service: flickr
tags:
- angelisland
- california
- camping
- outdoors
- sanfrancisco
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6958318761_7971df4192_o.jpg?resize=607%2C452
---

[![Last Ferry Out of Town](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6958318761_7971df4192_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/11/25/last-ferry-out-of-town/) 
# [Last Ferry Out of Town](http://dentedreality.com.au/2011/11/25/last-ferry-out-of-town/)

There goes the last ferry for the day. I guess we’re stuck here for the night!





* #[angelisland](http://dentedreality.com.au/tags/angelisland/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[camping](http://dentedreality.com.au/tags/camping/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958318761/) [11:54 am, November 25, 2011](http://dentedreality.com.au/2011/11/25/last-ferry-out-of-town/ "11:54 am") 
jQuery(document).ready(function(){
var gmap\_m47a2573e6face6e4a749842221f72bd1 = {
positions : {
90 : new google.maps.LatLng( '37.868833', '-122.432667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m47a2573e6face6e4a749842221f72bd1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m47a2573e6face6e4a749842221f72bd1.positions ) {
gmap\_m47a2573e6face6e4a749842221f72bd1.bounds.extend( gmap\_m47a2573e6face6e4a749842221f72bd1.positions[m] );
}
// Render markers
for ( var m in gmap\_m47a2573e6face6e4a749842221f72bd1.positions ) {
gmap\_m47a2573e6face6e4a749842221f72bd1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m47a2573e6face6e4a749842221f72bd1.map,
position : gmap\_m47a2573e6face6e4a749842221f72bd1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m47a2573e6face6e4a749842221f72bd1.map.setCenter( gmap\_m47a2573e6face6e4a749842221f72bd1.positions[90] );
});