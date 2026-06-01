---
title: Singapore Buildings
date: '2006-12-23T17:28:17+00:00'
format: image
service: flickr
tags:
- buildings
- singapore
- skyline
- thailand06
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348118488_54d145db8e_o.jpg?resize=607%2C455
---

[![Singapore Buildings](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348118488_54d145db8e_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/23/singapore-buildings/) 
# [Singapore Buildings](http://dentedreality.com.au/2006/12/23/singapore-buildings/)





* #[buildings](http://dentedreality.com.au/tags/buildings/)
* #[singapore](http://dentedreality.com.au/tags/singapore/)
* #[skyline](http://dentedreality.com.au/tags/skyline/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348118488/) [5:28 pm, December 23, 2006](http://dentedreality.com.au/2006/12/23/singapore-buildings/ "5:28 pm") 
jQuery(document).ready(function(){
var gmap\_md3674a8e1e43490f75179805c2f0ad53 = {
positions : {
770 : new google.maps.LatLng( '1.300394', '103.873157' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md3674a8e1e43490f75179805c2f0ad53' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md3674a8e1e43490f75179805c2f0ad53.positions ) {
gmap\_md3674a8e1e43490f75179805c2f0ad53.bounds.extend( gmap\_md3674a8e1e43490f75179805c2f0ad53.positions[m] );
}
// Render markers
for ( var m in gmap\_md3674a8e1e43490f75179805c2f0ad53.positions ) {
gmap\_md3674a8e1e43490f75179805c2f0ad53.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md3674a8e1e43490f75179805c2f0ad53.map,
position : gmap\_md3674a8e1e43490f75179805c2f0ad53.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md3674a8e1e43490f75179805c2f0ad53.map.setCenter( gmap\_md3674a8e1e43490f75179805c2f0ad53.positions[770] );
});