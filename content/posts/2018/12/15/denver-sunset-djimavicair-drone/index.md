---
title: ''
date: '2018-12-15T09:34:13-06:00'
format: image
service: instagram
tags:
- djimavicair
- drone
latitude: '39.7604294'
longitude: '-104.9768295'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/12/14181956/46197484_378229706080745_7538663946960475711_n.jpg?resize=607%2C606&ssl=1
---

[![Denver Sunset. #djimavicair #drone](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/12/14181956/46197484_378229706080745_7538663946960475711_n.jpg?resize=607%2C606&ssl=1)](https://dentedreality.com.au/2018/12/15/denver-sunset-djimavicair-drone/) 

[![Denver Sunset. #djimavicair #drone](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/12/14181956/46197484_378229706080745_7538663946960475711_n.jpg?resize=607%2C606&ssl=1)](https://www.instagram.com/p/BrajOIAgAKH/)

Denver Sunset. #djimavicair #drone

39.7604294-104.9768295




* #[djimavicair](https://dentedreality.com.au/tags/djimavicair/)
* #[drone](https://dentedreality.com.au/tags/drone/)

Posted on [Instagram](https://www.instagram.com/p/BrajOIAgAKH/) [9:34 am, December 15, 2018](https://dentedreality.com.au/2018/12/15/denver-sunset-djimavicair-drone/ "9:34 am") 
jQuery(document).ready(function(){
var gmap\_m1cb3dae05c5a01a50d222185175afe39 = {
positions : {
881 : new google.maps.LatLng( '39.7604294', '-104.9768295' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1cb3dae05c5a01a50d222185175afe39' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1cb3dae05c5a01a50d222185175afe39.positions ) {
gmap\_m1cb3dae05c5a01a50d222185175afe39.bounds.extend( gmap\_m1cb3dae05c5a01a50d222185175afe39.positions[m] );
}
// Render markers
for ( var m in gmap\_m1cb3dae05c5a01a50d222185175afe39.positions ) {
gmap\_m1cb3dae05c5a01a50d222185175afe39.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1cb3dae05c5a01a50d222185175afe39.map,
position : gmap\_m1cb3dae05c5a01a50d222185175afe39.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1cb3dae05c5a01a50d222185175afe39.map.setCenter( gmap\_m1cb3dae05c5a01a50d222185175afe39.positions[881] );
});