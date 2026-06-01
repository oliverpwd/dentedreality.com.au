---
title: ''
date: '2012-09-11T17:51:36+00:00'
format: image
service: instagram
tags:
- automattic
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/dc247ebefc5a11e18a5622000a1cf717_7.jpg?resize=607%2C607
---

[![Advanced JavaScript session for #Automattic-ians with the unstoppable @koop](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/dc247ebefc5a11e18a5622000a1cf717_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/09/11/advanced-javascript-session-for-automattic-ians-with-the-unstoppable-koop/) 

Advanced JavaScript session for #Automattic-ians with the unstoppable @koop





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/Pc2WjgimI6/) [5:51 pm, September 11, 2012](http://dentedreality.com.au/2012/09/11/advanced-javascript-session-for-automattic-ians-with-the-unstoppable-koop/ "5:51 pm") 
jQuery(document).ready(function(){
var gmap\_m3dc47fa24b6b9f17d47801c6c1e98099 = {
positions : {
804 : new google.maps.LatLng( '32.790149071', '-117.252331748' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3dc47fa24b6b9f17d47801c6c1e98099' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3dc47fa24b6b9f17d47801c6c1e98099.positions ) {
gmap\_m3dc47fa24b6b9f17d47801c6c1e98099.bounds.extend( gmap\_m3dc47fa24b6b9f17d47801c6c1e98099.positions[m] );
}
// Render markers
for ( var m in gmap\_m3dc47fa24b6b9f17d47801c6c1e98099.positions ) {
gmap\_m3dc47fa24b6b9f17d47801c6c1e98099.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3dc47fa24b6b9f17d47801c6c1e98099.map,
position : gmap\_m3dc47fa24b6b9f17d47801c6c1e98099.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3dc47fa24b6b9f17d47801c6c1e98099.map.setCenter( gmap\_m3dc47fa24b6b9f17d47801c6c1e98099.positions[804] );
});