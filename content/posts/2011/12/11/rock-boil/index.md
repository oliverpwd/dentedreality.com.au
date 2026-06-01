---
title: Rock Boil
date: '2011-12-11T10:48:12+00:00'
format: image
service: flickr
tags:
- camping
- disaster
- outdoors
- survival
- wilderness
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6958326239_4e0c346b10_o.jpg?resize=607%2C452
---

[![Rock Boil](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6958326239_4e0c346b10_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/12/11/rock-boil/) 
# [Rock Boil](http://dentedreality.com.au/2011/12/11/rock-boil/)

Boiling water using fire-heated rocks placed in a carved out log.





* #[camping](http://dentedreality.com.au/tags/camping/)
* #[disaster](http://dentedreality.com.au/tags/disaster/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[survival](http://dentedreality.com.au/tags/survival/)
* #[wilderness](http://dentedreality.com.au/tags/wilderness/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958326239/) [10:48 am, December 11, 2011](http://dentedreality.com.au/2011/12/11/rock-boil/ "10:48 am") 
jQuery(document).ready(function(){
var gmap\_m08ac44be1531ff91a2c6d04c7146430a = {
positions : {
739 : new google.maps.LatLng( '38.000166', '-122.6125' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m08ac44be1531ff91a2c6d04c7146430a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m08ac44be1531ff91a2c6d04c7146430a.positions ) {
gmap\_m08ac44be1531ff91a2c6d04c7146430a.bounds.extend( gmap\_m08ac44be1531ff91a2c6d04c7146430a.positions[m] );
}
// Render markers
for ( var m in gmap\_m08ac44be1531ff91a2c6d04c7146430a.positions ) {
gmap\_m08ac44be1531ff91a2c6d04c7146430a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m08ac44be1531ff91a2c6d04c7146430a.map,
position : gmap\_m08ac44be1531ff91a2c6d04c7146430a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m08ac44be1531ff91a2c6d04c7146430a.map.setCenter( gmap\_m08ac44be1531ff91a2c6d04c7146430a.positions[739] );
});