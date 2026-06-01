---
title: Epic Australian Adventure, 2014
date: '2014-03-19T03:23:55+00:00'
format: image
service: flickr
tags:
- perth
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904718876_eea8427e44_o.jpg?resize=607%2C809
---

[![Epic Australian Adventure, 2014](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904718876_eea8427e44_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2014/03/19/epic-australian-adventure-2014-19/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/19/epic-australian-adventure-2014-19/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904718876/) [3:23 am, March 19, 2014](http://dentedreality.com.au/2014/03/19/epic-australian-adventure-2014-19/ "3:23 am") 
jQuery(document).ready(function(){
var gmap\_m3061d9525f996f2d9d349aaaca845511 = {
positions : {
257 : new google.maps.LatLng( '-31.99507', '115.751908' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3061d9525f996f2d9d349aaaca845511' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3061d9525f996f2d9d349aaaca845511.positions ) {
gmap\_m3061d9525f996f2d9d349aaaca845511.bounds.extend( gmap\_m3061d9525f996f2d9d349aaaca845511.positions[m] );
}
// Render markers
for ( var m in gmap\_m3061d9525f996f2d9d349aaaca845511.positions ) {
gmap\_m3061d9525f996f2d9d349aaaca845511.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3061d9525f996f2d9d349aaaca845511.map,
position : gmap\_m3061d9525f996f2d9d349aaaca845511.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3061d9525f996f2d9d349aaaca845511.map.setCenter( gmap\_m3061d9525f996f2d9d349aaaca845511.positions[257] );
});