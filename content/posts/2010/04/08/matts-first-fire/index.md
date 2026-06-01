---
title: Matt’s First Fire
date: '2010-04-08T15:03:00+00:00'
format: image
service: flickr
tags:
- matt
- photomatt
- tombrown
- trackerschool
- tracking
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4515821953_1be2035f32_o.jpg?resize=607%2C455
---

[![Matt's First Fire](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4515821953_1be2035f32_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/08/matts-first-fire/) 
# [Matt’s First Fire](http://dentedreality.com.au/2010/04/08/matts-first-fire/)

Standard class, Tracker School.





* #[matt](http://dentedreality.com.au/tags/matt/)
* #[photomatt](http://dentedreality.com.au/tags/photomatt/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4515821953/) [3:03 pm, April 8, 2010](http://dentedreality.com.au/2010/04/08/matts-first-fire/ "3:03 pm") 
jQuery(document).ready(function(){
var gmap\_mbeac743ca3458b2725447bd996ecf8a9 = {
positions : {
81 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbeac743ca3458b2725447bd996ecf8a9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbeac743ca3458b2725447bd996ecf8a9.positions ) {
gmap\_mbeac743ca3458b2725447bd996ecf8a9.bounds.extend( gmap\_mbeac743ca3458b2725447bd996ecf8a9.positions[m] );
}
// Render markers
for ( var m in gmap\_mbeac743ca3458b2725447bd996ecf8a9.positions ) {
gmap\_mbeac743ca3458b2725447bd996ecf8a9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbeac743ca3458b2725447bd996ecf8a9.map,
position : gmap\_mbeac743ca3458b2725447bd996ecf8a9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbeac743ca3458b2725447bd996ecf8a9.map.setCenter( gmap\_mbeac743ca3458b2725447bd996ecf8a9.positions[81] );
});