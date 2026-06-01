---
title: Royal Hakea
date: '2008-04-07T16:14:22+00:00'
format: image
service: flickr
tags:
- australia
- fitzgeraldrivernationalpark
- hakea
- royalhakea
- westernaustraliabremerbay
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433449846_152b0b5d4a_o.jpg?resize=607%2C808
---

[![Royal Hakea](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433449846_152b0b5d4a_o.jpg?resize=607%2C808)](http://dentedreality.com.au/2008/04/07/royal-hakea/) 
# [Royal Hakea](http://dentedreality.com.au/2008/04/07/royal-hakea/)

Bizarre plant only found in the Fitzgerald River National Park, next door to Bremer Bay





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[fitzgeraldrivernationalpark](http://dentedreality.com.au/tags/fitzgeraldrivernationalpark/)
* #[hakea](http://dentedreality.com.au/tags/hakea/)
* #[royalhakea](http://dentedreality.com.au/tags/royalhakea/)
* #[westernaustraliabremerbay](http://dentedreality.com.au/tags/westernaustraliabremerbay/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2433449846/) [4:14 pm, April 7, 2008](http://dentedreality.com.au/2008/04/07/royal-hakea/ "4:14 pm") 
jQuery(document).ready(function(){
var gmap\_m6409120e71e12bab7575a7373489538b = {
positions : {
690 : new google.maps.LatLng( '-34.36859', '119.322681' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6409120e71e12bab7575a7373489538b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6409120e71e12bab7575a7373489538b.positions ) {
gmap\_m6409120e71e12bab7575a7373489538b.bounds.extend( gmap\_m6409120e71e12bab7575a7373489538b.positions[m] );
}
// Render markers
for ( var m in gmap\_m6409120e71e12bab7575a7373489538b.positions ) {
gmap\_m6409120e71e12bab7575a7373489538b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6409120e71e12bab7575a7373489538b.map,
position : gmap\_m6409120e71e12bab7575a7373489538b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6409120e71e12bab7575a7373489538b.map.setCenter( gmap\_m6409120e71e12bab7575a7373489538b.positions[690] );
});