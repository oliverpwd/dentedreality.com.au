---
title: ''
date: '2018-06-29T19:14:51-06:00'
format: image
service: instagram
tags:
- fjallravenclassicusa
latitude: '39.444'
longitude: '-106.326'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182138/35538841_1873968142664283_4573083213148192768_n.jpg?resize=607%2C607&ssl=1
---

[![No filter needed. Early on day 2 of #fjallravenclassicusa heading out of Camp Hale.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182138/35538841_1873968142664283_4573083213148192768_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/06/29/no-filter-needed-early-on-day-2-of-fjallravenclassicusa-heading-out-of-camp-hale/) 

[![No filter needed. Early on day 2 of #fjallravenclassicusa heading out of Camp Hale.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182138/35538841_1873968142664283_4573083213148192768_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/BkoUdhRFUSd/)

No filter needed. Early on day 2 of #fjallravenclassicusa heading out of Camp Hale.

39.444-106.326




* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BkoUdhRFUSd/) [7:14 pm, June 29, 2018](https://dentedreality.com.au/2018/06/29/no-filter-needed-early-on-day-2-of-fjallravenclassicusa-heading-out-of-camp-hale/ "7:14 pm") 
jQuery(document).ready(function(){
var gmap\_mdfa8f5f88ac7efe6591225b85834d6a9 = {
positions : {
503 : new google.maps.LatLng( '39.444', '-106.326' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdfa8f5f88ac7efe6591225b85834d6a9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdfa8f5f88ac7efe6591225b85834d6a9.positions ) {
gmap\_mdfa8f5f88ac7efe6591225b85834d6a9.bounds.extend( gmap\_mdfa8f5f88ac7efe6591225b85834d6a9.positions[m] );
}
// Render markers
for ( var m in gmap\_mdfa8f5f88ac7efe6591225b85834d6a9.positions ) {
gmap\_mdfa8f5f88ac7efe6591225b85834d6a9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdfa8f5f88ac7efe6591225b85834d6a9.map,
position : gmap\_mdfa8f5f88ac7efe6591225b85834d6a9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdfa8f5f88ac7efe6591225b85834d6a9.map.setCenter( gmap\_mdfa8f5f88ac7efe6591225b85834d6a9.positions[503] );
});