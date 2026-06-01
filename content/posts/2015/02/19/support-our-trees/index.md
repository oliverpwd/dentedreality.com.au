---
title: ''
date: '2015-02-19T13:21:03+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/11008011_852513041458197_1702414219_n.jpg?resize=640%2C640
---

[![Support Our Trees!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/11008011_852513041458197_1702414219_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/02/19/support-our-trees/) 

Support Our Trees!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/zS8Q8nimIA/) [1:21 pm, February 19, 2015](http://dentedreality.com.au/2015/02/19/support-our-trees/ "1:21 pm") 
jQuery(document).ready(function(){
var gmap\_med90ab6cd6e220fa30bcec66d9821462 = {
positions : {
258 : new google.maps.LatLng( '39.736588333', '-104.979905' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_med90ab6cd6e220fa30bcec66d9821462' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_med90ab6cd6e220fa30bcec66d9821462.positions ) {
gmap\_med90ab6cd6e220fa30bcec66d9821462.bounds.extend( gmap\_med90ab6cd6e220fa30bcec66d9821462.positions[m] );
}
// Render markers
for ( var m in gmap\_med90ab6cd6e220fa30bcec66d9821462.positions ) {
gmap\_med90ab6cd6e220fa30bcec66d9821462.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_med90ab6cd6e220fa30bcec66d9821462.map,
position : gmap\_med90ab6cd6e220fa30bcec66d9821462.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_med90ab6cd6e220fa30bcec66d9821462.map.setCenter( gmap\_med90ab6cd6e220fa30bcec66d9821462.positions[258] );
});