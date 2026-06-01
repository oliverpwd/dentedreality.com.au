---
title: ''
date: '2017-02-06T12:59:24+00:00'
format: image
service: instagram
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16585001_1264428986956144_5396322177710555136_n.jpg?fit=640%2C640
---

[![True Love.](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16585001_1264428986956144_5396322177710555136_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2017/02/06/true-love/) 

True Love.





Posted on [Instagram](https://www.instagram.com/p/BQLsiq2jp3w/) [12:59 pm, February 6, 2017](http://dentedreality.com.au/2017/02/06/true-love/ "12:59 pm") 
jQuery(document).ready(function(){
var gmap\_m9c5296f4ac1151564c55d7889f59c66c = {
positions : {
340 : new google.maps.LatLng( '37.760428907277', '-122.41928487582' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9c5296f4ac1151564c55d7889f59c66c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9c5296f4ac1151564c55d7889f59c66c.positions ) {
gmap\_m9c5296f4ac1151564c55d7889f59c66c.bounds.extend( gmap\_m9c5296f4ac1151564c55d7889f59c66c.positions[m] );
}
// Render markers
for ( var m in gmap\_m9c5296f4ac1151564c55d7889f59c66c.positions ) {
gmap\_m9c5296f4ac1151564c55d7889f59c66c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9c5296f4ac1151564c55d7889f59c66c.map,
position : gmap\_m9c5296f4ac1151564c55d7889f59c66c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9c5296f4ac1151564c55d7889f59c66c.map.setCenter( gmap\_m9c5296f4ac1151564c55d7889f59c66c.positions[340] );
});