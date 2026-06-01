---
title: Camping on Angel Island
date: '2011-11-25T13:31:50+00:00'
format: image
service: flickr
tags:
- angelisland
- california
- camping
- outdoors
- sanfrancisco
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6812209804_595747fb99_o.jpg?resize=607%2C452
---

[![Camping on Angel Island](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6812209804_595747fb99_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/11/25/camping-on-angel-island-5/) 
# [Camping on Angel Island](http://dentedreality.com.au/2011/11/25/camping-on-angel-island-5/)





* #[angelisland](http://dentedreality.com.au/tags/angelisland/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[camping](http://dentedreality.com.au/tags/camping/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812209804/) [1:31 pm, November 25, 2011](http://dentedreality.com.au/2011/11/25/camping-on-angel-island-5/ "1:31 pm") 
jQuery(document).ready(function(){
var gmap\_m3937a33b5d3d009d01f27c2a0152d60d = {
positions : {
789 : new google.maps.LatLng( '37.858333', '-122.424334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3937a33b5d3d009d01f27c2a0152d60d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3937a33b5d3d009d01f27c2a0152d60d.positions ) {
gmap\_m3937a33b5d3d009d01f27c2a0152d60d.bounds.extend( gmap\_m3937a33b5d3d009d01f27c2a0152d60d.positions[m] );
}
// Render markers
for ( var m in gmap\_m3937a33b5d3d009d01f27c2a0152d60d.positions ) {
gmap\_m3937a33b5d3d009d01f27c2a0152d60d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3937a33b5d3d009d01f27c2a0152d60d.map,
position : gmap\_m3937a33b5d3d009d01f27c2a0152d60d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3937a33b5d3d009d01f27c2a0152d60d.map.setCenter( gmap\_m3937a33b5d3d009d01f27c2a0152d60d.positions[789] );
});