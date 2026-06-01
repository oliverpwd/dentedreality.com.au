---
title: ''
date: '2016-04-13T19:34:52+00:00'
format: image
service: instagram
tags:
- noodles
- ramen
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/04/12501873_1720821211493589_491846619_n.jpg?fit=640%2C640
---

[![Raaaaaaaaamen. #ramen #noodles](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/04/12501873_1720821211493589_491846619_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/04/13/raaaaaaaaamen-ramen-noodles/) 

Raaaaaaaaamen. #ramen #noodles





* #[noodles](http://dentedreality.com.au/tags/noodles/)
* #[ramen](http://dentedreality.com.au/tags/ramen/)

Posted on [Instagram](https://www.instagram.com/p/BEKZQDQimFF/) [7:34 pm, April 13, 2016](http://dentedreality.com.au/2016/04/13/raaaaaaaaamen-ramen-noodles/ "7:34 pm") 
jQuery(document).ready(function(){
var gmap\_maf15c512f60f9a933bda2e16161d6414 = {
positions : {
536 : new google.maps.LatLng( '39.721241', '-104.9542999' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maf15c512f60f9a933bda2e16161d6414' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maf15c512f60f9a933bda2e16161d6414.positions ) {
gmap\_maf15c512f60f9a933bda2e16161d6414.bounds.extend( gmap\_maf15c512f60f9a933bda2e16161d6414.positions[m] );
}
// Render markers
for ( var m in gmap\_maf15c512f60f9a933bda2e16161d6414.positions ) {
gmap\_maf15c512f60f9a933bda2e16161d6414.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maf15c512f60f9a933bda2e16161d6414.map,
position : gmap\_maf15c512f60f9a933bda2e16161d6414.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maf15c512f60f9a933bda2e16161d6414.map.setCenter( gmap\_maf15c512f60f9a933bda2e16161d6414.positions[536] );
});