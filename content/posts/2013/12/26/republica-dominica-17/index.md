---
title: Republica Dominica
date: '2013-12-26T11:25:11+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924242375_7373bc174c_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924242375_7373bc174c_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/26/republica-dominica-17/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/26/republica-dominica-17/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924242375/) [11:25 am, December 26, 2013](http://dentedreality.com.au/2013/12/26/republica-dominica-17/ "11:25 am") 
jQuery(document).ready(function(){
var gmap\_medca45e0f820f08fc7eb67dab6cdcdb8 = {
positions : {
212 : new google.maps.LatLng( '19.581938', '-70.744889' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_medca45e0f820f08fc7eb67dab6cdcdb8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_medca45e0f820f08fc7eb67dab6cdcdb8.positions ) {
gmap\_medca45e0f820f08fc7eb67dab6cdcdb8.bounds.extend( gmap\_medca45e0f820f08fc7eb67dab6cdcdb8.positions[m] );
}
// Render markers
for ( var m in gmap\_medca45e0f820f08fc7eb67dab6cdcdb8.positions ) {
gmap\_medca45e0f820f08fc7eb67dab6cdcdb8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_medca45e0f820f08fc7eb67dab6cdcdb8.map,
position : gmap\_medca45e0f820f08fc7eb67dab6cdcdb8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_medca45e0f820f08fc7eb67dab6cdcdb8.map.setCenter( gmap\_medca45e0f820f08fc7eb67dab6cdcdb8.positions[212] );
});