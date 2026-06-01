---
title: NYE Beach Fireworks
date: '2006-12-31T07:08:30+00:00'
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
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349548035_c5a33e8a03_o.jpg?resize=607%2C809
---

[![NYE Beach Fireworks](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349548035_c5a33e8a03_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-8/) 
# [NYE Beach Fireworks](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-8/)





* #[fireworks](http://dentedreality.com.au/tags/fireworks/)
* #[newyearseve2006](http://dentedreality.com.au/tags/newyearseve2006/)
* #[nye2006](http://dentedreality.com.au/tags/nye2006/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[pyrotechnics](http://dentedreality.com.au/tags/pyrotechnics/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349548035/) [7:08 am, December 31, 2006](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-8/ "7:08 am") 
jQuery(document).ready(function(){
var gmap\_m5e0b6cf62bffd510ca0d764f3abcb48e = {
positions : {
548 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5e0b6cf62bffd510ca0d764f3abcb48e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5e0b6cf62bffd510ca0d764f3abcb48e.positions ) {
gmap\_m5e0b6cf62bffd510ca0d764f3abcb48e.bounds.extend( gmap\_m5e0b6cf62bffd510ca0d764f3abcb48e.positions[m] );
}
// Render markers
for ( var m in gmap\_m5e0b6cf62bffd510ca0d764f3abcb48e.positions ) {
gmap\_m5e0b6cf62bffd510ca0d764f3abcb48e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5e0b6cf62bffd510ca0d764f3abcb48e.map,
position : gmap\_m5e0b6cf62bffd510ca0d764f3abcb48e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5e0b6cf62bffd510ca0d764f3abcb48e.map.setCenter( gmap\_m5e0b6cf62bffd510ca0d764f3abcb48e.positions[548] );
});