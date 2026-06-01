---
title: Rooftop View
date: '2012-10-24T16:21:35+00:00'
format: image
service: flickr
tags:
- city
- lights
- newyork
- roof
- view
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8244797749_5b124ce77f_o.jpg?resize=607%2C813
---

[![Rooftop View](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8244797749_5b124ce77f_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/10/24/rooftop-view/) 
# [Rooftop View](http://dentedreality.com.au/2012/10/24/rooftop-view/)





* #[city](http://dentedreality.com.au/tags/city/)
* #[lights](http://dentedreality.com.au/tags/lights/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[roof](http://dentedreality.com.au/tags/roof/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8244797749/) [4:21 pm, October 24, 2012](http://dentedreality.com.au/2012/10/24/rooftop-view/ "4:21 pm") 
jQuery(document).ready(function(){
var gmap\_ma8b4bd400ebf878c6d8a886930e010ae = {
positions : {
896 : new google.maps.LatLng( '40.725833', '-73.996167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma8b4bd400ebf878c6d8a886930e010ae' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma8b4bd400ebf878c6d8a886930e010ae.positions ) {
gmap\_ma8b4bd400ebf878c6d8a886930e010ae.bounds.extend( gmap\_ma8b4bd400ebf878c6d8a886930e010ae.positions[m] );
}
// Render markers
for ( var m in gmap\_ma8b4bd400ebf878c6d8a886930e010ae.positions ) {
gmap\_ma8b4bd400ebf878c6d8a886930e010ae.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma8b4bd400ebf878c6d8a886930e010ae.map,
position : gmap\_ma8b4bd400ebf878c6d8a886930e010ae.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma8b4bd400ebf878c6d8a886930e010ae.map.setCenter( gmap\_ma8b4bd400ebf878c6d8a886930e010ae.positions[896] );
});