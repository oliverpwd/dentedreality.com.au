---
title: Snowy Trees
date: '2012-01-22T05:17:01+00:00'
format: image
service: flickr
tags:
- mountain
- snow
- trees
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813456080_51194cf0c4_o.jpg?resize=607%2C452
---

[![Snowy Trees](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813456080_51194cf0c4_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/22/snowy-trees/) 
# [Snowy Trees](http://dentedreality.com.au/2012/01/22/snowy-trees/)





* #[mountain](http://dentedreality.com.au/tags/mountain/)
* #[snow](http://dentedreality.com.au/tags/snow/)
* #[trees](http://dentedreality.com.au/tags/trees/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813456080/) [5:17 am, January 22, 2012](http://dentedreality.com.au/2012/01/22/snowy-trees/ "5:17 am") 
jQuery(document).ready(function(){
var gmap\_m81c631c3e90a1a7dbec458ea354a7213 = {
positions : {
961 : new google.maps.LatLng( '39.170833', '-120.2315' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m81c631c3e90a1a7dbec458ea354a7213' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m81c631c3e90a1a7dbec458ea354a7213.positions ) {
gmap\_m81c631c3e90a1a7dbec458ea354a7213.bounds.extend( gmap\_m81c631c3e90a1a7dbec458ea354a7213.positions[m] );
}
// Render markers
for ( var m in gmap\_m81c631c3e90a1a7dbec458ea354a7213.positions ) {
gmap\_m81c631c3e90a1a7dbec458ea354a7213.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m81c631c3e90a1a7dbec458ea354a7213.map,
position : gmap\_m81c631c3e90a1a7dbec458ea354a7213.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m81c631c3e90a1a7dbec458ea354a7213.map.setCenter( gmap\_m81c631c3e90a1a7dbec458ea354a7213.positions[961] );
});