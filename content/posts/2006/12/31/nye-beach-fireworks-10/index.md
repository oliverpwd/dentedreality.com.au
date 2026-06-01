---
title: NYE Beach Fireworks
date: '2006-12-31T07:08:52+00:00'
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
- wallpaper
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349546941_223d632a9d_o.jpg?resize=607%2C455
---

[![NYE Beach Fireworks](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349546941_223d632a9d_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-10/) 
# [NYE Beach Fireworks](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-10/)





* #[fireworks](http://dentedreality.com.au/tags/fireworks/)
* #[newyearseve2006](http://dentedreality.com.au/tags/newyearseve2006/)
* #[nye2006](http://dentedreality.com.au/tags/nye2006/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[pyrotechnics](http://dentedreality.com.au/tags/pyrotechnics/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)
* #[wallpaper](http://dentedreality.com.au/tags/wallpaper/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349546941/) [7:08 am, December 31, 2006](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-10/ "7:08 am") 
jQuery(document).ready(function(){
var gmap\_mac7877e402cbef4c4f26411e700a6422 = {
positions : {
319 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mac7877e402cbef4c4f26411e700a6422' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mac7877e402cbef4c4f26411e700a6422.positions ) {
gmap\_mac7877e402cbef4c4f26411e700a6422.bounds.extend( gmap\_mac7877e402cbef4c4f26411e700a6422.positions[m] );
}
// Render markers
for ( var m in gmap\_mac7877e402cbef4c4f26411e700a6422.positions ) {
gmap\_mac7877e402cbef4c4f26411e700a6422.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mac7877e402cbef4c4f26411e700a6422.map,
position : gmap\_mac7877e402cbef4c4f26411e700a6422.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mac7877e402cbef4c4f26411e700a6422.map.setCenter( gmap\_mac7877e402cbef4c4f26411e700a6422.positions[319] );
});