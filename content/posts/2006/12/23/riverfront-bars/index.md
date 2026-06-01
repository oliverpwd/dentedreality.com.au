---
title: Riverfront Bars
date: '2006-12-23T17:42:45+00:00'
format: image
service: flickr
tags:
- bar
- river
- riverfront
- singapore
- thailand06
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348116622_9121053be4_o.jpg?resize=607%2C455
---

[![Riverfront Bars](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348116622_9121053be4_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/23/riverfront-bars/) 
# [Riverfront Bars](http://dentedreality.com.au/2006/12/23/riverfront-bars/)





* #[bar](http://dentedreality.com.au/tags/bar/)
* #[river](http://dentedreality.com.au/tags/river/)
* #[riverfront](http://dentedreality.com.au/tags/riverfront/)
* #[singapore](http://dentedreality.com.au/tags/singapore/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348116622/) [5:42 pm, December 23, 2006](http://dentedreality.com.au/2006/12/23/riverfront-bars/ "5:42 pm") 
jQuery(document).ready(function(){
var gmap\_mad4bfd4e1554f2fe6aba3e0304cd4190 = {
positions : {
429 : new google.maps.LatLng( '1.300394', '103.873157' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mad4bfd4e1554f2fe6aba3e0304cd4190' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mad4bfd4e1554f2fe6aba3e0304cd4190.positions ) {
gmap\_mad4bfd4e1554f2fe6aba3e0304cd4190.bounds.extend( gmap\_mad4bfd4e1554f2fe6aba3e0304cd4190.positions[m] );
}
// Render markers
for ( var m in gmap\_mad4bfd4e1554f2fe6aba3e0304cd4190.positions ) {
gmap\_mad4bfd4e1554f2fe6aba3e0304cd4190.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mad4bfd4e1554f2fe6aba3e0304cd4190.map,
position : gmap\_mad4bfd4e1554f2fe6aba3e0304cd4190.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mad4bfd4e1554f2fe6aba3e0304cd4190.map.setCenter( gmap\_mad4bfd4e1554f2fe6aba3e0304cd4190.positions[429] );
});