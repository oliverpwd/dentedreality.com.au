---
title: Bread
date: '2011-10-30T07:51:56+00:00'
format: image
service: flickr
tags:
- bread
- norway
- Oslo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6958278849_9c729aeb08_o.jpg?resize=607%2C452
---

[![Bread](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6958278849_9c729aeb08_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/10/30/bread-2/) 
# [Bread](http://dentedreality.com.au/2011/10/30/bread-2/)





* #[bread](http://dentedreality.com.au/tags/bread/)
* #[norway](http://dentedreality.com.au/tags/norway/)
* #[Oslo](http://dentedreality.com.au/tags/oslo/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958278849/) [7:51 am, October 30, 2011](http://dentedreality.com.au/2011/10/30/bread-2/ "7:51 am") 
jQuery(document).ready(function(){
var gmap\_m2826593a3f98111e4018420c3c219f2b = {
positions : {
571 : new google.maps.LatLng( '59.913833', '10.735999' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2826593a3f98111e4018420c3c219f2b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2826593a3f98111e4018420c3c219f2b.positions ) {
gmap\_m2826593a3f98111e4018420c3c219f2b.bounds.extend( gmap\_m2826593a3f98111e4018420c3c219f2b.positions[m] );
}
// Render markers
for ( var m in gmap\_m2826593a3f98111e4018420c3c219f2b.positions ) {
gmap\_m2826593a3f98111e4018420c3c219f2b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2826593a3f98111e4018420c3c219f2b.map,
position : gmap\_m2826593a3f98111e4018420c3c219f2b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2826593a3f98111e4018420c3c219f2b.map.setCenter( gmap\_m2826593a3f98111e4018420c3c219f2b.positions[571] );
});