---
title: Angry Birds Cometh
date: '2012-07-31T16:28:31+00:00'
format: image
service: flickr
tags:
- angrybirds
- graffiti
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/07/8244716983_08d7c72703_o.jpg?resize=607%2C452
---

[![Angry Birds Cometh](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/07/8244716983_08d7c72703_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/07/31/angry-birds-cometh/) 
# [Angry Birds Cometh](http://dentedreality.com.au/2012/07/31/angry-birds-cometh/)





* #[angrybirds](http://dentedreality.com.au/tags/angrybirds/)
* #[graffiti](http://dentedreality.com.au/tags/graffiti/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8244716983/) [4:28 pm, July 31, 2012](http://dentedreality.com.au/2012/07/31/angry-birds-cometh/ "4:28 pm") 
jQuery(document).ready(function(){
var gmap\_m7f88a38157e2c7c234356b76eda6897e = {
positions : {
448 : new google.maps.LatLng( '40.7345', '-73.954334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7f88a38157e2c7c234356b76eda6897e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7f88a38157e2c7c234356b76eda6897e.positions ) {
gmap\_m7f88a38157e2c7c234356b76eda6897e.bounds.extend( gmap\_m7f88a38157e2c7c234356b76eda6897e.positions[m] );
}
// Render markers
for ( var m in gmap\_m7f88a38157e2c7c234356b76eda6897e.positions ) {
gmap\_m7f88a38157e2c7c234356b76eda6897e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7f88a38157e2c7c234356b76eda6897e.map,
position : gmap\_m7f88a38157e2c7c234356b76eda6897e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7f88a38157e2c7c234356b76eda6897e.map.setCenter( gmap\_m7f88a38157e2c7c234356b76eda6897e.positions[448] );
});