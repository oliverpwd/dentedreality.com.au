---
title: Frankenthumb
date: '2014-02-07T12:22:07+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13925257234_46235bf1f5_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13925257234_46235bf1f5_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/02/07/frankenthumb-4/) 
# [Frankenthumb](http://dentedreality.com.au/2014/02/07/frankenthumb-4/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13925257234/) [12:22 pm, February 7, 2014](http://dentedreality.com.au/2014/02/07/frankenthumb-4/ "12:22 pm") 
jQuery(document).ready(function(){
var gmap\_m4817098a905f98135dbc1bea60828784 = {
positions : {
898 : new google.maps.LatLng( '40.669444', '-73.984887' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4817098a905f98135dbc1bea60828784' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4817098a905f98135dbc1bea60828784.positions ) {
gmap\_m4817098a905f98135dbc1bea60828784.bounds.extend( gmap\_m4817098a905f98135dbc1bea60828784.positions[m] );
}
// Render markers
for ( var m in gmap\_m4817098a905f98135dbc1bea60828784.positions ) {
gmap\_m4817098a905f98135dbc1bea60828784.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4817098a905f98135dbc1bea60828784.map,
position : gmap\_m4817098a905f98135dbc1bea60828784.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4817098a905f98135dbc1bea60828784.map.setCenter( gmap\_m4817098a905f98135dbc1bea60828784.positions[898] );
});