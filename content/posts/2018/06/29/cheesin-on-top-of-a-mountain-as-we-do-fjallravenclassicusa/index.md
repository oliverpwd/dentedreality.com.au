---
title: ''
date: '2018-06-29T19:27:16-06:00'
format: image
service: instagram
tags:
- fjallravenclassicusa
latitude: '40.1619'
longitude: '-106.128'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182136/35617443_234346420693084_6542655778010955776_n.jpg?resize=607%2C607&ssl=1
---

[![Cheesin' on top of a mountain, as we do! #fjallravenclassicusa](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182136/35617443_234346420693084_6542655778010955776_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/06/29/cheesin-on-top-of-a-mountain-as-we-do-fjallravenclassicusa/) 

[![Cheesin' on top of a mountain, as we do! #fjallravenclassicusa](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182136/35617443_234346420693084_6542655778010955776_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/BkoV4g5lxFx/)

Cheesin’ on top of a mountain, as we do! #fjallravenclassicusa

40.1619-106.128




* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BkoV4g5lxFx/) [7:27 pm, June 29, 2018](https://dentedreality.com.au/2018/06/29/cheesin-on-top-of-a-mountain-as-we-do-fjallravenclassicusa/ "7:27 pm") 
jQuery(document).ready(function(){
var gmap\_m23dbd490be3db13b67cd43eb60fb9dbe = {
positions : {
992 : new google.maps.LatLng( '40.1619', '-106.128' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m23dbd490be3db13b67cd43eb60fb9dbe' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m23dbd490be3db13b67cd43eb60fb9dbe.positions ) {
gmap\_m23dbd490be3db13b67cd43eb60fb9dbe.bounds.extend( gmap\_m23dbd490be3db13b67cd43eb60fb9dbe.positions[m] );
}
// Render markers
for ( var m in gmap\_m23dbd490be3db13b67cd43eb60fb9dbe.positions ) {
gmap\_m23dbd490be3db13b67cd43eb60fb9dbe.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m23dbd490be3db13b67cd43eb60fb9dbe.map,
position : gmap\_m23dbd490be3db13b67cd43eb60fb9dbe.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m23dbd490be3db13b67cd43eb60fb9dbe.map.setCenter( gmap\_m23dbd490be3db13b67cd43eb60fb9dbe.positions[992] );
});