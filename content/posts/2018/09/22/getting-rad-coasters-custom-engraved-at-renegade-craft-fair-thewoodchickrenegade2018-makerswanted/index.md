---
title: ''
date: '2018-09-22T13:41:14-07:00'
format: image
service: instagram
tags:
- makerswanted
- thewoodchickrenegade2018
latitude: '39.7676'
longitude: '-104.97508'
image: https://dentedreality.com.au/wp-content/uploads/2018/09/41203432_2164699217117053_7218327051875977592_n.jpg
---

[![Getting rad coasters custom engraved at Renegade Craft Fair #thewoodchickrenegade2018 #makerswanted](https://dentedreality.com.au/wp-content/uploads/2018/09/41203432_2164699217117053_7218327051875977592_n.jpg)](https://dentedreality.com.au/2018/09/22/getting-rad-coasters-custom-engraved-at-renegade-craft-fair-thewoodchickrenegade2018-makerswanted/) 

[![Getting rad coasters custom engraved at Renegade Craft Fair #thewoodchickrenegade2018 #makerswanted](https://dentedreality.com.au/wp-content/uploads/2018/09/41203432_2164699217117053_7218327051875977592_n.jpg)](https://www.instagram.com/p/BoCl2YhF8X8/)

Getting rad coasters custom engraved at Renegade Craft Fair #thewoodchickrenegade2018 #makerswanted

39.7676-104.97508




* #[makerswanted](https://dentedreality.com.au/tags/makerswanted/)
* #[thewoodchickrenegade2018](https://dentedreality.com.au/tags/thewoodchickrenegade2018/)

Posted on [Instagram](https://www.instagram.com/p/BoCl2YhF8X8/) [1:41 pm, September 22, 2018](https://dentedreality.com.au/2018/09/22/getting-rad-coasters-custom-engraved-at-renegade-craft-fair-thewoodchickrenegade2018-makerswanted/ "1:41 pm") 
jQuery(document).ready(function(){
var gmap\_m4b4da17353e1b8270b3b18c24d080497 = {
positions : {
376 : new google.maps.LatLng( '39.7676', '-104.97508' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4b4da17353e1b8270b3b18c24d080497' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4b4da17353e1b8270b3b18c24d080497.positions ) {
gmap\_m4b4da17353e1b8270b3b18c24d080497.bounds.extend( gmap\_m4b4da17353e1b8270b3b18c24d080497.positions[m] );
}
// Render markers
for ( var m in gmap\_m4b4da17353e1b8270b3b18c24d080497.positions ) {
gmap\_m4b4da17353e1b8270b3b18c24d080497.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4b4da17353e1b8270b3b18c24d080497.map,
position : gmap\_m4b4da17353e1b8270b3b18c24d080497.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4b4da17353e1b8270b3b18c24d080497.map.setCenter( gmap\_m4b4da17353e1b8270b3b18c24d080497.positions[376] );
});