---
title: Frankenthumb
date: '2014-01-13T06:52:54+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13925248944_970810b4b3_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13925248944_970810b4b3_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/01/13/frankenthumb-13/) 
# [Frankenthumb](http://dentedreality.com.au/2014/01/13/frankenthumb-13/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13925248944/) [6:52 am, January 13, 2014](http://dentedreality.com.au/2014/01/13/frankenthumb-13/ "6:52 am") 
jQuery(document).ready(function(){
var gmap\_m229bc42bca7aaf029f12a01ec89eea4f = {
positions : {
735 : new google.maps.LatLng( '40.694888', '-73.987403' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m229bc42bca7aaf029f12a01ec89eea4f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m229bc42bca7aaf029f12a01ec89eea4f.positions ) {
gmap\_m229bc42bca7aaf029f12a01ec89eea4f.bounds.extend( gmap\_m229bc42bca7aaf029f12a01ec89eea4f.positions[m] );
}
// Render markers
for ( var m in gmap\_m229bc42bca7aaf029f12a01ec89eea4f.positions ) {
gmap\_m229bc42bca7aaf029f12a01ec89eea4f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m229bc42bca7aaf029f12a01ec89eea4f.map,
position : gmap\_m229bc42bca7aaf029f12a01ec89eea4f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m229bc42bca7aaf029f12a01ec89eea4f.map.setCenter( gmap\_m229bc42bca7aaf029f12a01ec89eea4f.positions[735] );
});