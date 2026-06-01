---
title: ''
date: '2018-06-29T19:11:41-06:00'
format: image
service: instagram
tags:
- fjallravenclassicusa
latitude: '39.444'
longitude: '-106.326'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182137/34982605_2211224739107559_7642134033891065856_n.jpg?resize=607%2C607&ssl=1
---

[![Early start to a long day on day 2 of #fjallravenclassicusa](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182137/34982605_2211224739107559_7642134033891065856_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/06/29/early-start-to-a-long-day-on-day-2-of-fjallravenclassicusa/) 

[![Early start to a long day on day 2 of #fjallravenclassicusa](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182137/34982605_2211224739107559_7642134033891065856_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/BkoUGYTlA2Y/)

Early start to a long day on day 2 of #fjallravenclassicusa

39.444-106.326




* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BkoUGYTlA2Y/) [7:11 pm, June 29, 2018](https://dentedreality.com.au/2018/06/29/early-start-to-a-long-day-on-day-2-of-fjallravenclassicusa/ "7:11 pm") 
jQuery(document).ready(function(){
var gmap\_m1f536640142c3ff88813e7581b235b10 = {
positions : {
66 : new google.maps.LatLng( '39.444', '-106.326' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1f536640142c3ff88813e7581b235b10' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1f536640142c3ff88813e7581b235b10.positions ) {
gmap\_m1f536640142c3ff88813e7581b235b10.bounds.extend( gmap\_m1f536640142c3ff88813e7581b235b10.positions[m] );
}
// Render markers
for ( var m in gmap\_m1f536640142c3ff88813e7581b235b10.positions ) {
gmap\_m1f536640142c3ff88813e7581b235b10.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1f536640142c3ff88813e7581b235b10.map,
position : gmap\_m1f536640142c3ff88813e7581b235b10.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1f536640142c3ff88813e7581b235b10.map.setCenter( gmap\_m1f536640142c3ff88813e7581b235b10.positions[66] );
});