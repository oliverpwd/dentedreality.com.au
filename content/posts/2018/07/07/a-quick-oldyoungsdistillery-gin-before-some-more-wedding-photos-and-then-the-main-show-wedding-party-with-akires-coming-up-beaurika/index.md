---
title: ''
date: '2018-07-07T16:17:17-06:00'
format: image
service: instagram
tags:
- beaurika
latitude: '39.7572'
longitude: '-104.967'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/07/14182133/36615758_1717301565043820_734347551150440448_n.jpg?resize=607%2C607&ssl=1
---

[![A quick @oldyoungsdistillery gin before some more wedding photos and then the main show. Wedding party with @akires coming up. #beaurika](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/07/14182133/36615758_1717301565043820_734347551150440448_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/07/07/a-quick-oldyoungsdistillery-gin-before-some-more-wedding-photos-and-then-the-main-show-wedding-party-with-akires-coming-up-beaurika/) 

[![A quick @oldyoungsdistillery gin before some more wedding photos and then the main show. Wedding party with @akires coming up. #beaurika](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/07/14182133/36615758_1717301565043820_734347551150440448_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/Bk8mf9UFPbI/)

A quick @oldyoungsdistillery gin before some more wedding photos and then the main show. Wedding party with @akires coming up. #beaurika

39.7572-104.967




* #[beaurika](https://dentedreality.com.au/tags/beaurika/)

Posted on [Instagram](https://www.instagram.com/p/Bk8mf9UFPbI/) [4:17 pm, July 7, 2018](https://dentedreality.com.au/2018/07/07/a-quick-oldyoungsdistillery-gin-before-some-more-wedding-photos-and-then-the-main-show-wedding-party-with-akires-coming-up-beaurika/ "4:17 pm") 
jQuery(document).ready(function(){
var gmap\_ma8b52464687f518afe6cf9bf87a83a7b = {
positions : {
748 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma8b52464687f518afe6cf9bf87a83a7b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma8b52464687f518afe6cf9bf87a83a7b.positions ) {
gmap\_ma8b52464687f518afe6cf9bf87a83a7b.bounds.extend( gmap\_ma8b52464687f518afe6cf9bf87a83a7b.positions[m] );
}
// Render markers
for ( var m in gmap\_ma8b52464687f518afe6cf9bf87a83a7b.positions ) {
gmap\_ma8b52464687f518afe6cf9bf87a83a7b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma8b52464687f518afe6cf9bf87a83a7b.map,
position : gmap\_ma8b52464687f518afe6cf9bf87a83a7b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma8b52464687f518afe6cf9bf87a83a7b.map.setCenter( gmap\_ma8b52464687f518afe6cf9bf87a83a7b.positions[748] );
});