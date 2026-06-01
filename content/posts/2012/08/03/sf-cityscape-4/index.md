---
title: SF Cityscape
date: '2012-08-03T19:26:22+00:00'
format: image
service: flickr
tags:
- cityscape
- sanfrancisco
- sf
- skyline
- view
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8245787196_a3237c2d64_o.jpg?resize=607%2C813
---

[![SF Cityscape](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8245787196_a3237c2d64_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/08/03/sf-cityscape-4/) 
# [SF Cityscape](http://dentedreality.com.au/2012/08/03/sf-cityscape-4/)





* #[cityscape](http://dentedreality.com.au/tags/cityscape/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[sf](http://dentedreality.com.au/tags/sf/)
* #[skyline](http://dentedreality.com.au/tags/skyline/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245787196/) [7:26 pm, August 3, 2012](http://dentedreality.com.au/2012/08/03/sf-cityscape-4/ "7:26 pm") 
jQuery(document).ready(function(){
var gmap\_m5dab9c7f0b8d534f38e6cbd98f6d1375 = {
positions : {
391 : new google.maps.LatLng( '37.7555', '-122.418334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5dab9c7f0b8d534f38e6cbd98f6d1375' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5dab9c7f0b8d534f38e6cbd98f6d1375.positions ) {
gmap\_m5dab9c7f0b8d534f38e6cbd98f6d1375.bounds.extend( gmap\_m5dab9c7f0b8d534f38e6cbd98f6d1375.positions[m] );
}
// Render markers
for ( var m in gmap\_m5dab9c7f0b8d534f38e6cbd98f6d1375.positions ) {
gmap\_m5dab9c7f0b8d534f38e6cbd98f6d1375.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5dab9c7f0b8d534f38e6cbd98f6d1375.map,
position : gmap\_m5dab9c7f0b8d534f38e6cbd98f6d1375.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5dab9c7f0b8d534f38e6cbd98f6d1375.map.setCenter( gmap\_m5dab9c7f0b8d534f38e6cbd98f6d1375.positions[391] );
});