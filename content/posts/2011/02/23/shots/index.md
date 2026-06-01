---
title: Shots!
date: '2011-02-23T18:43:02+00:00'
format: image
service: flickr
tags:
- newyork
- newyorkcity
- NYC
- tequila
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802060605_f9b13e40cf_o.jpg?resize=607%2C452
---

[![Shots!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802060605_f9b13e40cf_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/02/23/shots/) 
# [Shots!](http://dentedreality.com.au/2011/02/23/shots/)





* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[newyorkcity](http://dentedreality.com.au/tags/newyorkcity/)
* #[NYC](http://dentedreality.com.au/tags/nyc/)
* #[tequila](http://dentedreality.com.au/tags/tequila/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802060605/) [6:43 pm, February 23, 2011](http://dentedreality.com.au/2011/02/23/shots/ "6:43 pm") 
jQuery(document).ready(function(){
var gmap\_m614d069290d716ddd86117372e9cbe31 = {
positions : {
955 : new google.maps.LatLng( '40.759333', '-73.982667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m614d069290d716ddd86117372e9cbe31' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m614d069290d716ddd86117372e9cbe31.positions ) {
gmap\_m614d069290d716ddd86117372e9cbe31.bounds.extend( gmap\_m614d069290d716ddd86117372e9cbe31.positions[m] );
}
// Render markers
for ( var m in gmap\_m614d069290d716ddd86117372e9cbe31.positions ) {
gmap\_m614d069290d716ddd86117372e9cbe31.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m614d069290d716ddd86117372e9cbe31.map,
position : gmap\_m614d069290d716ddd86117372e9cbe31.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m614d069290d716ddd86117372e9cbe31.map.setCenter( gmap\_m614d069290d716ddd86117372e9cbe31.positions[955] );
});