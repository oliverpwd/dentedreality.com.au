---
title: ''
date: '2017-09-21T23:49:55-06:00'
format: image
service: instagram
latitude: '50.1122886'
longitude: '-122.9558218'
---

[![Mixmaster @scratchymonkey](https://scontent.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/21909403_1501179999976192_6795303058784911360_n.jpg)](https://dentedreality.com.au/2017/09/21/mixmaster-scratchymonkey/) 

[![Mixmaster @scratchymonkey](https://scontent.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/21909403_1501179999976192_6795303058784911360_n.jpg)](https://www.instagram.com/p/BZVQkR4BONu/)

Mixmaster @scratchymonkey

50.1122886-122.9558218




Posted on [Instagram](https://www.instagram.com/p/BZVQkR4BONu/) [11:49 pm, September 21, 2017](https://dentedreality.com.au/2017/09/21/mixmaster-scratchymonkey/ "11:49 pm") 
jQuery(document).ready(function(){
var gmap\_m1bde92a47f9d67f87c17ce909366ee13 = {
positions : {
281 : new google.maps.LatLng( '50.112288625037', '-122.95582178407' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1bde92a47f9d67f87c17ce909366ee13' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1bde92a47f9d67f87c17ce909366ee13.positions ) {
gmap\_m1bde92a47f9d67f87c17ce909366ee13.bounds.extend( gmap\_m1bde92a47f9d67f87c17ce909366ee13.positions[m] );
}
// Render markers
for ( var m in gmap\_m1bde92a47f9d67f87c17ce909366ee13.positions ) {
gmap\_m1bde92a47f9d67f87c17ce909366ee13.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1bde92a47f9d67f87c17ce909366ee13.map,
position : gmap\_m1bde92a47f9d67f87c17ce909366ee13.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1bde92a47f9d67f87c17ce909366ee13.map.setCenter( gmap\_m1bde92a47f9d67f87c17ce909366ee13.positions[281] );
});