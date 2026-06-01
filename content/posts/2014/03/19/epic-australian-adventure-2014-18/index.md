---
title: Epic Australian Adventure, 2014
date: '2014-03-19T04:23:04+00:00'
format: image
service: flickr
tags:
- perth
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904720716_13fcc0f1e4_o.jpg?resize=607%2C212
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904720716_13fcc0f1e4_o.jpg?resize=607%2C212)](http://dentedreality.com.au/2014/03/19/epic-australian-adventure-2014-18/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/19/epic-australian-adventure-2014-18/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904720716/) [4:23 am, March 19, 2014](http://dentedreality.com.au/2014/03/19/epic-australian-adventure-2014-18/ "4:23 am") 
jQuery(document).ready(function(){
var gmap\_m02a8852c53f66bc7984e4b09c2d37fe4 = {
positions : {
771 : new google.maps.LatLng( '-31.994667', '115.751602' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m02a8852c53f66bc7984e4b09c2d37fe4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m02a8852c53f66bc7984e4b09c2d37fe4.positions ) {
gmap\_m02a8852c53f66bc7984e4b09c2d37fe4.bounds.extend( gmap\_m02a8852c53f66bc7984e4b09c2d37fe4.positions[m] );
}
// Render markers
for ( var m in gmap\_m02a8852c53f66bc7984e4b09c2d37fe4.positions ) {
gmap\_m02a8852c53f66bc7984e4b09c2d37fe4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m02a8852c53f66bc7984e4b09c2d37fe4.map,
position : gmap\_m02a8852c53f66bc7984e4b09c2d37fe4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m02a8852c53f66bc7984e4b09c2d37fe4.map.setCenter( gmap\_m02a8852c53f66bc7984e4b09c2d37fe4.positions[771] );
});