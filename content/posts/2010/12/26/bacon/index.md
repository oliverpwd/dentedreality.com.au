---
title: BACON!
date: '2010-12-26T04:55:31+00:00'
format: image
service: flickr
tags:
- bacon
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434709104_eff29c884f_o.jpg?resize=607%2C452
---

[![BACON!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434709104_eff29c884f_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/12/26/bacon/) 
# [BACON!](http://dentedreality.com.au/2010/12/26/bacon/)





* #[bacon](http://dentedreality.com.au/tags/bacon/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434709104/) [4:55 am, December 26, 2010](http://dentedreality.com.au/2010/12/26/bacon/ "4:55 am") 
jQuery(document).ready(function(){
var gmap\_mf3ec80a858d44725dc18e76612e28dad = {
positions : {
612 : new google.maps.LatLng( '-32.053', '115.846499' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf3ec80a858d44725dc18e76612e28dad' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf3ec80a858d44725dc18e76612e28dad.positions ) {
gmap\_mf3ec80a858d44725dc18e76612e28dad.bounds.extend( gmap\_mf3ec80a858d44725dc18e76612e28dad.positions[m] );
}
// Render markers
for ( var m in gmap\_mf3ec80a858d44725dc18e76612e28dad.positions ) {
gmap\_mf3ec80a858d44725dc18e76612e28dad.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf3ec80a858d44725dc18e76612e28dad.map,
position : gmap\_mf3ec80a858d44725dc18e76612e28dad.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf3ec80a858d44725dc18e76612e28dad.map.setCenter( gmap\_mf3ec80a858d44725dc18e76612e28dad.positions[612] );
});