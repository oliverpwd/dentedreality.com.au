---
title: ''
date: '2019-02-21T17:08:14-07:00'
format: image
service: instagram
tags:
- iceland
latitude: '64.8305556'
longitude: '-17.9866667'
image: https://dentedreality.com.au/wp-content/uploads/2019/02/52135198_2399544073391444_1981404522918696215_n.jpg
---

[![Taking photos at the edge of the world. #iceland](https://dentedreality.com.au/wp-content/uploads/2019/02/52135198_2399544073391444_1981404522918696215_n.jpg)](https://dentedreality.com.au/2019/02/21/taking-photos-at-the-edge-of-the-world-iceland/) 

[![Taking photos at the edge of the world. #iceland](https://dentedreality.com.au/wp-content/uploads/2019/02/52135198_2399544073391444_1981404522918696215_n.jpg)](https://www.instagram.com/p/BuKdPA9nEys/)

Taking photos at the edge of the world. #iceland

64.8305556-17.9866667




* #[iceland](https://dentedreality.com.au/tags/iceland/)

Posted on [Instagram](https://www.instagram.com/p/BuKdPA9nEys/) [5:08 pm, February 21, 2019](https://dentedreality.com.au/2019/02/21/taking-photos-at-the-edge-of-the-world-iceland/ "5:08 pm") 
jQuery(document).ready(function(){
var gmap\_m4df0c55d01deb57acb2e2625e8b76028 = {
positions : {
948 : new google.maps.LatLng( '64.8305556', '-17.9866667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4df0c55d01deb57acb2e2625e8b76028' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4df0c55d01deb57acb2e2625e8b76028.positions ) {
gmap\_m4df0c55d01deb57acb2e2625e8b76028.bounds.extend( gmap\_m4df0c55d01deb57acb2e2625e8b76028.positions[m] );
}
// Render markers
for ( var m in gmap\_m4df0c55d01deb57acb2e2625e8b76028.positions ) {
gmap\_m4df0c55d01deb57acb2e2625e8b76028.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4df0c55d01deb57acb2e2625e8b76028.map,
position : gmap\_m4df0c55d01deb57acb2e2625e8b76028.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4df0c55d01deb57acb2e2625e8b76028.map.setCenter( gmap\_m4df0c55d01deb57acb2e2625e8b76028.positions[948] );
});