---
title: Paintballing in New Jersey
date: '2013-08-10T11:41:11+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- me
- paintball
- paintballing
- pedro
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767978366_9d1fbd08d7_o.jpg?resize=607%2C809
---

[![Paintballing in New Jersey](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767978366_9d1fbd08d7_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2013/08/10/paintballing-in-new-jersey/) 
# [Paintballing in New Jersey](http://dentedreality.com.au/2013/08/10/paintballing-in-new-jersey/)

Me and Pedro





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[paintball](http://dentedreality.com.au/tags/paintball/)
* #[paintballing](http://dentedreality.com.au/tags/paintballing/)
* #[pedro](http://dentedreality.com.au/tags/pedro/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9767978366/) [11:41 am, August 10, 2013](http://dentedreality.com.au/2013/08/10/paintballing-in-new-jersey/ "11:41 am") 
jQuery(document).ready(function(){
var gmap\_md7ae32b32704786bfdbf850686a5fedd = {
positions : {
940 : new google.maps.LatLng( '41.115166', '-74.383667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md7ae32b32704786bfdbf850686a5fedd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md7ae32b32704786bfdbf850686a5fedd.positions ) {
gmap\_md7ae32b32704786bfdbf850686a5fedd.bounds.extend( gmap\_md7ae32b32704786bfdbf850686a5fedd.positions[m] );
}
// Render markers
for ( var m in gmap\_md7ae32b32704786bfdbf850686a5fedd.positions ) {
gmap\_md7ae32b32704786bfdbf850686a5fedd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md7ae32b32704786bfdbf850686a5fedd.map,
position : gmap\_md7ae32b32704786bfdbf850686a5fedd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md7ae32b32704786bfdbf850686a5fedd.map.setCenter( gmap\_md7ae32b32704786bfdbf850686a5fedd.positions[940] );
});