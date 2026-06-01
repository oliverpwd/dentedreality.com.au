---
title: NERT Citywide Drill, 2011
date: '2011-04-16T05:21:49+00:00'
format: image
service: flickr
tags:
- nert
- sanfrancisco
- sffd
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802145095_a2ffef63e7_o.jpg?resize=607%2C452
---

[![NERT Citywide Drill, 2011](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802145095_a2ffef63e7_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/04/16/nert-citywide-drill-2011-5/) 
# [NERT Citywide Drill, 2011](http://dentedreality.com.au/2011/04/16/nert-citywide-drill-2011-5/)





* #[nert](http://dentedreality.com.au/tags/nert/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[sffd](http://dentedreality.com.au/tags/sffd/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802145095/) [5:21 am, April 16, 2011](http://dentedreality.com.au/2011/04/16/nert-citywide-drill-2011-5/ "5:21 am") 
jQuery(document).ready(function(){
var gmap\_ma0ee3787cb3525a53c402b05e7a5cc22 = {
positions : {
132 : new google.maps.LatLng( '37.759333', '-122.413334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma0ee3787cb3525a53c402b05e7a5cc22' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma0ee3787cb3525a53c402b05e7a5cc22.positions ) {
gmap\_ma0ee3787cb3525a53c402b05e7a5cc22.bounds.extend( gmap\_ma0ee3787cb3525a53c402b05e7a5cc22.positions[m] );
}
// Render markers
for ( var m in gmap\_ma0ee3787cb3525a53c402b05e7a5cc22.positions ) {
gmap\_ma0ee3787cb3525a53c402b05e7a5cc22.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma0ee3787cb3525a53c402b05e7a5cc22.map,
position : gmap\_ma0ee3787cb3525a53c402b05e7a5cc22.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma0ee3787cb3525a53c402b05e7a5cc22.map.setCenter( gmap\_ma0ee3787cb3525a53c402b05e7a5cc22.positions[132] );
});