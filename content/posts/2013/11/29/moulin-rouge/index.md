---
title: Moulin Rouge
date: '2013-11-29T06:27:05+00:00'
format: image
service: flickr
tags:
- france
- moulinrouge
- paris
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900356796_56452a4a25_o.jpg?fit=1500%2C1500
---

[![Moulin Rouge](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900356796_56452a4a25_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/11/29/moulin-rouge/) 
# [Moulin Rouge](http://dentedreality.com.au/2013/11/29/moulin-rouge/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[moulinrouge](http://dentedreality.com.au/tags/moulinrouge/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900356796/) [6:27 am, November 29, 2013](http://dentedreality.com.au/2013/11/29/moulin-rouge/ "6:27 am") 
jQuery(document).ready(function(){
var gmap\_m1919451844cbd01c92edaeb7108cd6c5 = {
positions : {
99 : new google.maps.LatLng( '48.88348', '2.332099' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1919451844cbd01c92edaeb7108cd6c5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1919451844cbd01c92edaeb7108cd6c5.positions ) {
gmap\_m1919451844cbd01c92edaeb7108cd6c5.bounds.extend( gmap\_m1919451844cbd01c92edaeb7108cd6c5.positions[m] );
}
// Render markers
for ( var m in gmap\_m1919451844cbd01c92edaeb7108cd6c5.positions ) {
gmap\_m1919451844cbd01c92edaeb7108cd6c5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1919451844cbd01c92edaeb7108cd6c5.map,
position : gmap\_m1919451844cbd01c92edaeb7108cd6c5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1919451844cbd01c92edaeb7108cd6c5.map.setCenter( gmap\_m1919451844cbd01c92edaeb7108cd6c5.positions[99] );
});