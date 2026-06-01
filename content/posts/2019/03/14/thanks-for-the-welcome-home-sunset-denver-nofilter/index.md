---
title: ''
date: '2019-03-14T22:26:28-06:00'
format: image
service: instagram
tags:
- nofilter
latitude: '39.7391'
longitude: '-104.9836'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/03/15042459/53425019_256739411897780_1137424220066554610_n.jpg?resize=607%2C340&ssl=1
---

[![Thanks for the welcome home sunset, Denver. #nofilter](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/03/15042459/53425019_256739411897780_1137424220066554610_n.jpg?resize=607%2C340&ssl=1)](https://dentedreality.com.au/2019/03/14/thanks-for-the-welcome-home-sunset-denver-nofilter/) 

[![Thanks for the welcome home sunset, Denver. #nofilter](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/03/15042459/53425019_256739411897780_1137424220066554610_n.jpg?resize=607%2C340&ssl=1)](https://www.instagram.com/p/BvA_exYHlbP/)

Thanks for the welcome home sunset, Denver. #nofilter

39.7391-104.9836




* #[nofilter](https://dentedreality.com.au/tags/nofilter/)

Posted on [Instagram](https://www.instagram.com/p/BvA_exYHlbP/) [10:26 pm, March 14, 2019](https://dentedreality.com.au/2019/03/14/thanks-for-the-welcome-home-sunset-denver-nofilter/ "10:26 pm") 
jQuery(document).ready(function(){
var gmap\_m8e1231bab7bc685930758b4c8e7b73a0 = {
positions : {
977 : new google.maps.LatLng( '39.7391', '-104.9836' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8e1231bab7bc685930758b4c8e7b73a0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8e1231bab7bc685930758b4c8e7b73a0.positions ) {
gmap\_m8e1231bab7bc685930758b4c8e7b73a0.bounds.extend( gmap\_m8e1231bab7bc685930758b4c8e7b73a0.positions[m] );
}
// Render markers
for ( var m in gmap\_m8e1231bab7bc685930758b4c8e7b73a0.positions ) {
gmap\_m8e1231bab7bc685930758b4c8e7b73a0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8e1231bab7bc685930758b4c8e7b73a0.map,
position : gmap\_m8e1231bab7bc685930758b4c8e7b73a0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8e1231bab7bc685930758b4c8e7b73a0.map.setCenter( gmap\_m8e1231bab7bc685930758b4c8e7b73a0.positions[977] );
});