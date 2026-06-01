---
title: San Francisco Buildings
date: '2011-02-03T15:41:12+00:00'
format: image
service: flickr
tags:
- building
- california
- city
- sanfrancisco
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802052835_5ca9f8d79f_o.jpg?resize=607%2C452
---

[![San Francisco Buildings](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802052835_5ca9f8d79f_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/02/03/san-francisco-buildings/) 
# [San Francisco Buildings](http://dentedreality.com.au/2011/02/03/san-francisco-buildings/)





* #[building](http://dentedreality.com.au/tags/building/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[city](http://dentedreality.com.au/tags/city/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802052835/) [3:41 pm, February 3, 2011](http://dentedreality.com.au/2011/02/03/san-francisco-buildings/ "3:41 pm") 
jQuery(document).ready(function(){
var gmap\_m349c02b0786f1bb478d1cf8908d329ce = {
positions : {
802 : new google.maps.LatLng( '37.793666', '-122.396' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m349c02b0786f1bb478d1cf8908d329ce' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m349c02b0786f1bb478d1cf8908d329ce.positions ) {
gmap\_m349c02b0786f1bb478d1cf8908d329ce.bounds.extend( gmap\_m349c02b0786f1bb478d1cf8908d329ce.positions[m] );
}
// Render markers
for ( var m in gmap\_m349c02b0786f1bb478d1cf8908d329ce.positions ) {
gmap\_m349c02b0786f1bb478d1cf8908d329ce.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m349c02b0786f1bb478d1cf8908d329ce.map,
position : gmap\_m349c02b0786f1bb478d1cf8908d329ce.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m349c02b0786f1bb478d1cf8908d329ce.map.setCenter( gmap\_m349c02b0786f1bb478d1cf8908d329ce.positions[802] );
});