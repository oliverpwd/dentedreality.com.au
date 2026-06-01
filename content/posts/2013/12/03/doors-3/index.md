---
title: Doors
date: '2013-12-03T11:30:11+00:00'
format: image
service: flickr
tags:
- door
- france
- paris
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923549233_1883a4002b_o.jpg?fit=1500%2C1500
---

[![Doors](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923549233_1883a4002b_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/03/doors-3/) 
# [Doors](http://dentedreality.com.au/2013/12/03/doors-3/)





* #[door](http://dentedreality.com.au/tags/door/)
* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13923549233/) [11:30 am, December 3, 2013](http://dentedreality.com.au/2013/12/03/doors-3/ "11:30 am") 
jQuery(document).ready(function(){
var gmap\_m8cac2ea1b8cb5f6131c2c627c8401632 = {
positions : {
189 : new google.maps.LatLng( '48.85808', '2.358111' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8cac2ea1b8cb5f6131c2c627c8401632' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8cac2ea1b8cb5f6131c2c627c8401632.positions ) {
gmap\_m8cac2ea1b8cb5f6131c2c627c8401632.bounds.extend( gmap\_m8cac2ea1b8cb5f6131c2c627c8401632.positions[m] );
}
// Render markers
for ( var m in gmap\_m8cac2ea1b8cb5f6131c2c627c8401632.positions ) {
gmap\_m8cac2ea1b8cb5f6131c2c627c8401632.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8cac2ea1b8cb5f6131c2c627c8401632.map,
position : gmap\_m8cac2ea1b8cb5f6131c2c627c8401632.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8cac2ea1b8cb5f6131c2c627c8401632.map.setCenter( gmap\_m8cac2ea1b8cb5f6131c2c627c8401632.positions[189] );
});