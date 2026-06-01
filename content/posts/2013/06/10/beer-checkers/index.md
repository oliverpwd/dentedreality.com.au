---
title: Beer Checkers!
date: '2013-06-10T17:36:30+00:00'
format: image
service: flickr
tags:
- beer
- checkers
- game
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9437046275_dc88680a93_o.jpg?resize=607%2C452
---

[![Beer Checkers!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9437046275_dc88680a93_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/06/10/beer-checkers/) 
# [Beer Checkers!](http://dentedreality.com.au/2013/06/10/beer-checkers/)





* #[beer](http://dentedreality.com.au/tags/beer/)
* #[checkers](http://dentedreality.com.au/tags/checkers/)
* #[game](http://dentedreality.com.au/tags/game/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437046275/) [5:36 pm, June 10, 2013](http://dentedreality.com.au/2013/06/10/beer-checkers/ "5:36 pm") 
jQuery(document).ready(function(){
var gmap\_m848f6163ca4212794052d6703dbdefe7 = {
positions : {
917 : new google.maps.LatLng( '45.5225', '-122.678001' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m848f6163ca4212794052d6703dbdefe7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m848f6163ca4212794052d6703dbdefe7.positions ) {
gmap\_m848f6163ca4212794052d6703dbdefe7.bounds.extend( gmap\_m848f6163ca4212794052d6703dbdefe7.positions[m] );
}
// Render markers
for ( var m in gmap\_m848f6163ca4212794052d6703dbdefe7.positions ) {
gmap\_m848f6163ca4212794052d6703dbdefe7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m848f6163ca4212794052d6703dbdefe7.map,
position : gmap\_m848f6163ca4212794052d6703dbdefe7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m848f6163ca4212794052d6703dbdefe7.map.setCenter( gmap\_m848f6163ca4212794052d6703dbdefe7.positions[917] );
});