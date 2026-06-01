---
title: NERT Citywide Drill, 2011
date: '2011-04-16T08:01:07+00:00'
format: image
service: flickr
tags:
- nert
- sanfrancisco
- sffd
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802145757_67655d6339_o.jpg?resize=607%2C452
---

[![NERT Citywide Drill, 2011](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802145757_67655d6339_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/04/16/nert-citywide-drill-2011-3/) 
# [NERT Citywide Drill, 2011](http://dentedreality.com.au/2011/04/16/nert-citywide-drill-2011-3/)





* #[nert](http://dentedreality.com.au/tags/nert/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[sffd](http://dentedreality.com.au/tags/sffd/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802145757/) [8:01 am, April 16, 2011](http://dentedreality.com.au/2011/04/16/nert-citywide-drill-2011-3/ "8:01 am") 
jQuery(document).ready(function(){
var gmap\_mdd09a23fed5ca9748d2a0aad758c3cfa = {
positions : {
456 : new google.maps.LatLng( '37.759333', '-122.413334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdd09a23fed5ca9748d2a0aad758c3cfa' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdd09a23fed5ca9748d2a0aad758c3cfa.positions ) {
gmap\_mdd09a23fed5ca9748d2a0aad758c3cfa.bounds.extend( gmap\_mdd09a23fed5ca9748d2a0aad758c3cfa.positions[m] );
}
// Render markers
for ( var m in gmap\_mdd09a23fed5ca9748d2a0aad758c3cfa.positions ) {
gmap\_mdd09a23fed5ca9748d2a0aad758c3cfa.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdd09a23fed5ca9748d2a0aad758c3cfa.map,
position : gmap\_mdd09a23fed5ca9748d2a0aad758c3cfa.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdd09a23fed5ca9748d2a0aad758c3cfa.map.setCenter( gmap\_mdd09a23fed5ca9748d2a0aad758c3cfa.positions[456] );
});