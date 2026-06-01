---
title: ''
date: '2014-06-14T12:25:49+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/06/10449012_1442017146062808_1321667729_n.jpg?resize=640%2C640
---

[![Giant robot](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/06/10449012_1442017146062808_1321667729_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/06/14/giant-robot/) 

Giant robot





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/pO5ewyCmF3/) [12:25 pm, June 14, 2014](http://dentedreality.com.au/2014/06/14/giant-robot/ "12:25 pm") 
jQuery(document).ready(function(){
var gmap\_m13e94631c712092bf81ed8ec038a172e = {
positions : {
303 : new google.maps.LatLng( '45.51907', '-73.585036667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m13e94631c712092bf81ed8ec038a172e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m13e94631c712092bf81ed8ec038a172e.positions ) {
gmap\_m13e94631c712092bf81ed8ec038a172e.bounds.extend( gmap\_m13e94631c712092bf81ed8ec038a172e.positions[m] );
}
// Render markers
for ( var m in gmap\_m13e94631c712092bf81ed8ec038a172e.positions ) {
gmap\_m13e94631c712092bf81ed8ec038a172e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m13e94631c712092bf81ed8ec038a172e.map,
position : gmap\_m13e94631c712092bf81ed8ec038a172e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m13e94631c712092bf81ed8ec038a172e.map.setCenter( gmap\_m13e94631c712092bf81ed8ec038a172e.positions[303] );
});