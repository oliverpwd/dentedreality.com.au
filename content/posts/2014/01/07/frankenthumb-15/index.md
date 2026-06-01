---
title: Frankenthumb
date: '2014-01-07T14:01:44+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901687206_7726b77f60_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901687206_7726b77f60_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/01/07/frankenthumb-15/) 
# [Frankenthumb](http://dentedreality.com.au/2014/01/07/frankenthumb-15/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901687206/) [2:01 pm, January 7, 2014](http://dentedreality.com.au/2014/01/07/frankenthumb-15/ "2:01 pm") 
jQuery(document).ready(function(){
var gmap\_m65e16fd060d144a5c78fe34de1f81d3f = {
positions : {
362 : new google.maps.LatLng( '40.669391', '-73.984992' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m65e16fd060d144a5c78fe34de1f81d3f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m65e16fd060d144a5c78fe34de1f81d3f.positions ) {
gmap\_m65e16fd060d144a5c78fe34de1f81d3f.bounds.extend( gmap\_m65e16fd060d144a5c78fe34de1f81d3f.positions[m] );
}
// Render markers
for ( var m in gmap\_m65e16fd060d144a5c78fe34de1f81d3f.positions ) {
gmap\_m65e16fd060d144a5c78fe34de1f81d3f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m65e16fd060d144a5c78fe34de1f81d3f.map,
position : gmap\_m65e16fd060d144a5c78fe34de1f81d3f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m65e16fd060d144a5c78fe34de1f81d3f.map.setCenter( gmap\_m65e16fd060d144a5c78fe34de1f81d3f.positions[362] );
});