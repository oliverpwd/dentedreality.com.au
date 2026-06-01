---
title: Epic Australian Adventure, 2014
date: '2014-03-18T16:18:45+00:00'
format: image
service: flickr
tags:
- perth
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928281324_1939dce167_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928281324_1939dce167_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/18/epic-australian-adventure-2014-20/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/18/epic-australian-adventure-2014-20/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13928281324/) [4:18 pm, March 18, 2014](http://dentedreality.com.au/2014/03/18/epic-australian-adventure-2014-20/ "4:18 pm") 
jQuery(document).ready(function(){
var gmap\_m23e42c20f3537153a2cb914b8063ba60 = {
positions : {
997 : new google.maps.LatLng( '-31.952114', '115.853019' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m23e42c20f3537153a2cb914b8063ba60' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m23e42c20f3537153a2cb914b8063ba60.positions ) {
gmap\_m23e42c20f3537153a2cb914b8063ba60.bounds.extend( gmap\_m23e42c20f3537153a2cb914b8063ba60.positions[m] );
}
// Render markers
for ( var m in gmap\_m23e42c20f3537153a2cb914b8063ba60.positions ) {
gmap\_m23e42c20f3537153a2cb914b8063ba60.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m23e42c20f3537153a2cb914b8063ba60.map,
position : gmap\_m23e42c20f3537153a2cb914b8063ba60.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m23e42c20f3537153a2cb914b8063ba60.map.setCenter( gmap\_m23e42c20f3537153a2cb914b8063ba60.positions[997] );
});