---
title: ''
date: '2018-06-29T19:22:38-06:00'
format: image
service: instagram
tags:
- fjallravenclassicusa
latitude: '39.4285985'
longitude: '-106.2272464'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182139/35564717_384870665367349_6853135497800187904_n.jpg?resize=607%2C607&ssl=1
---

[![Stumbled into a Windows 95 wallpaper. I'm OK with that. #fjallravenclassicusa](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182139/35564717_384870665367349_6853135497800187904_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/06/29/stumbled-into-a-windows-95-wallpaper-im-ok-with-that-fjallravenclassicusa/) 

[![Stumbled into a Windows 95 wallpaper. I'm OK with that. #fjallravenclassicusa](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182139/35564717_384870665367349_6853135497800187904_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/BkoVWkvlkUF/)

Stumbled into a Windows 95 wallpaper. I’m OK with that. #fjallravenclassicusa

39.4285985-106.2272464




* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BkoVWkvlkUF/) [7:22 pm, June 29, 2018](https://dentedreality.com.au/2018/06/29/stumbled-into-a-windows-95-wallpaper-im-ok-with-that-fjallravenclassicusa/ "7:22 pm") 
jQuery(document).ready(function(){
var gmap\_m16c57db1be19c3d65619c452cc834373 = {
positions : {
681 : new google.maps.LatLng( '39.4285985', '-106.2272464' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m16c57db1be19c3d65619c452cc834373' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m16c57db1be19c3d65619c452cc834373.positions ) {
gmap\_m16c57db1be19c3d65619c452cc834373.bounds.extend( gmap\_m16c57db1be19c3d65619c452cc834373.positions[m] );
}
// Render markers
for ( var m in gmap\_m16c57db1be19c3d65619c452cc834373.positions ) {
gmap\_m16c57db1be19c3d65619c452cc834373.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m16c57db1be19c3d65619c452cc834373.map,
position : gmap\_m16c57db1be19c3d65619c452cc834373.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m16c57db1be19c3d65619c452cc834373.map.setCenter( gmap\_m16c57db1be19c3d65619c452cc834373.positions[681] );
});