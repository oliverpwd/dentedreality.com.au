---
title: ''
date: '2012-01-28T23:46:13+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/c9f7c49e4a2b11e1a87612313804ec91_7.jpg?resize=607%2C607
---

[![Yeah that's right. Steak and jalepeno Mac n cheese](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/c9f7c49e4a2b11e1a87612313804ec91_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/01/28/yeah-thats-right-steak-and-jalepeno-mac-n-cheese/) 

Yeah that’s right. Steak and jalepeno Mac n cheese





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/ltxHt/) [11:46 pm, January 28, 2012](http://dentedreality.com.au/2012/01/28/yeah-thats-right-steak-and-jalepeno-mac-n-cheese/ "11:46 pm") 
jQuery(document).ready(function(){
var gmap\_mebd22f7b1d236e29b277ef223194f1b6 = {
positions : {
955 : new google.maps.LatLng( '37.75134', '-122.4165' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mebd22f7b1d236e29b277ef223194f1b6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mebd22f7b1d236e29b277ef223194f1b6.positions ) {
gmap\_mebd22f7b1d236e29b277ef223194f1b6.bounds.extend( gmap\_mebd22f7b1d236e29b277ef223194f1b6.positions[m] );
}
// Render markers
for ( var m in gmap\_mebd22f7b1d236e29b277ef223194f1b6.positions ) {
gmap\_mebd22f7b1d236e29b277ef223194f1b6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mebd22f7b1d236e29b277ef223194f1b6.map,
position : gmap\_mebd22f7b1d236e29b277ef223194f1b6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mebd22f7b1d236e29b277ef223194f1b6.map.setCenter( gmap\_mebd22f7b1d236e29b277ef223194f1b6.positions[955] );
});