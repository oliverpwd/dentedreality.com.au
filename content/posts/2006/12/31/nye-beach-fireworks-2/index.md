---
title: NYE Beach Fireworks
date: '2006-12-31T06:51:44+00:00'
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
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349551999_0be661807c_o.jpg?resize=607%2C455
---

[![NYE Beach Fireworks](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349551999_0be661807c_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-2/) 
# [NYE Beach Fireworks](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-2/)





* #[fireworks](http://dentedreality.com.au/tags/fireworks/)
* #[newyearseve2006](http://dentedreality.com.au/tags/newyearseve2006/)
* #[nye2006](http://dentedreality.com.au/tags/nye2006/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[pyrotechnics](http://dentedreality.com.au/tags/pyrotechnics/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349551999/) [6:51 am, December 31, 2006](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-2/ "6:51 am") 
jQuery(document).ready(function(){
var gmap\_m674a0ade4cd8e0f9b39da42b3f08918f = {
positions : {
475 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m674a0ade4cd8e0f9b39da42b3f08918f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m674a0ade4cd8e0f9b39da42b3f08918f.positions ) {
gmap\_m674a0ade4cd8e0f9b39da42b3f08918f.bounds.extend( gmap\_m674a0ade4cd8e0f9b39da42b3f08918f.positions[m] );
}
// Render markers
for ( var m in gmap\_m674a0ade4cd8e0f9b39da42b3f08918f.positions ) {
gmap\_m674a0ade4cd8e0f9b39da42b3f08918f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m674a0ade4cd8e0f9b39da42b3f08918f.map,
position : gmap\_m674a0ade4cd8e0f9b39da42b3f08918f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m674a0ade4cd8e0f9b39da42b3f08918f.map.setCenter( gmap\_m674a0ade4cd8e0f9b39da42b3f08918f.positions[475] );
});