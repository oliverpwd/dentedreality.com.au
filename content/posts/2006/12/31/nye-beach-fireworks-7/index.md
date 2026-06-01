---
title: NYE Beach Fireworks
date: '2006-12-31T07:08:10+00:00'
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
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349548747_dbb2982bce_o.jpg?resize=607%2C809
---

[![NYE Beach Fireworks](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349548747_dbb2982bce_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-7/) 
# [NYE Beach Fireworks](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-7/)





* #[fireworks](http://dentedreality.com.au/tags/fireworks/)
* #[newyearseve2006](http://dentedreality.com.au/tags/newyearseve2006/)
* #[nye2006](http://dentedreality.com.au/tags/nye2006/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[pyrotechnics](http://dentedreality.com.au/tags/pyrotechnics/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349548747/) [7:08 am, December 31, 2006](http://dentedreality.com.au/2006/12/31/nye-beach-fireworks-7/ "7:08 am") 
jQuery(document).ready(function(){
var gmap\_m7e8ac62a240892815564250de8804683 = {
positions : {
631 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7e8ac62a240892815564250de8804683' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7e8ac62a240892815564250de8804683.positions ) {
gmap\_m7e8ac62a240892815564250de8804683.bounds.extend( gmap\_m7e8ac62a240892815564250de8804683.positions[m] );
}
// Render markers
for ( var m in gmap\_m7e8ac62a240892815564250de8804683.positions ) {
gmap\_m7e8ac62a240892815564250de8804683.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7e8ac62a240892815564250de8804683.map,
position : gmap\_m7e8ac62a240892815564250de8804683.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7e8ac62a240892815564250de8804683.map.setCenter( gmap\_m7e8ac62a240892815564250de8804683.positions[631] );
});