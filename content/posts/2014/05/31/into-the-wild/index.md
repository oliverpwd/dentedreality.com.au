---
title: ''
date: '2014-05-31T15:14:44+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/05/10424675_1484774708422163_1175659864_n.jpg?resize=640%2C640
---

[![Into The Wild](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/05/10424675_1484774708422163_1175659864_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/05/31/into-the-wild/) 

Into The Wild





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/orJrp2imAN/) [3:14 pm, May 31, 2014](http://dentedreality.com.au/2014/05/31/into-the-wild/ "3:14 pm") 
jQuery(document).ready(function(){
var gmap\_m11e8f888d53f6f22df2471969c6d7006 = {
positions : {
283 : new google.maps.LatLng( '41.173925451', '-74.168624423' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m11e8f888d53f6f22df2471969c6d7006' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m11e8f888d53f6f22df2471969c6d7006.positions ) {
gmap\_m11e8f888d53f6f22df2471969c6d7006.bounds.extend( gmap\_m11e8f888d53f6f22df2471969c6d7006.positions[m] );
}
// Render markers
for ( var m in gmap\_m11e8f888d53f6f22df2471969c6d7006.positions ) {
gmap\_m11e8f888d53f6f22df2471969c6d7006.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m11e8f888d53f6f22df2471969c6d7006.map,
position : gmap\_m11e8f888d53f6f22df2471969c6d7006.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m11e8f888d53f6f22df2471969c6d7006.map.setCenter( gmap\_m11e8f888d53f6f22df2471969c6d7006.positions[283] );
});