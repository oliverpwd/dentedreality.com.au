---
title: ''
date: '2016-08-11T19:28:10+00:00'
format: image
service: instagram
tags:
- colorado
- coloradonationalmonument
- nationalmonument
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13649102_1093400830777739_744319802_n.jpg?fit=640%2C640
---

[![View from tonight's campsite. #colorado #nationalmonument #coloradonationalmonument](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13649102_1093400830777739_744319802_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/08/11/view-from-tonights-campsite-colorado-nationalmonument-coloradonationalmonument/) 

View from tonight’s campsite. #colorado #nationalmonument #coloradonationalmonument





* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[coloradonationalmonument](http://dentedreality.com.au/tags/coloradonationalmonument/)
* #[nationalmonument](http://dentedreality.com.au/tags/nationalmonument/)

Posted on [Instagram](https://www.instagram.com/p/BI_X35JgGoa/) [7:28 pm, August 11, 2016](http://dentedreality.com.au/2016/08/11/view-from-tonights-campsite-colorado-nationalmonument-coloradonationalmonument/ "7:28 pm") 
jQuery(document).ready(function(){
var gmap\_mb3616006c2ba13a20e8daf21ee5c7704 = {
positions : {
558 : new google.maps.LatLng( '39.100965816009', '-108.73441429808' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb3616006c2ba13a20e8daf21ee5c7704' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb3616006c2ba13a20e8daf21ee5c7704.positions ) {
gmap\_mb3616006c2ba13a20e8daf21ee5c7704.bounds.extend( gmap\_mb3616006c2ba13a20e8daf21ee5c7704.positions[m] );
}
// Render markers
for ( var m in gmap\_mb3616006c2ba13a20e8daf21ee5c7704.positions ) {
gmap\_mb3616006c2ba13a20e8daf21ee5c7704.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb3616006c2ba13a20e8daf21ee5c7704.map,
position : gmap\_mb3616006c2ba13a20e8daf21ee5c7704.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb3616006c2ba13a20e8daf21ee5c7704.map.setCenter( gmap\_mb3616006c2ba13a20e8daf21ee5c7704.positions[558] );
});