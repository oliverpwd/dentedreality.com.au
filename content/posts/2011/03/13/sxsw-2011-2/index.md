---
title: SXSW 2011
date: '2011-03-13T13:38:20+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2011
- texas
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802657014_22e6cc0736_o.jpg?resize=607%2C813
---

[![SXSW 2011](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802657014_22e6cc0736_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/03/13/sxsw-2011-2/) 
# [SXSW 2011](http://dentedreality.com.au/2011/03/13/sxsw-2011-2/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2011](http://dentedreality.com.au/tags/sxsw2011/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802657014/) [1:38 pm, March 13, 2011](http://dentedreality.com.au/2011/03/13/sxsw-2011-2/ "1:38 pm") 
jQuery(document).ready(function(){
var gmap\_ma5733b5a9abb61d8695f0958f5626d37 = {
positions : {
843 : new google.maps.LatLng( '30.264', '-97.739834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma5733b5a9abb61d8695f0958f5626d37' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma5733b5a9abb61d8695f0958f5626d37.positions ) {
gmap\_ma5733b5a9abb61d8695f0958f5626d37.bounds.extend( gmap\_ma5733b5a9abb61d8695f0958f5626d37.positions[m] );
}
// Render markers
for ( var m in gmap\_ma5733b5a9abb61d8695f0958f5626d37.positions ) {
gmap\_ma5733b5a9abb61d8695f0958f5626d37.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma5733b5a9abb61d8695f0958f5626d37.map,
position : gmap\_ma5733b5a9abb61d8695f0958f5626d37.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma5733b5a9abb61d8695f0958f5626d37.map.setCenter( gmap\_ma5733b5a9abb61d8695f0958f5626d37.positions[843] );
});