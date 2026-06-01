---
title: Inside the island
date: '2006-12-28T19:07:11+00:00'
format: image
service: flickr
tags:
- island
- lagoon
- lookingup
- phuket
- thailand
- thailand06
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348096167_eba882e393_o.jpg?resize=607%2C455
---

[![Inside the island](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348096167_eba882e393_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/28/inside-the-island/) 
# [Inside the island](http://dentedreality.com.au/2006/12/28/inside-the-island/)

This was taken from inside one of the islands, looking up. They’re hollow and they have lagoons inside them.





* #[island](http://dentedreality.com.au/tags/island/)
* #[lagoon](http://dentedreality.com.au/tags/lagoon/)
* #[lookingup](http://dentedreality.com.au/tags/lookingup/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348096167/) [7:07 pm, December 28, 2006](http://dentedreality.com.au/2006/12/28/inside-the-island/ "7:07 pm") 
jQuery(document).ready(function(){
var gmap\_m3ee687a7ac205b85c55f342753f38f1f = {
positions : {
284 : new google.maps.LatLng( '8.095005', '98.457927' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3ee687a7ac205b85c55f342753f38f1f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3ee687a7ac205b85c55f342753f38f1f.positions ) {
gmap\_m3ee687a7ac205b85c55f342753f38f1f.bounds.extend( gmap\_m3ee687a7ac205b85c55f342753f38f1f.positions[m] );
}
// Render markers
for ( var m in gmap\_m3ee687a7ac205b85c55f342753f38f1f.positions ) {
gmap\_m3ee687a7ac205b85c55f342753f38f1f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3ee687a7ac205b85c55f342753f38f1f.map,
position : gmap\_m3ee687a7ac205b85c55f342753f38f1f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3ee687a7ac205b85c55f342753f38f1f.map.setCenter( gmap\_m3ee687a7ac205b85c55f342753f38f1f.positions[284] );
});