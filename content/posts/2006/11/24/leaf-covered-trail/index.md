---
title: Leaf-Covered Trail
date: '2006-11-24T10:26:54+00:00'
format: image
service: flickr
tags:
- bigsur
- bottchersgap
- california
- leaves
- lospadresnationalpark
- trail
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/11/308101524_e75579fb58_o.jpg?resize=607%2C809
---

[![Leaf-Covered Trail](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/11/308101524_e75579fb58_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2006/11/24/leaf-covered-trail/) 
# [Leaf-Covered Trail](http://dentedreality.com.au/2006/11/24/leaf-covered-trail/)

Lots of sections like this.





* #[bigsur](http://dentedreality.com.au/tags/bigsur/)
* #[bottchersgap](http://dentedreality.com.au/tags/bottchersgap/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[leaves](http://dentedreality.com.au/tags/leaves/)
* #[lospadresnationalpark](http://dentedreality.com.au/tags/lospadresnationalpark/)
* #[trail](http://dentedreality.com.au/tags/trail/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/308101524/) [10:26 am, November 24, 2006](http://dentedreality.com.au/2006/11/24/leaf-covered-trail/ "10:26 am") 
jQuery(document).ready(function(){
var gmap\_mfdfecbd134b263a61d828d91ba704761 = {
positions : {
64 : new google.maps.LatLng( '36.34389', '-121.776409' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mfdfecbd134b263a61d828d91ba704761' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mfdfecbd134b263a61d828d91ba704761.positions ) {
gmap\_mfdfecbd134b263a61d828d91ba704761.bounds.extend( gmap\_mfdfecbd134b263a61d828d91ba704761.positions[m] );
}
// Render markers
for ( var m in gmap\_mfdfecbd134b263a61d828d91ba704761.positions ) {
gmap\_mfdfecbd134b263a61d828d91ba704761.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mfdfecbd134b263a61d828d91ba704761.map,
position : gmap\_mfdfecbd134b263a61d828d91ba704761.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mfdfecbd134b263a61d828d91ba704761.map.setCenter( gmap\_mfdfecbd134b263a61d828d91ba704761.positions[64] );
});