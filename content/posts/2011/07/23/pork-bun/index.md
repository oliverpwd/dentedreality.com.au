---
title: Pork Bun
date: '2011-07-23T18:42:47+00:00'
format: image
service: flickr
tags:
- porkbun
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6322934327_53276bb990_o.jpg?resize=607%2C813
---

[![Pork Bun](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6322934327_53276bb990_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/07/23/pork-bun/) 
# [Pork Bun](http://dentedreality.com.au/2011/07/23/pork-bun/)





* #[porkbun](http://dentedreality.com.au/tags/porkbun/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6322934327/) [6:42 pm, July 23, 2011](http://dentedreality.com.au/2011/07/23/pork-bun/ "6:42 pm") 
jQuery(document).ready(function(){
var gmap\_mdc763decbc2fb8e715b1b41100b8c965 = {
positions : {
854 : new google.maps.LatLng( '40.729166', '-73.984334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdc763decbc2fb8e715b1b41100b8c965' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdc763decbc2fb8e715b1b41100b8c965.positions ) {
gmap\_mdc763decbc2fb8e715b1b41100b8c965.bounds.extend( gmap\_mdc763decbc2fb8e715b1b41100b8c965.positions[m] );
}
// Render markers
for ( var m in gmap\_mdc763decbc2fb8e715b1b41100b8c965.positions ) {
gmap\_mdc763decbc2fb8e715b1b41100b8c965.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdc763decbc2fb8e715b1b41100b8c965.map,
position : gmap\_mdc763decbc2fb8e715b1b41100b8c965.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdc763decbc2fb8e715b1b41100b8c965.map.setCenter( gmap\_mdc763decbc2fb8e715b1b41100b8c965.positions[854] );
});