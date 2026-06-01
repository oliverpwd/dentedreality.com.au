---
title: ''
date: '2017-07-24T22:42:55+00:00'
format: image
service: instagram
tags:
- canoecamping
- canoeing
- canyon
- colorado
- river
- utah
image: https://dentedreality.com.au/wp-content/uploads/2017/07/20225476_327682217656870_8446783447988436992_n.jpg
---

[![Day Two campsite. Incredible. #canoeing #canoecamping #colorado #utah #river #canyon](https://dentedreality.com.au/wp-content/uploads/2017/07/20225476_327682217656870_8446783447988436992_n.jpg)](https://dentedreality.com.au/2017/07/24/day-two-campsite-incredible-canoeing-canoecamping-colorado-utah-river-canyon/) 

[![Day Two campsite. Incredible. #canoeing #canoecamping #colorado #utah #river #canyon](https://dentedreality.com.au/wp-content/uploads/2017/07/20225476_327682217656870_8446783447988436992_n.jpg)](https://www.instagram.com/p/BW9N_7HBf4p/)

Day Two campsite. Incredible. #canoeing #canoecamping #colorado #utah #river #canyon





* #[canoecamping](https://dentedreality.com.au/tags/canoecamping/)
* #[canoeing](https://dentedreality.com.au/tags/canoeing/)
* #[canyon](https://dentedreality.com.au/tags/canyon/)
* #[colorado](https://dentedreality.com.au/tags/colorado/)
* #[river](https://dentedreality.com.au/tags/river/)
* #[utah](https://dentedreality.com.au/tags/utah/)

Posted on [Instagram](https://www.instagram.com/p/BW9N_7HBf4p/) [10:42 pm, July 24, 2017](https://dentedreality.com.au/2017/07/24/day-two-campsite-incredible-canoeing-canoecamping-colorado-utah-river-canyon/ "10:42 pm") 
jQuery(document).ready(function(){
var gmap\_m1013717c82ee4fd64bfab1f32935f3a0 = {
positions : {
143 : new google.maps.LatLng( '39.142171016667', '-109.00057068333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1013717c82ee4fd64bfab1f32935f3a0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1013717c82ee4fd64bfab1f32935f3a0.positions ) {
gmap\_m1013717c82ee4fd64bfab1f32935f3a0.bounds.extend( gmap\_m1013717c82ee4fd64bfab1f32935f3a0.positions[m] );
}
// Render markers
for ( var m in gmap\_m1013717c82ee4fd64bfab1f32935f3a0.positions ) {
gmap\_m1013717c82ee4fd64bfab1f32935f3a0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1013717c82ee4fd64bfab1f32935f3a0.map,
position : gmap\_m1013717c82ee4fd64bfab1f32935f3a0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1013717c82ee4fd64bfab1f32935f3a0.map.setCenter( gmap\_m1013717c82ee4fd64bfab1f32935f3a0.positions[143] );
});