---
title: ''
date: '2019-12-11T16:15:05-07:00'
format: image
service: instagram
latitude: '33.7909265'
longitude: '-84.3795191'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/12/11162456/79372039_358748784976778_277551687613942849_n.jpg
---

[![Good evening, Atlanta.](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/12/11162456/79372039_358748784976778_277551687613942849_n.jpg)](https://dentedreality.com.au/2019/12/11/good-evening-atlanta/) 

![Good evening, Atlanta.](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/12/11162456/79372039_358748784976778_277551687613942849_n.jpg)

[![Good evening, Atlanta.](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/79372039_358748784976778_277551687613942849_n.jpg?_nc_ht=scontent.cdninstagram.com&oh=8126ab80e7c7debb456b66b1a8fadb1b&oe=5EB36770)![Good evening, Atlanta.](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/79372039_358748784976778_277551687613942849_n.jpg?_nc_ht=scontent.cdninstagram.com&oh=8126ab80e7c7debb456b66b1a8fadb1b&oe=5EB36770)](https://www.instagram.com/p/B580EFSpQEL/)

Good evening, Atlanta.

33.7909265-84.3795191




Posted on [Instagram](https://www.instagram.com/p/B580EFSpQEL/) [4:15 pm, December 11, 2019](https://dentedreality.com.au/2019/12/11/good-evening-atlanta/ "4:15 pm") 
jQuery(document).ready(function(){
var gmap\_m911e5879fe057e7f607eb32aea3d6832 = {
positions : {
259 : new google.maps.LatLng( '33.7909265', '-84.3795191' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m911e5879fe057e7f607eb32aea3d6832' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m911e5879fe057e7f607eb32aea3d6832.positions ) {
gmap\_m911e5879fe057e7f607eb32aea3d6832.bounds.extend( gmap\_m911e5879fe057e7f607eb32aea3d6832.positions[m] );
}
// Render markers
for ( var m in gmap\_m911e5879fe057e7f607eb32aea3d6832.positions ) {
gmap\_m911e5879fe057e7f607eb32aea3d6832.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m911e5879fe057e7f607eb32aea3d6832.map,
position : gmap\_m911e5879fe057e7f607eb32aea3d6832.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m911e5879fe057e7f607eb32aea3d6832.map.setCenter( gmap\_m911e5879fe057e7f607eb32aea3d6832.positions[259] );
});