---
title: ''
date: '2017-07-02T09:23:24+00:00'
format: image
service: instagram
tags:
- fjallravenclassicusa
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/07/19624561_321772208259646_2112618331851718656_n.jpg?fit=640%2C640&ssl=1
---

[![Icy ascent #fjallravenclassicusa](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/07/19624561_321772208259646_2112618331851718656_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/07/02/icy-ascent-fjallravenclassicusa/) 

[![Icy ascent #fjallravenclassicusa](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/07/19624561_321772208259646_2112618331851718656_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BWDJA6Xh7Zh/)

Icy ascent #fjallravenclassicusa





* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BWDJA6Xh7Zh/) [9:23 am, July 2, 2017](https://dentedreality.com.au/2017/07/02/icy-ascent-fjallravenclassicusa/ "9:23 am") 
jQuery(document).ready(function(){
var gmap\_m851f816329592eb12ca5174f5673cca0 = {
positions : {
45 : new google.maps.LatLng( '39.4938756', '-106.111132' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m851f816329592eb12ca5174f5673cca0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m851f816329592eb12ca5174f5673cca0.positions ) {
gmap\_m851f816329592eb12ca5174f5673cca0.bounds.extend( gmap\_m851f816329592eb12ca5174f5673cca0.positions[m] );
}
// Render markers
for ( var m in gmap\_m851f816329592eb12ca5174f5673cca0.positions ) {
gmap\_m851f816329592eb12ca5174f5673cca0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m851f816329592eb12ca5174f5673cca0.map,
position : gmap\_m851f816329592eb12ca5174f5673cca0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m851f816329592eb12ca5174f5673cca0.map.setCenter( gmap\_m851f816329592eb12ca5174f5673cca0.positions[45] );
});