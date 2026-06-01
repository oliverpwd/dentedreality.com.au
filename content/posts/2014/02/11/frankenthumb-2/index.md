---
title: Frankenthumb
date: '2014-02-11T15:27:10+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13924815375_de02f27098_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13924815375_de02f27098_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/02/11/frankenthumb-2/) 
# [Frankenthumb](http://dentedreality.com.au/2014/02/11/frankenthumb-2/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924815375/) [3:27 pm, February 11, 2014](http://dentedreality.com.au/2014/02/11/frankenthumb-2/ "3:27 pm") 
jQuery(document).ready(function(){
var gmap\_m903048fe3b617864e83129f5b044b9b5 = {
positions : {
402 : new google.maps.LatLng( '40.669433', '-73.984948' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m903048fe3b617864e83129f5b044b9b5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m903048fe3b617864e83129f5b044b9b5.positions ) {
gmap\_m903048fe3b617864e83129f5b044b9b5.bounds.extend( gmap\_m903048fe3b617864e83129f5b044b9b5.positions[m] );
}
// Render markers
for ( var m in gmap\_m903048fe3b617864e83129f5b044b9b5.positions ) {
gmap\_m903048fe3b617864e83129f5b044b9b5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m903048fe3b617864e83129f5b044b9b5.map,
position : gmap\_m903048fe3b617864e83129f5b044b9b5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m903048fe3b617864e83129f5b044b9b5.map.setCenter( gmap\_m903048fe3b617864e83129f5b044b9b5.positions[402] );
});