---
title: Epic Australian Adventure, 2014
date: '2014-03-15T10:03:18+00:00'
format: image
service: flickr
tags:
- perth
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928277404_788e1c6824_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928277404_788e1c6824_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/15/epic-australian-adventure-2014-43/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/15/epic-australian-adventure-2014-43/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13928277404/) [10:03 am, March 15, 2014](http://dentedreality.com.au/2014/03/15/epic-australian-adventure-2014-43/ "10:03 am") 
jQuery(document).ready(function(){
var gmap\_m1aa4b9abd11568a451a7a4d265f7e820 = {
positions : {
950 : new google.maps.LatLng( '-32.046639', '115.731438' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1aa4b9abd11568a451a7a4d265f7e820' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1aa4b9abd11568a451a7a4d265f7e820.positions ) {
gmap\_m1aa4b9abd11568a451a7a4d265f7e820.bounds.extend( gmap\_m1aa4b9abd11568a451a7a4d265f7e820.positions[m] );
}
// Render markers
for ( var m in gmap\_m1aa4b9abd11568a451a7a4d265f7e820.positions ) {
gmap\_m1aa4b9abd11568a451a7a4d265f7e820.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1aa4b9abd11568a451a7a4d265f7e820.map,
position : gmap\_m1aa4b9abd11568a451a7a4d265f7e820.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1aa4b9abd11568a451a7a4d265f7e820.map.setCenter( gmap\_m1aa4b9abd11568a451a7a4d265f7e820.positions[950] );
});