---
title: Oslo
date: '2011-10-28T06:54:06+00:00'
format: image
service: flickr
tags:
- norway
- Oslo
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812165906_ca6781f639_o.jpg?resize=607%2C452
---

[![Oslo](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812165906_ca6781f639_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/10/28/oslo-11/) 
# [Oslo](http://dentedreality.com.au/2011/10/28/oslo-11/)





* #[norway](http://dentedreality.com.au/tags/norway/)
* #[Oslo](http://dentedreality.com.au/tags/oslo/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812165906/) [6:54 am, October 28, 2011](http://dentedreality.com.au/2011/10/28/oslo-11/ "6:54 am") 
jQuery(document).ready(function(){
var gmap\_m018929cc10f3726cfc4dee8590320c16 = {
positions : {
382 : new google.maps.LatLng( '59.919999', '10.724166' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m018929cc10f3726cfc4dee8590320c16' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m018929cc10f3726cfc4dee8590320c16.positions ) {
gmap\_m018929cc10f3726cfc4dee8590320c16.bounds.extend( gmap\_m018929cc10f3726cfc4dee8590320c16.positions[m] );
}
// Render markers
for ( var m in gmap\_m018929cc10f3726cfc4dee8590320c16.positions ) {
gmap\_m018929cc10f3726cfc4dee8590320c16.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m018929cc10f3726cfc4dee8590320c16.map,
position : gmap\_m018929cc10f3726cfc4dee8590320c16.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m018929cc10f3726cfc4dee8590320c16.map.setCenter( gmap\_m018929cc10f3726cfc4dee8590320c16.positions[382] );
});