---
title: ''
date: '2015-02-01T16:34:15+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/10950581_373266622856022_1233261856_n.jpg?resize=640%2C640
---

[![First day with the new bow. Nice grouping except for that stray one up top.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/10950581_373266622856022_1233261856_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/02/01/first-day-with-the-new-bow-nice-grouping-except-for-that-stray-one-up-top/) 

First day with the new bow. Nice grouping except for that stray one up top.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/yk8EQBimEP/) [4:34 pm, February 1, 2015](http://dentedreality.com.au/2015/02/01/first-day-with-the-new-bow-nice-grouping-except-for-that-stray-one-up-top/ "4:34 pm") 
jQuery(document).ready(function(){
var gmap\_md4dd5faf9e6730f99c44c680018d333b = {
positions : {
700 : new google.maps.LatLng( '39.780011927', '-104.915659679' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md4dd5faf9e6730f99c44c680018d333b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md4dd5faf9e6730f99c44c680018d333b.positions ) {
gmap\_md4dd5faf9e6730f99c44c680018d333b.bounds.extend( gmap\_md4dd5faf9e6730f99c44c680018d333b.positions[m] );
}
// Render markers
for ( var m in gmap\_md4dd5faf9e6730f99c44c680018d333b.positions ) {
gmap\_md4dd5faf9e6730f99c44c680018d333b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md4dd5faf9e6730f99c44c680018d333b.map,
position : gmap\_md4dd5faf9e6730f99c44c680018d333b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md4dd5faf9e6730f99c44c680018d333b.map.setCenter( gmap\_md4dd5faf9e6730f99c44c680018d333b.positions[700] );
});