---
title: ''
date: '2016-09-03T13:10:29+00:00'
format: image
service: instagram
tags:
- 14er
- colorado
- mtbierstadt
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14156478_659111074255286_599544299_n.jpg?fit=640%2C640
---

[![Incredible views from up here. #mtbierstadt #colorado #14er](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14156478_659111074255286_599544299_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/09/03/incredible-views-from-up-here-mtbierstadt-colorado-14er/) 

Incredible views from up here. #mtbierstadt #colorado #14er





* #[14er](http://dentedreality.com.au/tags/14er/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[mtbierstadt](http://dentedreality.com.au/tags/mtbierstadt/)

Posted on [Instagram](https://www.instagram.com/p/BJ5672wA6u2/) [1:10 pm, September 3, 2016](http://dentedreality.com.au/2016/09/03/incredible-views-from-up-here-mtbierstadt-colorado-14er/ "1:10 pm") 
jQuery(document).ready(function(){
var gmap\_m7cb27544708bcaabbbadb20159c42cae = {
positions : {
23 : new google.maps.LatLng( '39.58261494', '-105.66885861' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7cb27544708bcaabbbadb20159c42cae' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7cb27544708bcaabbbadb20159c42cae.positions ) {
gmap\_m7cb27544708bcaabbbadb20159c42cae.bounds.extend( gmap\_m7cb27544708bcaabbbadb20159c42cae.positions[m] );
}
// Render markers
for ( var m in gmap\_m7cb27544708bcaabbbadb20159c42cae.positions ) {
gmap\_m7cb27544708bcaabbbadb20159c42cae.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7cb27544708bcaabbbadb20159c42cae.map,
position : gmap\_m7cb27544708bcaabbbadb20159c42cae.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7cb27544708bcaabbbadb20159c42cae.map.setCenter( gmap\_m7cb27544708bcaabbbadb20159c42cae.positions[23] );
});