---
title: Louvre
date: '2013-12-01T11:09:37+00:00'
format: image
service: flickr
tags:
- france
- louvre
- paris
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900363211_90f3f06cf6_o.jpg?fit=1500%2C1500
---

[![Louvre](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900363211_90f3f06cf6_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/01/louvre/) 
# [Louvre](http://dentedreality.com.au/2013/12/01/louvre/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[louvre](http://dentedreality.com.au/tags/louvre/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900363211/) [11:09 am, December 1, 2013](http://dentedreality.com.au/2013/12/01/louvre/ "11:09 am") 
jQuery(document).ready(function(){
var gmap\_m679f06f79491993a4bd0f5b45ef5c6c4 = {
positions : {
118 : new google.maps.LatLng( '48.861236', '2.335747' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m679f06f79491993a4bd0f5b45ef5c6c4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m679f06f79491993a4bd0f5b45ef5c6c4.positions ) {
gmap\_m679f06f79491993a4bd0f5b45ef5c6c4.bounds.extend( gmap\_m679f06f79491993a4bd0f5b45ef5c6c4.positions[m] );
}
// Render markers
for ( var m in gmap\_m679f06f79491993a4bd0f5b45ef5c6c4.positions ) {
gmap\_m679f06f79491993a4bd0f5b45ef5c6c4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m679f06f79491993a4bd0f5b45ef5c6c4.map,
position : gmap\_m679f06f79491993a4bd0f5b45ef5c6c4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m679f06f79491993a4bd0f5b45ef5c6c4.map.setCenter( gmap\_m679f06f79491993a4bd0f5b45ef5c6c4.positions[118] );
});