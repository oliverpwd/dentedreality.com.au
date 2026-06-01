---
title: Black Beach
date: '2012-01-28T12:12:33+00:00'
format: image
service: flickr
tags:
- beach
- california
- sanfrancisco
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959569037_a39b8f977b_o.jpg?resize=607%2C813
---

[![Black Beach](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959569037_a39b8f977b_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/01/28/black-beach/) 
# [Black Beach](http://dentedreality.com.au/2012/01/28/black-beach/)

Ocean Beach, SF





* #[beach](http://dentedreality.com.au/tags/beach/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959569037/) [12:12 pm, January 28, 2012](http://dentedreality.com.au/2012/01/28/black-beach/ "12:12 pm") 
jQuery(document).ready(function(){
var gmap\_m74016ef0f17ed2ba0b533861eecc23df = {
positions : {
567 : new google.maps.LatLng( '37.743833', '-122.5085' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m74016ef0f17ed2ba0b533861eecc23df' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m74016ef0f17ed2ba0b533861eecc23df.positions ) {
gmap\_m74016ef0f17ed2ba0b533861eecc23df.bounds.extend( gmap\_m74016ef0f17ed2ba0b533861eecc23df.positions[m] );
}
// Render markers
for ( var m in gmap\_m74016ef0f17ed2ba0b533861eecc23df.positions ) {
gmap\_m74016ef0f17ed2ba0b533861eecc23df.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m74016ef0f17ed2ba0b533861eecc23df.map,
position : gmap\_m74016ef0f17ed2ba0b533861eecc23df.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m74016ef0f17ed2ba0b533861eecc23df.map.setCenter( gmap\_m74016ef0f17ed2ba0b533861eecc23df.positions[567] );
});