---
title: L’Opera
date: '2013-11-29T04:57:54+00:00'
format: image
service: flickr
tags:
- france
- paris
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900352556_37e91efc3e_o.jpg?resize=607%2C455
---

[![L'Opera](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900352556_37e91efc3e_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/29/lopera/) 
# [L’Opera](http://dentedreality.com.au/2013/11/29/lopera/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900352556/) [4:57 am, November 29, 2013](http://dentedreality.com.au/2013/11/29/lopera/ "4:57 am") 
jQuery(document).ready(function(){
var gmap\_m351835dc27c3626751ed34d5090e78e0 = {
positions : {
194 : new google.maps.LatLng( '48.871033', '2.332194' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m351835dc27c3626751ed34d5090e78e0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m351835dc27c3626751ed34d5090e78e0.positions ) {
gmap\_m351835dc27c3626751ed34d5090e78e0.bounds.extend( gmap\_m351835dc27c3626751ed34d5090e78e0.positions[m] );
}
// Render markers
for ( var m in gmap\_m351835dc27c3626751ed34d5090e78e0.positions ) {
gmap\_m351835dc27c3626751ed34d5090e78e0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m351835dc27c3626751ed34d5090e78e0.map,
position : gmap\_m351835dc27c3626751ed34d5090e78e0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m351835dc27c3626751ed34d5090e78e0.map.setCenter( gmap\_m351835dc27c3626751ed34d5090e78e0.positions[194] );
});