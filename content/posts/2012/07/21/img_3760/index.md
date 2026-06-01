---
title: IMG_3760
date: '2012-07-21T13:46:43+00:00'
format: image
service: flickr
tags:
- battleofthebraces
- hackathon
- php
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/07/8244713311_42d9448efb_o.jpg?resize=607%2C813
---

[![IMG_3760](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/07/8244713311_42d9448efb_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/07/21/img_3760/) 
# [IMG\_3760](http://dentedreality.com.au/2012/07/21/img_3760/)





* #[battleofthebraces](http://dentedreality.com.au/tags/battleofthebraces/)
* #[hackathon](http://dentedreality.com.au/tags/hackathon/)
* #[php](http://dentedreality.com.au/tags/php/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8244713311/) [1:46 pm, July 21, 2012](http://dentedreality.com.au/2012/07/21/img_3760/ "1:46 pm") 
jQuery(document).ready(function(){
var gmap\_m35e62350e5d3063d1ff7d4912a0e6219 = {
positions : {
262 : new google.maps.LatLng( '40.670166', '-73.989167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m35e62350e5d3063d1ff7d4912a0e6219' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m35e62350e5d3063d1ff7d4912a0e6219.positions ) {
gmap\_m35e62350e5d3063d1ff7d4912a0e6219.bounds.extend( gmap\_m35e62350e5d3063d1ff7d4912a0e6219.positions[m] );
}
// Render markers
for ( var m in gmap\_m35e62350e5d3063d1ff7d4912a0e6219.positions ) {
gmap\_m35e62350e5d3063d1ff7d4912a0e6219.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m35e62350e5d3063d1ff7d4912a0e6219.map,
position : gmap\_m35e62350e5d3063d1ff7d4912a0e6219.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m35e62350e5d3063d1ff7d4912a0e6219.map.setCenter( gmap\_m35e62350e5d3063d1ff7d4912a0e6219.positions[262] );
});