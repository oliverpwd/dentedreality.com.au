---
title: ''
date: '2015-03-22T15:41:26+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/03/11078606_472948602858449_1692194548_n.jpg?resize=640%2C640
---

[![By far my best 20 yard shooting yet. Slowly working my way up to better aim at distance.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/03/11078606_472948602858449_1692194548_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/03/22/by-far-my-best-20-yard-shooting-yet-slowly-working-my-way-up-to-better-aim-at-distance/) 

By far my best 20 yard shooting yet. Slowly working my way up to better aim at distance.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/0i6Gz6CmBO/) [3:41 pm, March 22, 2015](http://dentedreality.com.au/2015/03/22/by-far-my-best-20-yard-shooting-yet-slowly-working-my-way-up-to-better-aim-at-distance/ "3:41 pm") 
jQuery(document).ready(function(){
var gmap\_m3c4e0033b2820bdd1cd4fc1c2a2f55c6 = {
positions : {
315 : new google.maps.LatLng( '39.826967992', '-104.976756458' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3c4e0033b2820bdd1cd4fc1c2a2f55c6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3c4e0033b2820bdd1cd4fc1c2a2f55c6.positions ) {
gmap\_m3c4e0033b2820bdd1cd4fc1c2a2f55c6.bounds.extend( gmap\_m3c4e0033b2820bdd1cd4fc1c2a2f55c6.positions[m] );
}
// Render markers
for ( var m in gmap\_m3c4e0033b2820bdd1cd4fc1c2a2f55c6.positions ) {
gmap\_m3c4e0033b2820bdd1cd4fc1c2a2f55c6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3c4e0033b2820bdd1cd4fc1c2a2f55c6.map,
position : gmap\_m3c4e0033b2820bdd1cd4fc1c2a2f55c6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3c4e0033b2820bdd1cd4fc1c2a2f55c6.map.setCenter( gmap\_m3c4e0033b2820bdd1cd4fc1c2a2f55c6.positions[315] );
});