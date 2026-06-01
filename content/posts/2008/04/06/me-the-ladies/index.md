---
title: Me & The Ladies
date: '2008-04-06T00:37:08-06:00'
format: image
service: flickr
tags:
- australia
- lucy
- maryann
- renniewedding
- timswedding
- westernaustraliadenmark
latitude: '-34.983877'
longitude: '117.298278'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184655/2433440396_bfb49a7ecc_o.jpg
---

[![Me & The Ladies](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184655/2433440396_bfb49a7ecc_o.jpg)](https://dentedreality.com.au/2008/04/06/me-the-ladies/) 
# [Me & The Ladies](https://dentedreality.com.au/2008/04/06/me-the-ladies/)

[![Me & The Ladies](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184655/2433440396_bfb49a7ecc_o.jpg)](http://www.flickr.com/photos/borkazoid/2433440396/)

-34.983877117.298278




* #[australia](https://dentedreality.com.au/tags/australia/)
* #[lucy](https://dentedreality.com.au/tags/lucy/)
* #[maryann](https://dentedreality.com.au/tags/maryann/)
* #[renniewedding](https://dentedreality.com.au/tags/renniewedding/)
* #[timswedding](https://dentedreality.com.au/tags/timswedding/)
* #[westernaustraliadenmark](https://dentedreality.com.au/tags/westernaustraliadenmark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2433440396/) [12:37 am, April 6, 2008](https://dentedreality.com.au/2008/04/06/me-the-ladies/ "12:37 am") 
jQuery(document).ready(function(){
var gmap\_m35a907cf12b9ee5bc424f1f034d3c933 = {
positions : {
553 : new google.maps.LatLng( '-34.983877', '117.298278' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m35a907cf12b9ee5bc424f1f034d3c933' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m35a907cf12b9ee5bc424f1f034d3c933.positions ) {
gmap\_m35a907cf12b9ee5bc424f1f034d3c933.bounds.extend( gmap\_m35a907cf12b9ee5bc424f1f034d3c933.positions[m] );
}
// Render markers
for ( var m in gmap\_m35a907cf12b9ee5bc424f1f034d3c933.positions ) {
gmap\_m35a907cf12b9ee5bc424f1f034d3c933.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m35a907cf12b9ee5bc424f1f034d3c933.map,
position : gmap\_m35a907cf12b9ee5bc424f1f034d3c933.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m35a907cf12b9ee5bc424f1f034d3c933.map.setCenter( gmap\_m35a907cf12b9ee5bc424f1f034d3c933.positions[553] );
});