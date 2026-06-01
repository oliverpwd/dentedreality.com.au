---
title: ''
date: '2017-06-14T08:06:50-06:00'
format: image
service: instagram
tags:
- eiffeltower
latitude: '48.8733692'
longitude: '2.2965205'
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/06/19051755_771235649722614_1443697610954113024_n.jpg?fit=640%2C640&ssl=1
---

[![Priority focus #eiffeltower](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/06/19051755_771235649722614_1443697610954113024_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/06/14/priority-focus-eiffeltower/) 

[![Priority focus #eiffeltower](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/06/19051755_771235649722614_1443697610954113024_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BVUp8XaB7Jg/)

Priority focus #eiffeltower

48.87336922.2965205




* #[eiffeltower](https://dentedreality.com.au/tags/eiffeltower/)

Posted on [Instagram](https://www.instagram.com/p/BVUp8XaB7Jg/) [8:06 am, June 14, 2017](https://dentedreality.com.au/2017/06/14/priority-focus-eiffeltower/ "8:06 am") 
jQuery(document).ready(function(){
var gmap\_mb0a9ca7d4086744b22665b67686b7f13 = {
positions : {
177 : new google.maps.LatLng( '48.873369178314', '2.2965205289044' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb0a9ca7d4086744b22665b67686b7f13' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb0a9ca7d4086744b22665b67686b7f13.positions ) {
gmap\_mb0a9ca7d4086744b22665b67686b7f13.bounds.extend( gmap\_mb0a9ca7d4086744b22665b67686b7f13.positions[m] );
}
// Render markers
for ( var m in gmap\_mb0a9ca7d4086744b22665b67686b7f13.positions ) {
gmap\_mb0a9ca7d4086744b22665b67686b7f13.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb0a9ca7d4086744b22665b67686b7f13.map,
position : gmap\_mb0a9ca7d4086744b22665b67686b7f13.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb0a9ca7d4086744b22665b67686b7f13.map.setCenter( gmap\_mb0a9ca7d4086744b22665b67686b7f13.positions[177] );
});