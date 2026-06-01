---
title: ''
date: '2012-08-05T13:51:37+00:00'
format: image
service: instagram
tags:
- photo
- wcsf
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/345de7b6df2611e1bde812313b08e061_7.jpg?resize=607%2C607
---

[![Setting up for #wcsf Dev Day](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/345de7b6df2611e1bde812313b08e061_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/08/05/setting-up-for-wcsf-dev-day-2/) 

Setting up for #wcsf Dev Day





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[wcsf](http://dentedreality.com.au/tags/wcsf/)

Posted on [Instagram](http://instagram.com/p/N9JefFCmCn/) [1:51 pm, August 5, 2012](http://dentedreality.com.au/2012/08/05/setting-up-for-wcsf-dev-day-2/ "1:51 pm") 
jQuery(document).ready(function(){
var gmap\_mc50171796a61c760c6dd2ae8774350a2 = {
positions : {
235 : new google.maps.LatLng( '37.755230703', '-122.418396935' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc50171796a61c760c6dd2ae8774350a2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc50171796a61c760c6dd2ae8774350a2.positions ) {
gmap\_mc50171796a61c760c6dd2ae8774350a2.bounds.extend( gmap\_mc50171796a61c760c6dd2ae8774350a2.positions[m] );
}
// Render markers
for ( var m in gmap\_mc50171796a61c760c6dd2ae8774350a2.positions ) {
gmap\_mc50171796a61c760c6dd2ae8774350a2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc50171796a61c760c6dd2ae8774350a2.map,
position : gmap\_mc50171796a61c760c6dd2ae8774350a2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc50171796a61c760c6dd2ae8774350a2.map.setCenter( gmap\_mc50171796a61c760c6dd2ae8774350a2.positions[235] );
});