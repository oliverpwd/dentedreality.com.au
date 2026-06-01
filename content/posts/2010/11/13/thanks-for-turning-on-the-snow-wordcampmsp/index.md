---
title: ''
date: '2010-11-13T11:19:22-07:00'
format: image
service: instagram
tags:
- photo
- wordcampmsp
latitude: '44.8639605'
longitude: '-93.3058548'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/11/14191004/1ef22864024e460dabaee4498b0eb94b_7.jpg
---

[![Thanks for turning on the snow #wordcampmsp](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/11/14191004/1ef22864024e460dabaee4498b0eb94b_7.jpg)](https://dentedreality.com.au/2010/11/13/thanks-for-turning-on-the-snow-wordcampmsp/) 

[![Thanks for turning on the snow #wordcampmsp](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/11/14191004/1ef22864024e460dabaee4498b0eb94b_7.jpg)](http://instagram.com/p/PU9o/)

Thanks for turning on the snow #wordcampmsp

44.8639605-93.3058548




* #[photo](https://dentedreality.com.au/tags/photo/)
* #[wordcampmsp](https://dentedreality.com.au/tags/wordcampmsp/)

Posted on [Instagram](http://instagram.com/p/PU9o/) [11:19 am, November 13, 2010](https://dentedreality.com.au/2010/11/13/thanks-for-turning-on-the-snow-wordcampmsp/ "11:19 am") 
jQuery(document).ready(function(){
var gmap\_m47f45cfd7fbdad89458bd718562c3c8f = {
positions : {
555 : new google.maps.LatLng( '44.863960483', '-93.305854797' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m47f45cfd7fbdad89458bd718562c3c8f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m47f45cfd7fbdad89458bd718562c3c8f.positions ) {
gmap\_m47f45cfd7fbdad89458bd718562c3c8f.bounds.extend( gmap\_m47f45cfd7fbdad89458bd718562c3c8f.positions[m] );
}
// Render markers
for ( var m in gmap\_m47f45cfd7fbdad89458bd718562c3c8f.positions ) {
gmap\_m47f45cfd7fbdad89458bd718562c3c8f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m47f45cfd7fbdad89458bd718562c3c8f.map,
position : gmap\_m47f45cfd7fbdad89458bd718562c3c8f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m47f45cfd7fbdad89458bd718562c3c8f.map.setCenter( gmap\_m47f45cfd7fbdad89458bd718562c3c8f.positions[555] );
});