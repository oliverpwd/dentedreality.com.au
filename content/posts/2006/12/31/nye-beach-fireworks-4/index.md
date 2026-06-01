---
title: NYE Beach Fireworks
date: '2006-12-31T06:59:48+00:00'
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
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349550983_5fba78f34c_o.jpg?resize=607%2C809
---

[![NYE Beach Fireworks](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349550983_5fba78f34c_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-4/) 
# [NYE Beach Fireworks](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-4/)





* #[fireworks](http://dentedreality.com.au/tags/fireworks/)
* #[newyearseve2006](http://dentedreality.com.au/tags/newyearseve2006/)
* #[nye2006](http://dentedreality.com.au/tags/nye2006/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[pyrotechnics](http://dentedreality.com.au/tags/pyrotechnics/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349550983/) [6:59 am, December 31, 2006](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-4/ "6:59 am") 
jQuery(document).ready(function(){
var gmap\_mef34cc7bca88565ab76855d016b75e0f = {
positions : {
485 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mef34cc7bca88565ab76855d016b75e0f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mef34cc7bca88565ab76855d016b75e0f.positions ) {
gmap\_mef34cc7bca88565ab76855d016b75e0f.bounds.extend( gmap\_mef34cc7bca88565ab76855d016b75e0f.positions[m] );
}
// Render markers
for ( var m in gmap\_mef34cc7bca88565ab76855d016b75e0f.positions ) {
gmap\_mef34cc7bca88565ab76855d016b75e0f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mef34cc7bca88565ab76855d016b75e0f.map,
position : gmap\_mef34cc7bca88565ab76855d016b75e0f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mef34cc7bca88565ab76855d016b75e0f.map.setCenter( gmap\_mef34cc7bca88565ab76855d016b75e0f.positions[485] );
});