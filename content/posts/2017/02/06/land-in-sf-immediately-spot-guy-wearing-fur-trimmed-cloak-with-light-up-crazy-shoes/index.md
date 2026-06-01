---
title: ''
date: '2017-02-06T12:36:48+00:00'
format: image
service: instagram
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16464891_2094580644101566_3519487543135436800_n.jpg?fit=640%2C640
---

[![Land in SF, immediately spot guy wearing fur-trimmed cloak, with light-up crazy shoes.](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16464891_2094580644101566_3519487543135436800_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2017/02/06/land-in-sf-immediately-spot-guy-wearing-fur-trimmed-cloak-with-light-up-crazy-shoes/) 

Land in SF, immediately spot guy wearing fur-trimmed cloak, with light-up crazy shoes.





Posted on [Instagram](https://www.instagram.com/p/BQLp9CxjgAP/) [12:36 pm, February 6, 2017](http://dentedreality.com.au/2017/02/06/land-in-sf-immediately-spot-guy-wearing-fur-trimmed-cloak-with-light-up-crazy-shoes/ "12:36 pm") 
jQuery(document).ready(function(){
var gmap\_m9b9e0bd386b2a9affe78a3e1f1b489c8 = {
positions : {
232 : new google.maps.LatLng( '37.615608', '-122.389544' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9b9e0bd386b2a9affe78a3e1f1b489c8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9b9e0bd386b2a9affe78a3e1f1b489c8.positions ) {
gmap\_m9b9e0bd386b2a9affe78a3e1f1b489c8.bounds.extend( gmap\_m9b9e0bd386b2a9affe78a3e1f1b489c8.positions[m] );
}
// Render markers
for ( var m in gmap\_m9b9e0bd386b2a9affe78a3e1f1b489c8.positions ) {
gmap\_m9b9e0bd386b2a9affe78a3e1f1b489c8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9b9e0bd386b2a9affe78a3e1f1b489c8.map,
position : gmap\_m9b9e0bd386b2a9affe78a3e1f1b489c8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9b9e0bd386b2a9affe78a3e1f1b489c8.map.setCenter( gmap\_m9b9e0bd386b2a9affe78a3e1f1b489c8.positions[232] );
});