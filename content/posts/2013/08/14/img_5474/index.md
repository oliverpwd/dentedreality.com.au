---
title: Peter Luger’s Steakhouse
date: '2013-08-14T18:24:04+00:00'
format: image
service: flickr
tags:
- dinner
- peter luger
- steak
- steakhouse
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767768902_fe44dd57d8_o.jpg?resize=607%2C452
---

[![IMG_5474](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767768902_fe44dd57d8_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/08/14/img_5474/) 
# [Peter Luger’s Steakhouse](http://dentedreality.com.au/2013/08/14/img_5474/)





* #[dinner](http://dentedreality.com.au/tags/dinner/)
* #[peter luger](http://dentedreality.com.au/tags/peter-luger/)
* #[steak](http://dentedreality.com.au/tags/steak/)
* #[steakhouse](http://dentedreality.com.au/tags/steakhouse/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9767768902/) [6:24 pm, August 14, 2013](http://dentedreality.com.au/2013/08/14/img_5474/ "6:24 pm") 
jQuery(document).ready(function(){
var gmap\_m745a42fec1af0281c8d0a4cc457d330e = {
positions : {
921 : new google.maps.LatLng( '40.71', '-73.962334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m745a42fec1af0281c8d0a4cc457d330e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m745a42fec1af0281c8d0a4cc457d330e.positions ) {
gmap\_m745a42fec1af0281c8d0a4cc457d330e.bounds.extend( gmap\_m745a42fec1af0281c8d0a4cc457d330e.positions[m] );
}
// Render markers
for ( var m in gmap\_m745a42fec1af0281c8d0a4cc457d330e.positions ) {
gmap\_m745a42fec1af0281c8d0a4cc457d330e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m745a42fec1af0281c8d0a4cc457d330e.map,
position : gmap\_m745a42fec1af0281c8d0a4cc457d330e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m745a42fec1af0281c8d0a4cc457d330e.map.setCenter( gmap\_m745a42fec1af0281c8d0a4cc457d330e.positions[921] );
});