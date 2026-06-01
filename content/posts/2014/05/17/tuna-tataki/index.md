---
title: ''
date: '2014-05-17T11:39:26-06:00'
format: image
service: instagram
tags:
- photo
latitude: '38.9084487'
longitude: '-76.9974852'
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/05/10296699_291597194333054_1190902436_n.jpg?resize=640%2C640
---

[![Tuna Tataki](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/05/10296699_291597194333054_1190902436_n.jpg?resize=640%2C640)](https://dentedreality.com.au/2014/05/17/tuna-tataki/) 

[![Tuna Tataki](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/05/10296699_291597194333054_1190902436_n.jpg?resize=640%2C640)](http://instagram.com/p/oGt6jTimOB/)

Tuna Tataki

38.9084487-76.9974852




* #[photo](https://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/oGt6jTimOB/) [11:39 am, May 17, 2014](https://dentedreality.com.au/2014/05/17/tuna-tataki/ "11:39 am") 
jQuery(document).ready(function(){
var gmap\_m807ac5cd623d0919e47d6b325a0b47e3 = {
positions : {
866 : new google.maps.LatLng( '38.908448716', '-76.997485158' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m807ac5cd623d0919e47d6b325a0b47e3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m807ac5cd623d0919e47d6b325a0b47e3.positions ) {
gmap\_m807ac5cd623d0919e47d6b325a0b47e3.bounds.extend( gmap\_m807ac5cd623d0919e47d6b325a0b47e3.positions[m] );
}
// Render markers
for ( var m in gmap\_m807ac5cd623d0919e47d6b325a0b47e3.positions ) {
gmap\_m807ac5cd623d0919e47d6b325a0b47e3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m807ac5cd623d0919e47d6b325a0b47e3.map,
position : gmap\_m807ac5cd623d0919e47d6b325a0b47e3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m807ac5cd623d0919e47d6b325a0b47e3.map.setCenter( gmap\_m807ac5cd623d0919e47d6b325a0b47e3.positions[866] );
});