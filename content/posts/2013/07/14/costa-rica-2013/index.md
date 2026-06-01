---
title: Costa Rica, 2013
date: '2013-07-14T13:56:38+00:00'
format: image
service: flickr
tags:
- costarica
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440192744_ed44939ec9_o.jpg?resize=607%2C455
---

[![Costa Rica, 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440192744_ed44939ec9_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/07/14/costa-rica-2013/) 
# [Costa Rica, 2013](http://dentedreality.com.au/2013/07/14/costa-rica-2013/)





* #[costarica](http://dentedreality.com.au/tags/costarica/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9440192744/) [1:56 pm, July 14, 2013](http://dentedreality.com.au/2013/07/14/costa-rica-2013/ "1:56 pm") 
jQuery(document).ready(function(){
var gmap\_mb7b461090e1966adcd2a40a1ef323f88 = {
positions : {
38 : new google.maps.LatLng( '9.880075', '-85.529848' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb7b461090e1966adcd2a40a1ef323f88' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb7b461090e1966adcd2a40a1ef323f88.positions ) {
gmap\_mb7b461090e1966adcd2a40a1ef323f88.bounds.extend( gmap\_mb7b461090e1966adcd2a40a1ef323f88.positions[m] );
}
// Render markers
for ( var m in gmap\_mb7b461090e1966adcd2a40a1ef323f88.positions ) {
gmap\_mb7b461090e1966adcd2a40a1ef323f88.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb7b461090e1966adcd2a40a1ef323f88.map,
position : gmap\_mb7b461090e1966adcd2a40a1ef323f88.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb7b461090e1966adcd2a40a1ef323f88.map.setCenter( gmap\_mb7b461090e1966adcd2a40a1ef323f88.positions[38] );
});