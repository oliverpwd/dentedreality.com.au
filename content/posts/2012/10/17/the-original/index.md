---
title: The Original
date: '2012-10-17T08:44:18+00:00'
format: image
service: flickr
tags:
- door
- police
- precinct
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8245863840_e9d7f09617_o.jpg?resize=607%2C813
---

[![The Original](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8245863840_e9d7f09617_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/10/17/the-original/) 
# [The Original](http://dentedreality.com.au/2012/10/17/the-original/)





* #[door](http://dentedreality.com.au/tags/door/)
* #[police](http://dentedreality.com.au/tags/police/)
* #[precinct](http://dentedreality.com.au/tags/precinct/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245863840/) [8:44 am, October 17, 2012](http://dentedreality.com.au/2012/10/17/the-original/ "8:44 am") 
jQuery(document).ready(function(){
var gmap\_me0fee71ce5941b5257829f0e79571f7b = {
positions : {
546 : new google.maps.LatLng( '40.720166', '-74.006834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me0fee71ce5941b5257829f0e79571f7b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me0fee71ce5941b5257829f0e79571f7b.positions ) {
gmap\_me0fee71ce5941b5257829f0e79571f7b.bounds.extend( gmap\_me0fee71ce5941b5257829f0e79571f7b.positions[m] );
}
// Render markers
for ( var m in gmap\_me0fee71ce5941b5257829f0e79571f7b.positions ) {
gmap\_me0fee71ce5941b5257829f0e79571f7b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me0fee71ce5941b5257829f0e79571f7b.map,
position : gmap\_me0fee71ce5941b5257829f0e79571f7b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me0fee71ce5941b5257829f0e79571f7b.map.setCenter( gmap\_me0fee71ce5941b5257829f0e79571f7b.positions[546] );
});