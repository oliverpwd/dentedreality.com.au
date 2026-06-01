---
title: Ryan & Rani
date: '2011-05-29T17:50:52+00:00'
format: image
service: flickr
tags:
- owenswedding
- wedding
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802876837_f8c1fb24e3_o.jpg?resize=607%2C452
---

[![Ryan & Rani](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802876837_f8c1fb24e3_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/29/ryan-rani/) 
# [Ryan & Rani](http://dentedreality.com.au/2011/05/29/ryan-rani/)





* #[owenswedding](http://dentedreality.com.au/tags/owenswedding/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802876837/) [5:50 pm, May 29, 2011](http://dentedreality.com.au/2011/05/29/ryan-rani/ "5:50 pm") 
jQuery(document).ready(function(){
var gmap\_md128ee2220cead21494678673f139eab = {
positions : {
759 : new google.maps.LatLng( '37.792666', '-122.421167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md128ee2220cead21494678673f139eab' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md128ee2220cead21494678673f139eab.positions ) {
gmap\_md128ee2220cead21494678673f139eab.bounds.extend( gmap\_md128ee2220cead21494678673f139eab.positions[m] );
}
// Render markers
for ( var m in gmap\_md128ee2220cead21494678673f139eab.positions ) {
gmap\_md128ee2220cead21494678673f139eab.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md128ee2220cead21494678673f139eab.map,
position : gmap\_md128ee2220cead21494678673f139eab.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md128ee2220cead21494678673f139eab.map.setCenter( gmap\_md128ee2220cead21494678673f139eab.positions[759] );
});