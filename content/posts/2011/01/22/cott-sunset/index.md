---
title: Cott Sunset
date: '2011-01-22T15:22:13+00:00'
format: image
service: flickr
tags:
- australia
- beach
- cottesloe
- sunset
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434176895_09d0a91b4f_o.jpg?resize=607%2C452
---

[![Cott Sunset](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434176895_09d0a91b4f_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/22/cott-sunset/) 
# [Cott Sunset](http://dentedreality.com.au/2011/01/22/cott-sunset/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[cottesloe](http://dentedreality.com.au/tags/cottesloe/)
* #[sunset](http://dentedreality.com.au/tags/sunset/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434176895/) [3:22 pm, January 22, 2011](http://dentedreality.com.au/2011/01/22/cott-sunset/ "3:22 pm") 
jQuery(document).ready(function(){
var gmap\_m5ab708b8085e2db83d37aa397e80aef6 = {
positions : {
765 : new google.maps.LatLng( '-31.994667', '115.7515' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5ab708b8085e2db83d37aa397e80aef6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5ab708b8085e2db83d37aa397e80aef6.positions ) {
gmap\_m5ab708b8085e2db83d37aa397e80aef6.bounds.extend( gmap\_m5ab708b8085e2db83d37aa397e80aef6.positions[m] );
}
// Render markers
for ( var m in gmap\_m5ab708b8085e2db83d37aa397e80aef6.positions ) {
gmap\_m5ab708b8085e2db83d37aa397e80aef6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5ab708b8085e2db83d37aa397e80aef6.map,
position : gmap\_m5ab708b8085e2db83d37aa397e80aef6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5ab708b8085e2db83d37aa397e80aef6.map.setCenter( gmap\_m5ab708b8085e2db83d37aa397e80aef6.positions[765] );
});