---
title: Dinner on the Maritol
date: '2012-02-02T17:53:56+00:00'
format: image
service: flickr
tags:
- boat
- houseboat
- maritol
- ship
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959569827_41b87bcb16_o.jpg?resize=607%2C452
---

[![Dinner on the Maritol](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959569827_41b87bcb16_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/02/02/dinner-on-the-maritol-3/) 
# [Dinner on the Maritol](http://dentedreality.com.au/2012/02/02/dinner-on-the-maritol-3/)

@chexee was moving off the Maritol, so we went around for a going away dinner.





* #[boat](http://dentedreality.com.au/tags/boat/)
* #[houseboat](http://dentedreality.com.au/tags/houseboat/)
* #[maritol](http://dentedreality.com.au/tags/maritol/)
* #[ship](http://dentedreality.com.au/tags/ship/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959569827/) [5:53 pm, February 2, 2012](http://dentedreality.com.au/2012/02/02/dinner-on-the-maritol-3/ "5:53 pm") 
jQuery(document).ready(function(){
var gmap\_mdcb62ad09884f887d1df7d63666111fb = {
positions : {
991 : new google.maps.LatLng( '37.7735', '-122.385167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdcb62ad09884f887d1df7d63666111fb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdcb62ad09884f887d1df7d63666111fb.positions ) {
gmap\_mdcb62ad09884f887d1df7d63666111fb.bounds.extend( gmap\_mdcb62ad09884f887d1df7d63666111fb.positions[m] );
}
// Render markers
for ( var m in gmap\_mdcb62ad09884f887d1df7d63666111fb.positions ) {
gmap\_mdcb62ad09884f887d1df7d63666111fb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdcb62ad09884f887d1df7d63666111fb.map,
position : gmap\_mdcb62ad09884f887d1df7d63666111fb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdcb62ad09884f887d1df7d63666111fb.map.setCenter( gmap\_mdcb62ad09884f887d1df7d63666111fb.positions[991] );
});