---
title: ''
date: '2018-06-29T18:49:59-06:00'
format: image
service: instagram
tags:
- fjallravenclassicusa
latitude: '39.444'
longitude: '-106.326'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182137/36086514_1565251430269613_8305418409076588544_n.jpg?resize=607%2C604&ssl=1
---

[![Matchy matchy hats on #fjallravenclassicusa](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182137/36086514_1565251430269613_8305418409076588544_n.jpg?resize=607%2C604&ssl=1)](https://dentedreality.com.au/2018/06/29/matchy-matchy-hats-on-fjallravenclassicusa/) 

[![Matchy matchy hats on #fjallravenclassicusa](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182137/36086514_1565251430269613_8305418409076588544_n.jpg?resize=607%2C604&ssl=1)](https://www.instagram.com/p/BkoRnXbFJ1M/)

Matchy matchy hats on #fjallravenclassicusa

39.444-106.326




* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BkoRnXbFJ1M/) [6:49 pm, June 29, 2018](https://dentedreality.com.au/2018/06/29/matchy-matchy-hats-on-fjallravenclassicusa/ "6:49 pm") 
jQuery(document).ready(function(){
var gmap\_m194e243cc11776fa76f11d70bb638bfb = {
positions : {
280 : new google.maps.LatLng( '39.444', '-106.326' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m194e243cc11776fa76f11d70bb638bfb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m194e243cc11776fa76f11d70bb638bfb.positions ) {
gmap\_m194e243cc11776fa76f11d70bb638bfb.bounds.extend( gmap\_m194e243cc11776fa76f11d70bb638bfb.positions[m] );
}
// Render markers
for ( var m in gmap\_m194e243cc11776fa76f11d70bb638bfb.positions ) {
gmap\_m194e243cc11776fa76f11d70bb638bfb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m194e243cc11776fa76f11d70bb638bfb.map,
position : gmap\_m194e243cc11776fa76f11d70bb638bfb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m194e243cc11776fa76f11d70bb638bfb.map.setCenter( gmap\_m194e243cc11776fa76f11d70bb638bfb.positions[280] );
});