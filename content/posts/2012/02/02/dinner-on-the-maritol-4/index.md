---
title: Dinner on the Maritol
date: '2012-02-02T15:20:54+00:00'
format: image
service: flickr
tags:
- boat
- houseboat
- maritol
- ship
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959569531_bec0243196_o.jpg?resize=607%2C452
---

[![Dinner on the Maritol](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959569531_bec0243196_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/02/02/dinner-on-the-maritol-4/) 
# [Dinner on the Maritol](http://dentedreality.com.au/2012/02/02/dinner-on-the-maritol-4/)

@chexee was moving off the Maritol, so we went around for a going away dinner.





* #[boat](http://dentedreality.com.au/tags/boat/)
* #[houseboat](http://dentedreality.com.au/tags/houseboat/)
* #[maritol](http://dentedreality.com.au/tags/maritol/)
* #[ship](http://dentedreality.com.au/tags/ship/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959569531/) [3:20 pm, February 2, 2012](http://dentedreality.com.au/2012/02/02/dinner-on-the-maritol-4/ "3:20 pm") 
jQuery(document).ready(function(){
var gmap\_m9c08cfce616d0ec3e3480ba09940c05d = {
positions : {
132 : new google.maps.LatLng( '37.773166', '-122.385167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9c08cfce616d0ec3e3480ba09940c05d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9c08cfce616d0ec3e3480ba09940c05d.positions ) {
gmap\_m9c08cfce616d0ec3e3480ba09940c05d.bounds.extend( gmap\_m9c08cfce616d0ec3e3480ba09940c05d.positions[m] );
}
// Render markers
for ( var m in gmap\_m9c08cfce616d0ec3e3480ba09940c05d.positions ) {
gmap\_m9c08cfce616d0ec3e3480ba09940c05d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9c08cfce616d0ec3e3480ba09940c05d.map,
position : gmap\_m9c08cfce616d0ec3e3480ba09940c05d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9c08cfce616d0ec3e3480ba09940c05d.map.setCenter( gmap\_m9c08cfce616d0ec3e3480ba09940c05d.positions[132] );
});