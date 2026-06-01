---
title: Dinner on the Maritol
date: '2012-02-02T17:55:07+00:00'
format: image
service: flickr
tags:
- boat
- houseboat
- maritol
- ship
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813457900_696d5d9e5d_o.jpg?resize=607%2C452
---

[![Dinner on the Maritol](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813457900_696d5d9e5d_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/02/02/dinner-on-the-maritol-2/) 
# [Dinner on the Maritol](http://dentedreality.com.au/2012/02/02/dinner-on-the-maritol-2/)

@chexee was moving off the Maritol, so we went around for a going away dinner.





* #[boat](http://dentedreality.com.au/tags/boat/)
* #[houseboat](http://dentedreality.com.au/tags/houseboat/)
* #[maritol](http://dentedreality.com.au/tags/maritol/)
* #[ship](http://dentedreality.com.au/tags/ship/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813457900/) [5:55 pm, February 2, 2012](http://dentedreality.com.au/2012/02/02/dinner-on-the-maritol-2/ "5:55 pm") 
jQuery(document).ready(function(){
var gmap\_m32902f1bb4f310c9e56d6604dd91a3a4 = {
positions : {
375 : new google.maps.LatLng( '37.773333', '-122.385167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m32902f1bb4f310c9e56d6604dd91a3a4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m32902f1bb4f310c9e56d6604dd91a3a4.positions ) {
gmap\_m32902f1bb4f310c9e56d6604dd91a3a4.bounds.extend( gmap\_m32902f1bb4f310c9e56d6604dd91a3a4.positions[m] );
}
// Render markers
for ( var m in gmap\_m32902f1bb4f310c9e56d6604dd91a3a4.positions ) {
gmap\_m32902f1bb4f310c9e56d6604dd91a3a4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m32902f1bb4f310c9e56d6604dd91a3a4.map,
position : gmap\_m32902f1bb4f310c9e56d6604dd91a3a4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m32902f1bb4f310c9e56d6604dd91a3a4.map.setCenter( gmap\_m32902f1bb4f310c9e56d6604dd91a3a4.positions[375] );
});