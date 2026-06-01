---
title: Republica Dominica
date: '2013-12-30T11:02:58+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924310343_92b1d94794_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924310343_92b1d94794_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/30/republica-dominica-7/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/30/republica-dominica-7/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924310343/) [11:02 am, December 30, 2013](http://dentedreality.com.au/2013/12/30/republica-dominica-7/ "11:02 am") 
jQuery(document).ready(function(){
var gmap\_mbdf632c2decd4f47fbbc9c737df3a7c0 = {
positions : {
260 : new google.maps.LatLng( '19.093508', '-70.59462' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbdf632c2decd4f47fbbc9c737df3a7c0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbdf632c2decd4f47fbbc9c737df3a7c0.positions ) {
gmap\_mbdf632c2decd4f47fbbc9c737df3a7c0.bounds.extend( gmap\_mbdf632c2decd4f47fbbc9c737df3a7c0.positions[m] );
}
// Render markers
for ( var m in gmap\_mbdf632c2decd4f47fbbc9c737df3a7c0.positions ) {
gmap\_mbdf632c2decd4f47fbbc9c737df3a7c0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbdf632c2decd4f47fbbc9c737df3a7c0.map,
position : gmap\_mbdf632c2decd4f47fbbc9c737df3a7c0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbdf632c2decd4f47fbbc9c737df3a7c0.map.setCenter( gmap\_mbdf632c2decd4f47fbbc9c737df3a7c0.positions[260] );
});