---
title: Lunch in the Park
date: '2009-12-12T12:33:48+00:00'
format: image
service: flickr
tags:
- beer
- chicken
- Chile
- eggs
- fries
- Santiago
- steak
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2009/12/4202697657_80ac773649_o.jpg?resize=607%2C455
---

[![Lunch in the Park](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2009/12/4202697657_80ac773649_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2009/12/12/lunch-in-the-park/) 
# [Lunch in the Park](http://dentedreality.com.au/2009/12/12/lunch-in-the-park/)





* #[beer](http://dentedreality.com.au/tags/beer/)
* #[chicken](http://dentedreality.com.au/tags/chicken/)
* #[Chile](http://dentedreality.com.au/tags/chile/)
* #[eggs](http://dentedreality.com.au/tags/eggs/)
* #[fries](http://dentedreality.com.au/tags/fries/)
* #[Santiago](http://dentedreality.com.au/tags/santiago/)
* #[steak](http://dentedreality.com.au/tags/steak/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4202697657/) [12:33 pm, December 12, 2009](http://dentedreality.com.au/2009/12/12/lunch-in-the-park/ "12:33 pm") 
jQuery(document).ready(function(){
var gmap\_m2b0159035039ea00aed7f1828e3ea2f3 = {
positions : {
235 : new google.maps.LatLng( '-33.388834', '-70.557334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2b0159035039ea00aed7f1828e3ea2f3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2b0159035039ea00aed7f1828e3ea2f3.positions ) {
gmap\_m2b0159035039ea00aed7f1828e3ea2f3.bounds.extend( gmap\_m2b0159035039ea00aed7f1828e3ea2f3.positions[m] );
}
// Render markers
for ( var m in gmap\_m2b0159035039ea00aed7f1828e3ea2f3.positions ) {
gmap\_m2b0159035039ea00aed7f1828e3ea2f3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2b0159035039ea00aed7f1828e3ea2f3.map,
position : gmap\_m2b0159035039ea00aed7f1828e3ea2f3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2b0159035039ea00aed7f1828e3ea2f3.map.setCenter( gmap\_m2b0159035039ea00aed7f1828e3ea2f3.positions[235] );
});