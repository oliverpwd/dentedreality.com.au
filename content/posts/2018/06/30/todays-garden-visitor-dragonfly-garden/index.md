---
title: ''
date: '2018-06-30T09:42:23-06:00'
format: image
service: instagram
tags:
- dragonfly
- garden
latitude: '39.7572'
longitude: '-104.967'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182135/35459244_1249620685173794_3960946697252634624_n.jpg?resize=607%2C607&ssl=1
---

[![Today's garden visitor #dragonfly #garden](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182135/35459244_1249620685173794_3960946697252634624_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/06/30/todays-garden-visitor-dragonfly-garden/) 

[![Today's garden visitor #dragonfly #garden](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182135/35459244_1249620685173794_3960946697252634624_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/Bkp3vetFktR/)

Today’s garden visitor #dragonfly #garden

39.7572-104.967




* #[dragonfly](https://dentedreality.com.au/tags/dragonfly/)
* #[garden](https://dentedreality.com.au/tags/garden/)

Posted on [Instagram](https://www.instagram.com/p/Bkp3vetFktR/) [9:42 am, June 30, 2018](https://dentedreality.com.au/2018/06/30/todays-garden-visitor-dragonfly-garden/ "9:42 am") 
jQuery(document).ready(function(){
var gmap\_ma3ea82f81e27944ceaf9b6801fe8e18c = {
positions : {
776 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma3ea82f81e27944ceaf9b6801fe8e18c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma3ea82f81e27944ceaf9b6801fe8e18c.positions ) {
gmap\_ma3ea82f81e27944ceaf9b6801fe8e18c.bounds.extend( gmap\_ma3ea82f81e27944ceaf9b6801fe8e18c.positions[m] );
}
// Render markers
for ( var m in gmap\_ma3ea82f81e27944ceaf9b6801fe8e18c.positions ) {
gmap\_ma3ea82f81e27944ceaf9b6801fe8e18c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma3ea82f81e27944ceaf9b6801fe8e18c.map,
position : gmap\_ma3ea82f81e27944ceaf9b6801fe8e18c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma3ea82f81e27944ceaf9b6801fe8e18c.map.setCenter( gmap\_ma3ea82f81e27944ceaf9b6801fe8e18c.positions[776] );
});