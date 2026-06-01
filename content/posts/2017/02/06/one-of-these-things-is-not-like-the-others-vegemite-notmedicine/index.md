---
title: ''
date: '2017-02-06T14:51:22+00:00'
format: image
service: instagram
tags:
- notmedicine
- vegemite
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16230821_1428305270514166_7352919440213671936_n.jpg?fit=640%2C640
---

[![One of these things is not like the others. #vegemite #notmedicine](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16230821_1428305270514166_7352919440213671936_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2017/02/06/one-of-these-things-is-not-like-the-others-vegemite-notmedicine/) 

One of these things is not like the others. #vegemite #notmedicine





* #[notmedicine](http://dentedreality.com.au/tags/notmedicine/)
* #[vegemite](http://dentedreality.com.au/tags/vegemite/)

Posted on [Instagram](https://www.instagram.com/p/BQL5Wp8jijO/) [2:51 pm, February 6, 2017](http://dentedreality.com.au/2017/02/06/one-of-these-things-is-not-like-the-others-vegemite-notmedicine/ "2:51 pm") 
jQuery(document).ready(function(){
var gmap\_mcb89be7979aaf70eb954b5190d0aa66c = {
positions : {
553 : new google.maps.LatLng( '37.784161540494', '-122.39733877818' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mcb89be7979aaf70eb954b5190d0aa66c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mcb89be7979aaf70eb954b5190d0aa66c.positions ) {
gmap\_mcb89be7979aaf70eb954b5190d0aa66c.bounds.extend( gmap\_mcb89be7979aaf70eb954b5190d0aa66c.positions[m] );
}
// Render markers
for ( var m in gmap\_mcb89be7979aaf70eb954b5190d0aa66c.positions ) {
gmap\_mcb89be7979aaf70eb954b5190d0aa66c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mcb89be7979aaf70eb954b5190d0aa66c.map,
position : gmap\_mcb89be7979aaf70eb954b5190d0aa66c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mcb89be7979aaf70eb954b5190d0aa66c.map.setCenter( gmap\_mcb89be7979aaf70eb954b5190d0aa66c.positions[553] );
});