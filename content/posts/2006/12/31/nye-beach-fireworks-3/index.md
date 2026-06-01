---
title: NYE Beach Fireworks
date: '2006-12-31T06:59:28+00:00'
format: image
service: flickr
tags:
- fireworks
- newyearseve2006
- nye2006
- phuket
- pyrotechnics
- thailand
- thailand06
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349551474_83fdda3acd_o.jpg?resize=607%2C455
---

[![NYE Beach Fireworks](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349551474_83fdda3acd_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-3/) 
# [NYE Beach Fireworks](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-3/)





* #[fireworks](http://dentedreality.com.au/tags/fireworks/)
* #[newyearseve2006](http://dentedreality.com.au/tags/newyearseve2006/)
* #[nye2006](http://dentedreality.com.au/tags/nye2006/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[pyrotechnics](http://dentedreality.com.au/tags/pyrotechnics/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349551474/) [6:59 am, December 31, 2006](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-3/ "6:59 am") 
jQuery(document).ready(function(){
var gmap\_me0447ee078ade11958a788c808b07715 = {
positions : {
402 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me0447ee078ade11958a788c808b07715' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me0447ee078ade11958a788c808b07715.positions ) {
gmap\_me0447ee078ade11958a788c808b07715.bounds.extend( gmap\_me0447ee078ade11958a788c808b07715.positions[m] );
}
// Render markers
for ( var m in gmap\_me0447ee078ade11958a788c808b07715.positions ) {
gmap\_me0447ee078ade11958a788c808b07715.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me0447ee078ade11958a788c808b07715.map,
position : gmap\_me0447ee078ade11958a788c808b07715.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me0447ee078ade11958a788c808b07715.map.setCenter( gmap\_me0447ee078ade11958a788c808b07715.positions[402] );
});