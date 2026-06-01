---
title: ''
date: '2013-12-19T13:54:40+00:00'
format: image
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/e19945f468de11e3a8f3123daafffadd_8.jpg?resize=640%2C640
---

[![W is for old WordPress buddies!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/e19945f468de11e3a8f3123daafffadd_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2013/12/19/w-is-for-old-wordpress-buddies/) 

W is for old WordPress buddies!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/iHS8jmCmN6/) [1:54 pm, December 19, 2013](http://dentedreality.com.au/2013/12/19/w-is-for-old-wordpress-buddies/ "1:54 pm") 
jQuery(document).ready(function(){
var gmap\_mc068242f321aa1c87e8e4c3e283a3aca = {
positions : {
959 : new google.maps.LatLng( '40.7443', '-73.9813' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc068242f321aa1c87e8e4c3e283a3aca' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc068242f321aa1c87e8e4c3e283a3aca.positions ) {
gmap\_mc068242f321aa1c87e8e4c3e283a3aca.bounds.extend( gmap\_mc068242f321aa1c87e8e4c3e283a3aca.positions[m] );
}
// Render markers
for ( var m in gmap\_mc068242f321aa1c87e8e4c3e283a3aca.positions ) {
gmap\_mc068242f321aa1c87e8e4c3e283a3aca.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc068242f321aa1c87e8e4c3e283a3aca.map,
position : gmap\_mc068242f321aa1c87e8e4c3e283a3aca.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc068242f321aa1c87e8e4c3e283a3aca.map.setCenter( gmap\_mc068242f321aa1c87e8e4c3e283a3aca.positions[959] );
});