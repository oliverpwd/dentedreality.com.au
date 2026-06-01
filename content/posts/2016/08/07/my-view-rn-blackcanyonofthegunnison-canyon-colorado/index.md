---
title: ''
date: '2016-08-07T17:41:29+00:00'
format: image
service: instagram
tags:
- blackcanyonofthegunnison
- canyon
- colorado
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13724684_541790686006415_1433768259_n.jpg?fit=640%2C640
---

[![My view rn. #blackcanyonofthegunnison #canyon #colorado](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13724684_541790686006415_1433768259_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/08/07/my-view-rn-blackcanyonofthegunnison-canyon-colorado/) 

My view rn. #blackcanyonofthegunnison #canyon #colorado





* #[blackcanyonofthegunnison](http://dentedreality.com.au/tags/blackcanyonofthegunnison/)
* #[canyon](http://dentedreality.com.au/tags/canyon/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)

Posted on [Instagram](https://www.instagram.com/p/BI04fEfgZZx/) [5:41 pm, August 7, 2016](http://dentedreality.com.au/2016/08/07/my-view-rn-blackcanyonofthegunnison-canyon-colorado/ "5:41 pm") 
jQuery(document).ready(function(){
var gmap\_mbc2fa8393dd6fab5b4b225540b6719be = {
positions : {
326 : new google.maps.LatLng( '38.488869182295', '-107.74033621979' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbc2fa8393dd6fab5b4b225540b6719be' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbc2fa8393dd6fab5b4b225540b6719be.positions ) {
gmap\_mbc2fa8393dd6fab5b4b225540b6719be.bounds.extend( gmap\_mbc2fa8393dd6fab5b4b225540b6719be.positions[m] );
}
// Render markers
for ( var m in gmap\_mbc2fa8393dd6fab5b4b225540b6719be.positions ) {
gmap\_mbc2fa8393dd6fab5b4b225540b6719be.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbc2fa8393dd6fab5b4b225540b6719be.map,
position : gmap\_mbc2fa8393dd6fab5b4b225540b6719be.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbc2fa8393dd6fab5b4b225540b6719be.map.setCenter( gmap\_mbc2fa8393dd6fab5b4b225540b6719be.positions[326] );
});