---
title: ''
date: '2015-09-23T15:58:57-06:00'
format: image
service: instagram
tags:
- car
- vintage
- vintagecar
latitude: '39.8230705'
longitude: '-105.1677094'
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/09/11881902_940367906019792_539656558_n.jpg?resize=640%2C640
---

[![Stanley Steamer #car #vintagecar #vintage](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/09/11881902_940367906019792_539656558_n.jpg?resize=640%2C640)](https://dentedreality.com.au/2015/09/23/stanley-steamer-car-vintagecar-vintage/) 

[![Stanley Steamer #car #vintagecar #vintage](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/09/11881902_940367906019792_539656558_n.jpg?resize=640%2C640)](https://instagram.com/p/7_TK9UCmCX/)

Stanley Steamer #car #vintagecar #vintage

39.8230705-105.1677094




* #[car](https://dentedreality.com.au/tags/car/)
* #[vintage](https://dentedreality.com.au/tags/vintage/)
* #[vintagecar](https://dentedreality.com.au/tags/vintagecar/)

Posted on [Instagram](https://instagram.com/p/7_TK9UCmCX/) [3:58 pm, September 23, 2015](https://dentedreality.com.au/2015/09/23/stanley-steamer-car-vintagecar-vintage/ "3:58 pm") 
jQuery(document).ready(function(){
var gmap\_m9fd8075be1e91c1f37f246b4b2763859 = {
positions : {
344 : new google.maps.LatLng( '39.8230705', '-105.1677094' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9fd8075be1e91c1f37f246b4b2763859' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9fd8075be1e91c1f37f246b4b2763859.positions ) {
gmap\_m9fd8075be1e91c1f37f246b4b2763859.bounds.extend( gmap\_m9fd8075be1e91c1f37f246b4b2763859.positions[m] );
}
// Render markers
for ( var m in gmap\_m9fd8075be1e91c1f37f246b4b2763859.positions ) {
gmap\_m9fd8075be1e91c1f37f246b4b2763859.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9fd8075be1e91c1f37f246b4b2763859.map,
position : gmap\_m9fd8075be1e91c1f37f246b4b2763859.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9fd8075be1e91c1f37f246b4b2763859.map.setCenter( gmap\_m9fd8075be1e91c1f37f246b4b2763859.positions[344] );
});