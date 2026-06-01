---
title: Anthony’s Nose
date: '2013-08-24T10:02:20+00:00'
format: image
tags:
- anthony's nose
- bear mountain
- hiking
- new york
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767765521_dd7b95e29a_o.jpg?resize=607%2C452
---

[![IMG_5508](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767765521_dd7b95e29a_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/08/24/img_5508/) 
# [Anthony’s Nose](http://dentedreality.com.au/2013/08/24/img_5508/)





* #[anthony's nose](http://dentedreality.com.au/tags/anthonys-nose/)
* #[bear mountain](http://dentedreality.com.au/tags/bear-mountain/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[new york](http://dentedreality.com.au/tags/new-york/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9767765521/) [10:02 am, August 24, 2013](http://dentedreality.com.au/2013/08/24/img_5508/ "10:02 am") 
jQuery(document).ready(function(){
var gmap\_mcf860e7caf00d9d0653d90e93995a63c = {
positions : {
881 : new google.maps.LatLng( '41.32', '-73.974334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mcf860e7caf00d9d0653d90e93995a63c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mcf860e7caf00d9d0653d90e93995a63c.positions ) {
gmap\_mcf860e7caf00d9d0653d90e93995a63c.bounds.extend( gmap\_mcf860e7caf00d9d0653d90e93995a63c.positions[m] );
}
// Render markers
for ( var m in gmap\_mcf860e7caf00d9d0653d90e93995a63c.positions ) {
gmap\_mcf860e7caf00d9d0653d90e93995a63c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mcf860e7caf00d9d0653d90e93995a63c.map,
position : gmap\_mcf860e7caf00d9d0653d90e93995a63c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mcf860e7caf00d9d0653d90e93995a63c.map.setCenter( gmap\_mcf860e7caf00d9d0653d90e93995a63c.positions[881] );
});