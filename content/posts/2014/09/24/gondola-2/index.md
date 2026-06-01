---
title: ''
date: '2014-09-24T17:40:45+00:00'
format: image
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10683802_694907130579022_1776375338_n.jpg?resize=640%2C640
---

[![Gondola](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10683802_694907130579022_1776375338_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/09/24/gondola-2/) 

Gondola





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/tWNeCcCmNi/) [5:40 pm, September 24, 2014](http://dentedreality.com.au/2014/09/24/gondola-2/ "5:40 pm") 
jQuery(document).ready(function(){
var gmap\_mb4d85b5dc5c6817aa2fe553e646b3997 = {
positions : {
250 : new google.maps.LatLng( '40.686056739', '-111.561702451' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb4d85b5dc5c6817aa2fe553e646b3997' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb4d85b5dc5c6817aa2fe553e646b3997.positions ) {
gmap\_mb4d85b5dc5c6817aa2fe553e646b3997.bounds.extend( gmap\_mb4d85b5dc5c6817aa2fe553e646b3997.positions[m] );
}
// Render markers
for ( var m in gmap\_mb4d85b5dc5c6817aa2fe553e646b3997.positions ) {
gmap\_mb4d85b5dc5c6817aa2fe553e646b3997.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb4d85b5dc5c6817aa2fe553e646b3997.map,
position : gmap\_mb4d85b5dc5c6817aa2fe553e646b3997.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb4d85b5dc5c6817aa2fe553e646b3997.map.setCenter( gmap\_mb4d85b5dc5c6817aa2fe553e646b3997.positions[250] );
});