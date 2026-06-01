---
title: Epic Australian Adventure, 2014
date: '2014-03-20T09:58:14+00:00'
format: image
service: flickr
tags:
- mooloolaba
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904731676_22395dfedd_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904731676_22395dfedd_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/20/epic-australian-adventure-2014-11/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/20/epic-australian-adventure-2014-11/)

Perth, Mooloolaba and Melbourne





* #[mooloolaba](http://dentedreality.com.au/tags/mooloolaba/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904731676/) [9:58 am, March 20, 2014](http://dentedreality.com.au/2014/03/20/epic-australian-adventure-2014-11/ "9:58 am") 
jQuery(document).ready(function(){
var gmap\_m7a24e832f49a488a1e1a5c9665fbe8d3 = {
positions : {
807 : new google.maps.LatLng( '-26.750784', '153.046447' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7a24e832f49a488a1e1a5c9665fbe8d3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7a24e832f49a488a1e1a5c9665fbe8d3.positions ) {
gmap\_m7a24e832f49a488a1e1a5c9665fbe8d3.bounds.extend( gmap\_m7a24e832f49a488a1e1a5c9665fbe8d3.positions[m] );
}
// Render markers
for ( var m in gmap\_m7a24e832f49a488a1e1a5c9665fbe8d3.positions ) {
gmap\_m7a24e832f49a488a1e1a5c9665fbe8d3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7a24e832f49a488a1e1a5c9665fbe8d3.map,
position : gmap\_m7a24e832f49a488a1e1a5c9665fbe8d3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7a24e832f49a488a1e1a5c9665fbe8d3.map.setCenter( gmap\_m7a24e832f49a488a1e1a5c9665fbe8d3.positions[807] );
});