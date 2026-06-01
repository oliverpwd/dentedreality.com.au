---
title: Epic Australian Adventure, 2014
date: '2014-03-15T11:43:49+00:00'
format: image
service: flickr
tags:
- perth
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904720622_9a719bd27b_o.jpg?resize=607%2C809
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904720622_9a719bd27b_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2014/03/15/epic-australian-adventure-2014-22/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/15/epic-australian-adventure-2014-22/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904720622/) [11:43 am, March 15, 2014](http://dentedreality.com.au/2014/03/15/epic-australian-adventure-2014-22/ "11:43 am") 
jQuery(document).ready(function(){
var gmap\_m3f2d46ef975e3bb4101eacbf8cce08ba = {
positions : {
952 : new google.maps.LatLng( '-31.940692', '115.819441' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3f2d46ef975e3bb4101eacbf8cce08ba' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3f2d46ef975e3bb4101eacbf8cce08ba.positions ) {
gmap\_m3f2d46ef975e3bb4101eacbf8cce08ba.bounds.extend( gmap\_m3f2d46ef975e3bb4101eacbf8cce08ba.positions[m] );
}
// Render markers
for ( var m in gmap\_m3f2d46ef975e3bb4101eacbf8cce08ba.positions ) {
gmap\_m3f2d46ef975e3bb4101eacbf8cce08ba.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3f2d46ef975e3bb4101eacbf8cce08ba.map,
position : gmap\_m3f2d46ef975e3bb4101eacbf8cce08ba.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3f2d46ef975e3bb4101eacbf8cce08ba.map.setCenter( gmap\_m3f2d46ef975e3bb4101eacbf8cce08ba.positions[952] );
});