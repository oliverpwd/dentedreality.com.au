---
title: Rock Garden
date: '2011-01-10T11:40:22+00:00'
format: image
service: flickr
tags:
- garden
- rockgarden
- zen
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434722774_90c249e2cd_o.jpg?resize=607%2C813
---

[![Rock Garden](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434722774_90c249e2cd_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/01/10/rock-garden/) 
# [Rock Garden](http://dentedreality.com.au/2011/01/10/rock-garden/)





* #[garden](http://dentedreality.com.au/tags/garden/)
* #[rockgarden](http://dentedreality.com.au/tags/rockgarden/)
* #[zen](http://dentedreality.com.au/tags/zen/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434722774/) [11:40 am, January 10, 2011](http://dentedreality.com.au/2011/01/10/rock-garden/ "11:40 am") 
jQuery(document).ready(function(){
var gmap\_m7f2e8afd22a307d675a3fa04133a2074 = {
positions : {
36 : new google.maps.LatLng( '-32.0635', '115.936' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7f2e8afd22a307d675a3fa04133a2074' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7f2e8afd22a307d675a3fa04133a2074.positions ) {
gmap\_m7f2e8afd22a307d675a3fa04133a2074.bounds.extend( gmap\_m7f2e8afd22a307d675a3fa04133a2074.positions[m] );
}
// Render markers
for ( var m in gmap\_m7f2e8afd22a307d675a3fa04133a2074.positions ) {
gmap\_m7f2e8afd22a307d675a3fa04133a2074.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7f2e8afd22a307d675a3fa04133a2074.map,
position : gmap\_m7f2e8afd22a307d675a3fa04133a2074.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7f2e8afd22a307d675a3fa04133a2074.map.setCenter( gmap\_m7f2e8afd22a307d675a3fa04133a2074.positions[36] );
});