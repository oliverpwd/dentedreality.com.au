---
title: ''
date: '2011-03-16T13:40:29+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5cfa340d31de4227820a56dbf3826cc7_7.jpg?resize=607%2C607
---

[![Geniuses](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5cfa340d31de4227820a56dbf3826cc7_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/03/16/geniuses/) 

Geniuses





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/CSQfl/) [1:40 pm, March 16, 2011](http://dentedreality.com.au/2011/03/16/geniuses/ "1:40 pm") 
jQuery(document).ready(function(){
var gmap\_m021c8fc6f6f6e044014110f50f212add = {
positions : {
721 : new google.maps.LatLng( '30.264324', '-97.739243' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m021c8fc6f6f6e044014110f50f212add' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m021c8fc6f6f6e044014110f50f212add.positions ) {
gmap\_m021c8fc6f6f6e044014110f50f212add.bounds.extend( gmap\_m021c8fc6f6f6e044014110f50f212add.positions[m] );
}
// Render markers
for ( var m in gmap\_m021c8fc6f6f6e044014110f50f212add.positions ) {
gmap\_m021c8fc6f6f6e044014110f50f212add.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m021c8fc6f6f6e044014110f50f212add.map,
position : gmap\_m021c8fc6f6f6e044014110f50f212add.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m021c8fc6f6f6e044014110f50f212add.map.setCenter( gmap\_m021c8fc6f6f6e044014110f50f212add.positions[721] );
});