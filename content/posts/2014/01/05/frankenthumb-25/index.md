---
title: Frankenthumb
date: '2014-01-05T08:17:34+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- Frankenthumb
- me
---

[![Frankenthumb](http://i2.wp.com/farm8.staticflickr.com/7338/13925241084_813a25dbac_o.jpg?w=607)](http://dentedreality.com.au/2014/01/05/frankenthumb-25/) 
# [Frankenthumb](http://dentedreality.com.au/2014/01/05/frankenthumb-25/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)
* #[me](http://dentedreality.com.au/tags/me/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13925241084/) [8:17 am, January 5, 2014](http://dentedreality.com.au/2014/01/05/frankenthumb-25/ "8:17 am") 
jQuery(document).ready(function(){
var gmap\_m2bd9c2f3df225874363db8c71abf1f2e = {
positions : {
232 : new google.maps.LatLng( '40.670169', '-73.985573' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2bd9c2f3df225874363db8c71abf1f2e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2bd9c2f3df225874363db8c71abf1f2e.positions ) {
gmap\_m2bd9c2f3df225874363db8c71abf1f2e.bounds.extend( gmap\_m2bd9c2f3df225874363db8c71abf1f2e.positions[m] );
}
// Render markers
for ( var m in gmap\_m2bd9c2f3df225874363db8c71abf1f2e.positions ) {
gmap\_m2bd9c2f3df225874363db8c71abf1f2e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2bd9c2f3df225874363db8c71abf1f2e.map,
position : gmap\_m2bd9c2f3df225874363db8c71abf1f2e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2bd9c2f3df225874363db8c71abf1f2e.map.setCenter( gmap\_m2bd9c2f3df225874363db8c71abf1f2e.positions[232] );
});