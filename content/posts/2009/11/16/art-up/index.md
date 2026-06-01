---
title: Art, Up
date: '2009-11-16T09:14:51+00:00'
format: image
service: flickr
tags:
- newyork
- newyork09
- wcnyc
- wordcamp
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2009/11/4123966996_d11e2dfc22_o.jpg?resize=607%2C809
---

[![Art, Up](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2009/11/4123966996_d11e2dfc22_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2009/11/16/art-up/) 
# [Art, Up](http://dentedreality.com.au/2009/11/16/art-up/)





* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[newyork09](http://dentedreality.com.au/tags/newyork09/)
* #[wcnyc](http://dentedreality.com.au/tags/wcnyc/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4123966996/) [9:14 am, November 16, 2009](http://dentedreality.com.au/2009/11/16/art-up/ "9:14 am") 
jQuery(document).ready(function(){
var gmap\_md46a6c1fef6747dd978da71568abbebc = {
positions : {
12 : new google.maps.LatLng( '40.757166', '-73.989' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md46a6c1fef6747dd978da71568abbebc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md46a6c1fef6747dd978da71568abbebc.positions ) {
gmap\_md46a6c1fef6747dd978da71568abbebc.bounds.extend( gmap\_md46a6c1fef6747dd978da71568abbebc.positions[m] );
}
// Render markers
for ( var m in gmap\_md46a6c1fef6747dd978da71568abbebc.positions ) {
gmap\_md46a6c1fef6747dd978da71568abbebc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md46a6c1fef6747dd978da71568abbebc.map,
position : gmap\_md46a6c1fef6747dd978da71568abbebc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md46a6c1fef6747dd978da71568abbebc.map.setCenter( gmap\_md46a6c1fef6747dd978da71568abbebc.positions[12] );
});