---
title: ''
date: '2017-07-24T22:47:17+00:00'
format: image
service: instagram
tags:
- camping
- canoecamping
- coleman
- tent
image: https://dentedreality.com.au/wp-content/uploads/2017/07/20225454_106150706728409_5027273054057660416_n.jpg
---

[![Tents in the darkness. #canoecamping #camping #tent #coleman](https://dentedreality.com.au/wp-content/uploads/2017/07/20225454_106150706728409_5027273054057660416_n.jpg)](https://dentedreality.com.au/2017/07/24/tents-in-the-darkness-canoecamping-camping-tent-coleman/) 

[![Tents in the darkness. #canoecamping #camping #tent #coleman](https://dentedreality.com.au/wp-content/uploads/2017/07/20225454_106150706728409_5027273054057660416_n.jpg)](https://www.instagram.com/p/BW9Of5ghB1I/)

Tents in the darkness. #canoecamping #camping #tent #coleman





* #[camping](https://dentedreality.com.au/tags/camping/)
* #[canoecamping](https://dentedreality.com.au/tags/canoecamping/)
* #[coleman](https://dentedreality.com.au/tags/coleman/)
* #[tent](https://dentedreality.com.au/tags/tent/)

Posted on [Instagram](https://www.instagram.com/p/BW9Of5ghB1I/) [10:47 pm, July 24, 2017](https://dentedreality.com.au/2017/07/24/tents-in-the-darkness-canoecamping-camping-tent-coleman/ "10:47 pm") 
jQuery(document).ready(function(){
var gmap\_md6d7657b3574e59117ad5ae109a68f2f = {
positions : {
785 : new google.maps.LatLng( '39.862997046629', '-105.08438988874' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md6d7657b3574e59117ad5ae109a68f2f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md6d7657b3574e59117ad5ae109a68f2f.positions ) {
gmap\_md6d7657b3574e59117ad5ae109a68f2f.bounds.extend( gmap\_md6d7657b3574e59117ad5ae109a68f2f.positions[m] );
}
// Render markers
for ( var m in gmap\_md6d7657b3574e59117ad5ae109a68f2f.positions ) {
gmap\_md6d7657b3574e59117ad5ae109a68f2f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md6d7657b3574e59117ad5ae109a68f2f.map,
position : gmap\_md6d7657b3574e59117ad5ae109a68f2f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md6d7657b3574e59117ad5ae109a68f2f.map.setCenter( gmap\_md6d7657b3574e59117ad5ae109a68f2f.positions[785] );
});