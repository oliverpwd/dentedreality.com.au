---
title: Crazy Grill
date: '2013-07-14T13:48:05+00:00'
format: image
service: flickr
tags:
- bbq
- coals
- costarica
- grill
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440191820_961959dda7_o.jpg?resize=607%2C455
---

[![Crazy Grill](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440191820_961959dda7_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/07/14/crazy-grill/) 
# [Crazy Grill](http://dentedreality.com.au/2013/07/14/crazy-grill/)





* #[bbq](http://dentedreality.com.au/tags/bbq/)
* #[coals](http://dentedreality.com.au/tags/coals/)
* #[costarica](http://dentedreality.com.au/tags/costarica/)
* #[grill](http://dentedreality.com.au/tags/grill/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9440191820/) [1:48 pm, July 14, 2013](http://dentedreality.com.au/2013/07/14/crazy-grill/ "1:48 pm") 
jQuery(document).ready(function(){
var gmap\_m2c1c14992ef54438a3e6a756047c15fe = {
positions : {
748 : new google.maps.LatLng( '9.880177', '-85.530009' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2c1c14992ef54438a3e6a756047c15fe' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2c1c14992ef54438a3e6a756047c15fe.positions ) {
gmap\_m2c1c14992ef54438a3e6a756047c15fe.bounds.extend( gmap\_m2c1c14992ef54438a3e6a756047c15fe.positions[m] );
}
// Render markers
for ( var m in gmap\_m2c1c14992ef54438a3e6a756047c15fe.positions ) {
gmap\_m2c1c14992ef54438a3e6a756047c15fe.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2c1c14992ef54438a3e6a756047c15fe.map,
position : gmap\_m2c1c14992ef54438a3e6a756047c15fe.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2c1c14992ef54438a3e6a756047c15fe.map.setCenter( gmap\_m2c1c14992ef54438a3e6a756047c15fe.positions[748] );
});