---
title: Republica Dominica
date: '2013-12-28T12:18:27+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924696594_8207a7cf73_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924696594_8207a7cf73_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/28/republica-dominica-9/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/28/republica-dominica-9/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924696594/) [12:18 pm, December 28, 2013](http://dentedreality.com.au/2013/12/28/republica-dominica-9/ "12:18 pm") 
jQuery(document).ready(function(){
var gmap\_m51b8d1ff0cfa7785748afb4d77e17dbc = {
positions : {
173 : new google.maps.LatLng( '19.886102', '-71.657067' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m51b8d1ff0cfa7785748afb4d77e17dbc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m51b8d1ff0cfa7785748afb4d77e17dbc.positions ) {
gmap\_m51b8d1ff0cfa7785748afb4d77e17dbc.bounds.extend( gmap\_m51b8d1ff0cfa7785748afb4d77e17dbc.positions[m] );
}
// Render markers
for ( var m in gmap\_m51b8d1ff0cfa7785748afb4d77e17dbc.positions ) {
gmap\_m51b8d1ff0cfa7785748afb4d77e17dbc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m51b8d1ff0cfa7785748afb4d77e17dbc.map,
position : gmap\_m51b8d1ff0cfa7785748afb4d77e17dbc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m51b8d1ff0cfa7785748afb4d77e17dbc.map.setCenter( gmap\_m51b8d1ff0cfa7785748afb4d77e17dbc.positions[173] );
});