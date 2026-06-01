---
title: Epic Australian Adventure, 2014
date: '2014-03-25T16:35:12+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927874285_9ca324ec2b_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927874285_9ca324ec2b_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-31/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-31/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927874285/) [4:35 pm, March 25, 2014](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-31/ "4:35 pm") 
jQuery(document).ready(function(){
var gmap\_m3ab17daaf020797c5339f5eeb73f312c = {
positions : {
97 : new google.maps.LatLng( '-37.810139', '144.969758' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3ab17daaf020797c5339f5eeb73f312c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3ab17daaf020797c5339f5eeb73f312c.positions ) {
gmap\_m3ab17daaf020797c5339f5eeb73f312c.bounds.extend( gmap\_m3ab17daaf020797c5339f5eeb73f312c.positions[m] );
}
// Render markers
for ( var m in gmap\_m3ab17daaf020797c5339f5eeb73f312c.positions ) {
gmap\_m3ab17daaf020797c5339f5eeb73f312c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3ab17daaf020797c5339f5eeb73f312c.map,
position : gmap\_m3ab17daaf020797c5339f5eeb73f312c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3ab17daaf020797c5339f5eeb73f312c.map.setCenter( gmap\_m3ab17daaf020797c5339f5eeb73f312c.positions[97] );
});