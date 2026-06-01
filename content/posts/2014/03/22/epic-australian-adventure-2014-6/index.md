---
title: Epic Australian Adventure, 2014
date: '2014-03-22T16:15:19+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904742892_520ec3f93b_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904742892_520ec3f93b_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/22/epic-australian-adventure-2014-6/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/22/epic-australian-adventure-2014-6/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904742892/) [4:15 pm, March 22, 2014](http://dentedreality.com.au/2014/03/22/epic-australian-adventure-2014-6/ "4:15 pm") 
jQuery(document).ready(function(){
var gmap\_m3af24f46f25b8a7e6af1e3f4a37acee2 = {
positions : {
249 : new google.maps.LatLng( '-37.824087', '144.953352' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3af24f46f25b8a7e6af1e3f4a37acee2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3af24f46f25b8a7e6af1e3f4a37acee2.positions ) {
gmap\_m3af24f46f25b8a7e6af1e3f4a37acee2.bounds.extend( gmap\_m3af24f46f25b8a7e6af1e3f4a37acee2.positions[m] );
}
// Render markers
for ( var m in gmap\_m3af24f46f25b8a7e6af1e3f4a37acee2.positions ) {
gmap\_m3af24f46f25b8a7e6af1e3f4a37acee2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3af24f46f25b8a7e6af1e3f4a37acee2.map,
position : gmap\_m3af24f46f25b8a7e6af1e3f4a37acee2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3af24f46f25b8a7e6af1e3f4a37acee2.map.setCenter( gmap\_m3af24f46f25b8a7e6af1e3f4a37acee2.positions[249] );
});