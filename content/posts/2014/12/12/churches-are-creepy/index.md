---
title: ''
date: '2014-12-12T07:48:13+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10838844_524122141024509_810872369_n.jpg?resize=640%2C640
---

[![Churches are creepy.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10838844_524122141024509_810872369_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/12/12/churches-are-creepy/) 

Churches are creepy.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/wgrUzfCmFR/) [7:48 am, December 12, 2014](http://dentedreality.com.au/2014/12/12/churches-are-creepy/ "7:48 am") 
jQuery(document).ready(function(){
var gmap\_m38a8e363d94befd5941c0c6bfdb46f91 = {
positions : {
815 : new google.maps.LatLng( '41.893333333', '12.483055556' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m38a8e363d94befd5941c0c6bfdb46f91' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m38a8e363d94befd5941c0c6bfdb46f91.positions ) {
gmap\_m38a8e363d94befd5941c0c6bfdb46f91.bounds.extend( gmap\_m38a8e363d94befd5941c0c6bfdb46f91.positions[m] );
}
// Render markers
for ( var m in gmap\_m38a8e363d94befd5941c0c6bfdb46f91.positions ) {
gmap\_m38a8e363d94befd5941c0c6bfdb46f91.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m38a8e363d94befd5941c0c6bfdb46f91.map,
position : gmap\_m38a8e363d94befd5941c0c6bfdb46f91.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m38a8e363d94befd5941c0c6bfdb46f91.map.setCenter( gmap\_m38a8e363d94befd5941c0c6bfdb46f91.positions[815] );
});