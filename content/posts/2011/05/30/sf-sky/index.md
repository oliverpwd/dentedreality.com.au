---
title: SF Sky
date: '2011-05-30T10:42:37+00:00'
format: image
service: flickr
tags:
- sanfrancisco
- sky
- sun
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802879179_71763d40c3_o.jpg?resize=607%2C452
---

[![SF Sky](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802879179_71763d40c3_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/30/sf-sky/) 
# [SF Sky](http://dentedreality.com.au/2011/05/30/sf-sky/)





* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[sky](http://dentedreality.com.au/tags/sky/)
* #[sun](http://dentedreality.com.au/tags/sun/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802879179/) [10:42 am, May 30, 2011](http://dentedreality.com.au/2011/05/30/sf-sky/ "10:42 am") 
jQuery(document).ready(function(){
var gmap\_m20b2d5334fb2b0a733e70b4a0c483e25 = {
positions : {
597 : new google.maps.LatLng( '37.781333', '-122.403501' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m20b2d5334fb2b0a733e70b4a0c483e25' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m20b2d5334fb2b0a733e70b4a0c483e25.positions ) {
gmap\_m20b2d5334fb2b0a733e70b4a0c483e25.bounds.extend( gmap\_m20b2d5334fb2b0a733e70b4a0c483e25.positions[m] );
}
// Render markers
for ( var m in gmap\_m20b2d5334fb2b0a733e70b4a0c483e25.positions ) {
gmap\_m20b2d5334fb2b0a733e70b4a0c483e25.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m20b2d5334fb2b0a733e70b4a0c483e25.map,
position : gmap\_m20b2d5334fb2b0a733e70b4a0c483e25.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m20b2d5334fb2b0a733e70b4a0c483e25.map.setCenter( gmap\_m20b2d5334fb2b0a733e70b4a0c483e25.positions[597] );
});