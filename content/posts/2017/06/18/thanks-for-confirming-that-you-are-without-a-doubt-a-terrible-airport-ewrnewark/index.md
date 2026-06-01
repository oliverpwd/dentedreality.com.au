---
title: ''
date: '2017-06-18T10:23:33-06:00'
format: image
service: instagram
latitude: '40.6925'
longitude: '-74.1686'
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/06/19122398_1891261317796207_7305632507414708224_n.jpg?fit=640%2C640&ssl=1
---

[![Thanks for confirming that you are, without a doubt, a terrible airport, EWR/Newark.](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/06/19122398_1891261317796207_7305632507414708224_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/06/18/thanks-for-confirming-that-you-are-without-a-doubt-a-terrible-airport-ewrnewark/) 

[![Thanks for confirming that you are, without a doubt, a terrible airport, EWR/Newark.](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/06/19122398_1891261317796207_7305632507414708224_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BVfMxLVBr6o/)

Thanks for confirming that you are, without a doubt, a terrible airport, EWR/Newark.

40.6925-74.1686




Posted on [Instagram](https://www.instagram.com/p/BVfMxLVBr6o/) [10:23 am, June 18, 2017](https://dentedreality.com.au/2017/06/18/thanks-for-confirming-that-you-are-without-a-doubt-a-terrible-airport-ewrnewark/ "10:23 am") 
jQuery(document).ready(function(){
var gmap\_mf32411b1817b7fa5f58482e270c90b5d = {
positions : {
12 : new google.maps.LatLng( '40.6925', '-74.1686' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf32411b1817b7fa5f58482e270c90b5d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf32411b1817b7fa5f58482e270c90b5d.positions ) {
gmap\_mf32411b1817b7fa5f58482e270c90b5d.bounds.extend( gmap\_mf32411b1817b7fa5f58482e270c90b5d.positions[m] );
}
// Render markers
for ( var m in gmap\_mf32411b1817b7fa5f58482e270c90b5d.positions ) {
gmap\_mf32411b1817b7fa5f58482e270c90b5d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf32411b1817b7fa5f58482e270c90b5d.map,
position : gmap\_mf32411b1817b7fa5f58482e270c90b5d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf32411b1817b7fa5f58482e270c90b5d.map.setCenter( gmap\_mf32411b1817b7fa5f58482e270c90b5d.positions[12] );
});