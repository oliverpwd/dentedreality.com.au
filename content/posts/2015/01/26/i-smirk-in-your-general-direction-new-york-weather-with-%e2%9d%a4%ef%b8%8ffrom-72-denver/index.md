---
title: ''
date: '2015-01-26T14:21:24+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/01/10950358_814804455232632_28737692_n.jpg?resize=640%2C640
---

[![I smirk in your general direction, New York weather. With ❤️from 72° Denver.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/01/10950358_814804455232632_28737692_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/01/26/i-smirk-in-your-general-direction-new-york-weather-with-%e2%9d%a4%ef%b8%8ffrom-72-denver/) 

I smirk in your general direction, New York weather. With ❤️from 72° Denver.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/yVQF7EimI2/) [2:21 pm, January 26, 2015](http://dentedreality.com.au/2015/01/26/i-smirk-in-your-general-direction-new-york-weather-with-%e2%9d%a4%ef%b8%8ffrom-72-denver/ "2:21 pm") 
jQuery(document).ready(function(){
var gmap\_m45c2c7f4d7cf7e58f82aa3f5bf6487c8 = {
positions : {
275 : new google.maps.LatLng( '39.734221667', '-104.978561667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m45c2c7f4d7cf7e58f82aa3f5bf6487c8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m45c2c7f4d7cf7e58f82aa3f5bf6487c8.positions ) {
gmap\_m45c2c7f4d7cf7e58f82aa3f5bf6487c8.bounds.extend( gmap\_m45c2c7f4d7cf7e58f82aa3f5bf6487c8.positions[m] );
}
// Render markers
for ( var m in gmap\_m45c2c7f4d7cf7e58f82aa3f5bf6487c8.positions ) {
gmap\_m45c2c7f4d7cf7e58f82aa3f5bf6487c8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m45c2c7f4d7cf7e58f82aa3f5bf6487c8.map,
position : gmap\_m45c2c7f4d7cf7e58f82aa3f5bf6487c8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m45c2c7f4d7cf7e58f82aa3f5bf6487c8.map.setCenter( gmap\_m45c2c7f4d7cf7e58f82aa3f5bf6487c8.positions[275] );
});