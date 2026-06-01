---
title: Lounge Kitchen
date: '2013-05-17T09:35:22+00:00'
format: image
service: flickr
tags:
- automattic
- hawthorne
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436930521_27e547fbcc_o.jpg?resize=607%2C452
---

[![Lounge Kitchen](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436930521_27e547fbcc_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/05/17/lounge-kitchen/) 
# [Lounge Kitchen](http://dentedreality.com.au/2013/05/17/lounge-kitchen/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[hawthorne](http://dentedreality.com.au/tags/hawthorne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9436930521/) [9:35 am, May 17, 2013](http://dentedreality.com.au/2013/05/17/lounge-kitchen/ "9:35 am") 
jQuery(document).ready(function(){
var gmap\_me088996fc1a39129a1ffba3888be453a = {
positions : {
536 : new google.maps.LatLng( '37.784333', '-122.397334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me088996fc1a39129a1ffba3888be453a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me088996fc1a39129a1ffba3888be453a.positions ) {
gmap\_me088996fc1a39129a1ffba3888be453a.bounds.extend( gmap\_me088996fc1a39129a1ffba3888be453a.positions[m] );
}
// Render markers
for ( var m in gmap\_me088996fc1a39129a1ffba3888be453a.positions ) {
gmap\_me088996fc1a39129a1ffba3888be453a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me088996fc1a39129a1ffba3888be453a.map,
position : gmap\_me088996fc1a39129a1ffba3888be453a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me088996fc1a39129a1ffba3888be453a.map.setCenter( gmap\_me088996fc1a39129a1ffba3888be453a.positions[536] );
});