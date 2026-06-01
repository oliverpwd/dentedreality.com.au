---
title: ''
date: '2019-02-16T02:59:19-07:00'
format: image
service: instagram
tags:
- djimavicair
- dronestagram
latitude: '64.1333'
longitude: '-21.9333'
image: https://dentedreality.com.au/wp-content/uploads/2019/02/50824527_1543345509131328_7678713588377088803_n.jpg
---

[![Good morning, Reykjavík. #dronestagram #djimavicair](https://dentedreality.com.au/wp-content/uploads/2019/02/50824527_1543345509131328_7678713588377088803_n.jpg)](https://dentedreality.com.au/2019/02/16/good-morning-reykjavik-dronestagram-djimavicair/) 

[![Good morning, Reykjavík. #dronestagram #djimavicair](https://dentedreality.com.au/wp-content/uploads/2019/02/50824527_1543345509131328_7678713588377088803_n.jpg)](https://www.instagram.com/p/Bt8EG_iHm8b/)

Good morning, Reykjavík. #dronestagram #djimavicair

64.1333-21.9333




* #[djimavicair](https://dentedreality.com.au/tags/djimavicair/)
* #[dronestagram](https://dentedreality.com.au/tags/dronestagram/)

Posted on [Instagram](https://www.instagram.com/p/Bt8EG_iHm8b/) [2:59 am, February 16, 2019](https://dentedreality.com.au/2019/02/16/good-morning-reykjavik-dronestagram-djimavicair/ "2:59 am") 
jQuery(document).ready(function(){
var gmap\_m7c5f9593d11813d797ebcc17ca998680 = {
positions : {
608 : new google.maps.LatLng( '64.1333', '-21.9333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7c5f9593d11813d797ebcc17ca998680' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7c5f9593d11813d797ebcc17ca998680.positions ) {
gmap\_m7c5f9593d11813d797ebcc17ca998680.bounds.extend( gmap\_m7c5f9593d11813d797ebcc17ca998680.positions[m] );
}
// Render markers
for ( var m in gmap\_m7c5f9593d11813d797ebcc17ca998680.positions ) {
gmap\_m7c5f9593d11813d797ebcc17ca998680.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7c5f9593d11813d797ebcc17ca998680.map,
position : gmap\_m7c5f9593d11813d797ebcc17ca998680.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7c5f9593d11813d797ebcc17ca998680.map.setCenter( gmap\_m7c5f9593d11813d797ebcc17ca998680.positions[608] );
});