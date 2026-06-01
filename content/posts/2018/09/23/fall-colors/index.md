---
title: ''
date: '2018-09-23T20:36:42-06:00'
format: image
service: instagram
latitude: '39.4864'
longitude: '-106.044'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2018/09/14182051/41712144_699398347094433_7698242132709277019_n.jpg
---

[![Fall colors.](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2018/09/14182051/41712144_699398347094433_7698242132709277019_n.jpg)](https://dentedreality.com.au/2018/09/23/fall-colors/) 

[![Fall colors.](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2018/09/14182051/41712144_699398347094433_7698242132709277019_n.jpg)](https://www.instagram.com/p/BoF6MPll-nJ/)

Fall colors.

39.4864-106.044




Posted on [Instagram](https://www.instagram.com/p/BoF6MPll-nJ/) [8:36 pm, September 23, 2018](https://dentedreality.com.au/2018/09/23/fall-colors/ "8:36 pm") 
jQuery(document).ready(function(){
var gmap\_m27133d640f34f0889115dae7c97e1254 = {
positions : {
727 : new google.maps.LatLng( '39.4864', '-106.044' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m27133d640f34f0889115dae7c97e1254' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m27133d640f34f0889115dae7c97e1254.positions ) {
gmap\_m27133d640f34f0889115dae7c97e1254.bounds.extend( gmap\_m27133d640f34f0889115dae7c97e1254.positions[m] );
}
// Render markers
for ( var m in gmap\_m27133d640f34f0889115dae7c97e1254.positions ) {
gmap\_m27133d640f34f0889115dae7c97e1254.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m27133d640f34f0889115dae7c97e1254.map,
position : gmap\_m27133d640f34f0889115dae7c97e1254.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m27133d640f34f0889115dae7c97e1254.map.setCenter( gmap\_m27133d640f34f0889115dae7c97e1254.positions[727] );
});