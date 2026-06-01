---
title: ''
date: '2017-07-02T09:19:36-06:00'
format: image
service: instagram
tags:
- fjallravenclassicusa
- nofilter
latitude: '39.4864'
longitude: '-106.044'
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/07/19534695_249786042186927_4156690879739854848_n.jpg?fit=640%2C640&ssl=1
---

[![#fjallravenclassicusa views. #nofilter](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/07/19534695_249786042186927_4156690879739854848_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/07/02/fjallravenclassicusa-views-nofilter/) 

[![#fjallravenclassicusa views. #nofilter](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/07/19534695_249786042186927_4156690879739854848_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BWDIlAQBWMX/)

#fjallravenclassicusa views. #nofilter

39.4864-106.044




* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)
* #[nofilter](https://dentedreality.com.au/tags/nofilter/)

Posted on [Instagram](https://www.instagram.com/p/BWDIlAQBWMX/) [9:19 am, July 2, 2017](https://dentedreality.com.au/2017/07/02/fjallravenclassicusa-views-nofilter/ "9:19 am") 
jQuery(document).ready(function(){
var gmap\_m78a595dd735df3389dd8a73725a673ab = {
positions : {
274 : new google.maps.LatLng( '39.4864', '-106.044' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m78a595dd735df3389dd8a73725a673ab' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m78a595dd735df3389dd8a73725a673ab.positions ) {
gmap\_m78a595dd735df3389dd8a73725a673ab.bounds.extend( gmap\_m78a595dd735df3389dd8a73725a673ab.positions[m] );
}
// Render markers
for ( var m in gmap\_m78a595dd735df3389dd8a73725a673ab.positions ) {
gmap\_m78a595dd735df3389dd8a73725a673ab.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m78a595dd735df3389dd8a73725a673ab.map,
position : gmap\_m78a595dd735df3389dd8a73725a673ab.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m78a595dd735df3389dd8a73725a673ab.map.setCenter( gmap\_m78a595dd735df3389dd8a73725a673ab.positions[274] );
});