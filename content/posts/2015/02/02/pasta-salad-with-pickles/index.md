---
title: ''
date: '2015-02-02T12:54:00+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/10684110_1535326656732445_751057934_n.jpg?resize=640%2C640
---

[![Pasta salad with pickles.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/10684110_1535326656732445_751057934_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/02/02/pasta-salad-with-pickles/) 

Pasta salad with pickles.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/ynHp-_imGn/) [12:54 pm, February 2, 2015](http://dentedreality.com.au/2015/02/02/pasta-salad-with-pickles/ "12:54 pm") 
jQuery(document).ready(function(){
var gmap\_mc4cae7e0c9ad806f22258a69c135afaf = {
positions : {
114 : new google.maps.LatLng( '39.734745', '-104.97863' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc4cae7e0c9ad806f22258a69c135afaf' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc4cae7e0c9ad806f22258a69c135afaf.positions ) {
gmap\_mc4cae7e0c9ad806f22258a69c135afaf.bounds.extend( gmap\_mc4cae7e0c9ad806f22258a69c135afaf.positions[m] );
}
// Render markers
for ( var m in gmap\_mc4cae7e0c9ad806f22258a69c135afaf.positions ) {
gmap\_mc4cae7e0c9ad806f22258a69c135afaf.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc4cae7e0c9ad806f22258a69c135afaf.map,
position : gmap\_mc4cae7e0c9ad806f22258a69c135afaf.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc4cae7e0c9ad806f22258a69c135afaf.map.setCenter( gmap\_mc4cae7e0c9ad806f22258a69c135afaf.positions[114] );
});