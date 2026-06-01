---
title: Word Processor
date: '2010-05-12T07:53:05+00:00'
format: image
service: flickr
tags:
- typewriter
- wordprocessor
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/05/4746455397_6cfef5c218_o.jpg?resize=607%2C455
---

[![Word Processor](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/05/4746455397_6cfef5c218_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/05/12/word-processor/) 
# [Word Processor](http://dentedreality.com.au/2010/05/12/word-processor/)





* #[typewriter](http://dentedreality.com.au/tags/typewriter/)
* #[wordprocessor](http://dentedreality.com.au/tags/wordprocessor/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4746455397/) [7:53 am, May 12, 2010](http://dentedreality.com.au/2010/05/12/word-processor/ "7:53 am") 
jQuery(document).ready(function(){
var gmap\_m718e34c7c602a27ac2b081cd3ca7c781 = {
positions : {
525 : new google.maps.LatLng( '37.790833', '-122.417834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m718e34c7c602a27ac2b081cd3ca7c781' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m718e34c7c602a27ac2b081cd3ca7c781.positions ) {
gmap\_m718e34c7c602a27ac2b081cd3ca7c781.bounds.extend( gmap\_m718e34c7c602a27ac2b081cd3ca7c781.positions[m] );
}
// Render markers
for ( var m in gmap\_m718e34c7c602a27ac2b081cd3ca7c781.positions ) {
gmap\_m718e34c7c602a27ac2b081cd3ca7c781.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m718e34c7c602a27ac2b081cd3ca7c781.map,
position : gmap\_m718e34c7c602a27ac2b081cd3ca7c781.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m718e34c7c602a27ac2b081cd3ca7c781.map.setCenter( gmap\_m718e34c7c602a27ac2b081cd3ca7c781.positions[525] );
});