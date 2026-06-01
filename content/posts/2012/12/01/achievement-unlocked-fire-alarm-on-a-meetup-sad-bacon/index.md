---
title: ''
date: '2012-12-01T11:49:26+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/af8e31983bce11e2b62322000a9f12da_7.jpg?resize=607%2C607
---

[![Achievement Unlocked: Fire alarm on a meetup. Sad bacon.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/af8e31983bce11e2b62322000a9f12da_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/12/01/achievement-unlocked-fire-alarm-on-a-meetup-sad-bacon/) 

Achievement Unlocked: Fire alarm on a meetup. Sad bacon.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/SsxS2ZimE_/) [11:49 am, December 1, 2012](http://dentedreality.com.au/2012/12/01/achievement-unlocked-fire-alarm-on-a-meetup-sad-bacon/ "11:49 am") 
jQuery(document).ready(function(){
var gmap\_m6783e2907a1a041f15867361814e2a54 = {
positions : {
938 : new google.maps.LatLng( '29.93354161', '-90.098043001' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6783e2907a1a041f15867361814e2a54' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6783e2907a1a041f15867361814e2a54.positions ) {
gmap\_m6783e2907a1a041f15867361814e2a54.bounds.extend( gmap\_m6783e2907a1a041f15867361814e2a54.positions[m] );
}
// Render markers
for ( var m in gmap\_m6783e2907a1a041f15867361814e2a54.positions ) {
gmap\_m6783e2907a1a041f15867361814e2a54.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6783e2907a1a041f15867361814e2a54.map,
position : gmap\_m6783e2907a1a041f15867361814e2a54.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6783e2907a1a041f15867361814e2a54.map.setCenter( gmap\_m6783e2907a1a041f15867361814e2a54.positions[938] );
});