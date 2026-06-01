---
title: WordCamp Minnesota
date: '2010-11-12T07:57:49+00:00'
format: image
service: flickr
tags:
- minnesota
- wcmsp
- wordcamp
- wordcampmsp
- wordpress
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5183208609_6f7f13fa5e_o.jpg?resize=607%2C452
---

[![WordCamp Minnesota](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5183208609_6f7f13fa5e_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/11/12/wordcamp-minnesota-5/) 
# [WordCamp Minnesota](http://dentedreality.com.au/2010/11/12/wordcamp-minnesota-5/)





* #[minnesota](http://dentedreality.com.au/tags/minnesota/)
* #[wcmsp](http://dentedreality.com.au/tags/wcmsp/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)
* #[wordcampmsp](http://dentedreality.com.au/tags/wordcampmsp/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183208609/) [7:57 am, November 12, 2010](http://dentedreality.com.au/2010/11/12/wordcamp-minnesota-5/ "7:57 am") 
jQuery(document).ready(function(){
var gmap\_mda8e70e4c42a616d0cd4b8e262a6326f = {
positions : {
178 : new google.maps.LatLng( '44.979833', '-93.257834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mda8e70e4c42a616d0cd4b8e262a6326f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mda8e70e4c42a616d0cd4b8e262a6326f.positions ) {
gmap\_mda8e70e4c42a616d0cd4b8e262a6326f.bounds.extend( gmap\_mda8e70e4c42a616d0cd4b8e262a6326f.positions[m] );
}
// Render markers
for ( var m in gmap\_mda8e70e4c42a616d0cd4b8e262a6326f.positions ) {
gmap\_mda8e70e4c42a616d0cd4b8e262a6326f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mda8e70e4c42a616d0cd4b8e262a6326f.map,
position : gmap\_mda8e70e4c42a616d0cd4b8e262a6326f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mda8e70e4c42a616d0cd4b8e262a6326f.map.setCenter( gmap\_mda8e70e4c42a616d0cd4b8e262a6326f.positions[178] );
});