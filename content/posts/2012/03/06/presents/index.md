---
title: Presents!
date: '2012-03-06T05:41:36+00:00'
format: image
service: flickr
tags:
- christmas
- christmastree
- presents
- tree
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/6813291054_6976037410_o.jpg?resize=607%2C607
---

[![Presents!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/6813291054_6976037410_o.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/03/06/presents/) 
# [Presents!](http://dentedreality.com.au/2012/03/06/presents/)





* #[christmas](http://dentedreality.com.au/tags/christmas/)
* #[christmastree](http://dentedreality.com.au/tags/christmastree/)
* #[presents](http://dentedreality.com.au/tags/presents/)
* #[tree](http://dentedreality.com.au/tags/tree/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813291054/) [5:41 am, March 6, 2012](http://dentedreality.com.au/2012/03/06/presents/ "5:41 am") 
jQuery(document).ready(function(){
var gmap\_m7c55fb5a954e355d3e19dfe29980965a = {
positions : {
686 : new google.maps.LatLng( '37.735833', '-122.433834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7c55fb5a954e355d3e19dfe29980965a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7c55fb5a954e355d3e19dfe29980965a.positions ) {
gmap\_m7c55fb5a954e355d3e19dfe29980965a.bounds.extend( gmap\_m7c55fb5a954e355d3e19dfe29980965a.positions[m] );
}
// Render markers
for ( var m in gmap\_m7c55fb5a954e355d3e19dfe29980965a.positions ) {
gmap\_m7c55fb5a954e355d3e19dfe29980965a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7c55fb5a954e355d3e19dfe29980965a.map,
position : gmap\_m7c55fb5a954e355d3e19dfe29980965a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7c55fb5a954e355d3e19dfe29980965a.map.setCenter( gmap\_m7c55fb5a954e355d3e19dfe29980965a.positions[686] );
});