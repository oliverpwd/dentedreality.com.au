---
title: Champagne Brunch
date: '2011-01-23T05:01:58+00:00'
format: image
service: flickr
tags:
- australia
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434805314_47055a1314_o.jpg?resize=607%2C452
---

[![Champagne Brunch](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434805314_47055a1314_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/23/champagne-brunch/) 
# [Champagne Brunch](http://dentedreality.com.au/2011/01/23/champagne-brunch/)





* #[australia](http://dentedreality.com.au/tags/australia/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434805314/) [5:01 am, January 23, 2011](http://dentedreality.com.au/2011/01/23/champagne-brunch/ "5:01 am") 
jQuery(document).ready(function(){
var gmap\_mc270d792f467e26682bc557c8aba4b4d = {
positions : {
989 : new google.maps.LatLng( '-32.053167', '115.846333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc270d792f467e26682bc557c8aba4b4d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc270d792f467e26682bc557c8aba4b4d.positions ) {
gmap\_mc270d792f467e26682bc557c8aba4b4d.bounds.extend( gmap\_mc270d792f467e26682bc557c8aba4b4d.positions[m] );
}
// Render markers
for ( var m in gmap\_mc270d792f467e26682bc557c8aba4b4d.positions ) {
gmap\_mc270d792f467e26682bc557c8aba4b4d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc270d792f467e26682bc557c8aba4b4d.map,
position : gmap\_mc270d792f467e26682bc557c8aba4b4d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc270d792f467e26682bc557c8aba4b4d.map.setCenter( gmap\_mc270d792f467e26682bc557c8aba4b4d.positions[989] );
});