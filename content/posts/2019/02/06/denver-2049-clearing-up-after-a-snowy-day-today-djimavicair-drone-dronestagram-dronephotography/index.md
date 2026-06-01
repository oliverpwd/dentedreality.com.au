---
title: ''
date: '2019-02-06T18:24:35-06:00'
format: image
service: instagram
tags:
- djimavicair
- drone
- dronephotography
- dronestagram
latitude: '39.7391'
longitude: '-104.9836'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/02/14181943/50481263_386356785261404_375162264198562190_n.jpg?resize=607%2C340&ssl=1
---

[![Denver 2049. Clearing up after a snowy day today. #djimavicair #drone #dronestagram #dronephotography](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/02/14181943/50481263_386356785261404_375162264198562190_n.jpg?resize=607%2C340&ssl=1)](https://dentedreality.com.au/2019/02/06/denver-2049-clearing-up-after-a-snowy-day-today-djimavicair-drone-dronestagram-dronephotography/) 

[![Denver 2049. Clearing up after a snowy day today. #djimavicair #drone #dronestagram #dronephotography](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/02/14181943/50481263_386356785261404_375162264198562190_n.jpg?resize=607%2C340&ssl=1)](https://www.instagram.com/p/Btj-DF_HamJ/)

Denver 2049. Clearing up after a snowy day today. #djimavicair #drone #dronestagram #dronephotography

39.7391-104.9836




* #[djimavicair](https://dentedreality.com.au/tags/djimavicair/)
* #[drone](https://dentedreality.com.au/tags/drone/)
* #[dronephotography](https://dentedreality.com.au/tags/dronephotography/)
* #[dronestagram](https://dentedreality.com.au/tags/dronestagram/)

Posted on [Instagram](https://www.instagram.com/p/Btj-DF_HamJ/) [6:24 pm, February 6, 2019](https://dentedreality.com.au/2019/02/06/denver-2049-clearing-up-after-a-snowy-day-today-djimavicair-drone-dronestagram-dronephotography/ "6:24 pm") 
jQuery(document).ready(function(){
var gmap\_m54ebb0e01a7dd6adc140ef024dc70b7e = {
positions : {
769 : new google.maps.LatLng( '39.7391', '-104.9836' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m54ebb0e01a7dd6adc140ef024dc70b7e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m54ebb0e01a7dd6adc140ef024dc70b7e.positions ) {
gmap\_m54ebb0e01a7dd6adc140ef024dc70b7e.bounds.extend( gmap\_m54ebb0e01a7dd6adc140ef024dc70b7e.positions[m] );
}
// Render markers
for ( var m in gmap\_m54ebb0e01a7dd6adc140ef024dc70b7e.positions ) {
gmap\_m54ebb0e01a7dd6adc140ef024dc70b7e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m54ebb0e01a7dd6adc140ef024dc70b7e.map,
position : gmap\_m54ebb0e01a7dd6adc140ef024dc70b7e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m54ebb0e01a7dd6adc140ef024dc70b7e.map.setCenter( gmap\_m54ebb0e01a7dd6adc140ef024dc70b7e.positions[769] );
});