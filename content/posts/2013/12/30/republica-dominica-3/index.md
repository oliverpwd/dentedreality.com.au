---
title: Republica Dominica
date: '2013-12-30T12:41:53+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924315963_ccc1740fba_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924315963_ccc1740fba_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/30/republica-dominica-3/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/30/republica-dominica-3/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924315963/) [12:41 pm, December 30, 2013](http://dentedreality.com.au/2013/12/30/republica-dominica-3/ "12:41 pm") 
jQuery(document).ready(function(){
var gmap\_m904a29e985616731d0ee2417c2c933e9 = {
positions : {
289 : new google.maps.LatLng( '19.087927', '-70.642089' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m904a29e985616731d0ee2417c2c933e9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m904a29e985616731d0ee2417c2c933e9.positions ) {
gmap\_m904a29e985616731d0ee2417c2c933e9.bounds.extend( gmap\_m904a29e985616731d0ee2417c2c933e9.positions[m] );
}
// Render markers
for ( var m in gmap\_m904a29e985616731d0ee2417c2c933e9.positions ) {
gmap\_m904a29e985616731d0ee2417c2c933e9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m904a29e985616731d0ee2417c2c933e9.map,
position : gmap\_m904a29e985616731d0ee2417c2c933e9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m904a29e985616731d0ee2417c2c933e9.map.setCenter( gmap\_m904a29e985616731d0ee2417c2c933e9.positions[289] );
});