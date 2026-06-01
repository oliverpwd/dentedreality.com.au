---
title: Butterfly By The Beach
date: '2006-12-29T17:51:43+00:00'
format: image
service: flickr
tags:
- butterfly
- macro
- phuket
- thailand
- thailand06
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348092281_9ddc52b620_o.jpg?resize=607%2C455
---

[![Butterfly By The Beach](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348092281_9ddc52b620_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/29/butterfly-by-the-beach/) 
# [Butterfly By The Beach](http://dentedreality.com.au/2006/12/29/butterfly-by-the-beach/)





* #[butterfly](http://dentedreality.com.au/tags/butterfly/)
* #[macro](http://dentedreality.com.au/tags/macro/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348092281/) [5:51 pm, December 29, 2006](http://dentedreality.com.au/2006/12/29/butterfly-by-the-beach/ "5:51 pm") 
jQuery(document).ready(function(){
var gmap\_ma268f5f671967f0d45fe16142657e248 = {
positions : {
152 : new google.maps.LatLng( '7.955282', '98.282489' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma268f5f671967f0d45fe16142657e248' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma268f5f671967f0d45fe16142657e248.positions ) {
gmap\_ma268f5f671967f0d45fe16142657e248.bounds.extend( gmap\_ma268f5f671967f0d45fe16142657e248.positions[m] );
}
// Render markers
for ( var m in gmap\_ma268f5f671967f0d45fe16142657e248.positions ) {
gmap\_ma268f5f671967f0d45fe16142657e248.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma268f5f671967f0d45fe16142657e248.map,
position : gmap\_ma268f5f671967f0d45fe16142657e248.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma268f5f671967f0d45fe16142657e248.map.setCenter( gmap\_ma268f5f671967f0d45fe16142657e248.positions[152] );
});