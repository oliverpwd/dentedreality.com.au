---
title: Epic Australian Adventure, 2014
date: '2014-03-15T07:57:58+00:00'
format: image
service: flickr
tags:
- perth
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904718022_4d7cb68341_o.jpg?resize=607%2C197
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904718022_4d7cb68341_o.jpg?resize=607%2C197)](http://dentedreality.com.au/2014/03/15/epic-australian-adventure-2014-45/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/15/epic-australian-adventure-2014-45/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904718022/) [7:57 am, March 15, 2014](http://dentedreality.com.au/2014/03/15/epic-australian-adventure-2014-45/ "7:57 am") 
jQuery(document).ready(function(){
var gmap\_m3c7eba9340078f0d06357ad45b89c35d = {
positions : {
671 : new google.maps.LatLng( '-32.034378', '115.7455' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3c7eba9340078f0d06357ad45b89c35d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3c7eba9340078f0d06357ad45b89c35d.positions ) {
gmap\_m3c7eba9340078f0d06357ad45b89c35d.bounds.extend( gmap\_m3c7eba9340078f0d06357ad45b89c35d.positions[m] );
}
// Render markers
for ( var m in gmap\_m3c7eba9340078f0d06357ad45b89c35d.positions ) {
gmap\_m3c7eba9340078f0d06357ad45b89c35d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3c7eba9340078f0d06357ad45b89c35d.map,
position : gmap\_m3c7eba9340078f0d06357ad45b89c35d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3c7eba9340078f0d06357ad45b89c35d.map.setCenter( gmap\_m3c7eba9340078f0d06357ad45b89c35d.positions[671] );
});