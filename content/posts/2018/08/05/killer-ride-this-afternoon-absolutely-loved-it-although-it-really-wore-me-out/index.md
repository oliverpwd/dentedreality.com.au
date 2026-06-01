---
title: ''
date: '2018-08-05T00:29:09-06:00'
format: image
service: instagram
latitude: '39.0957279'
longitude: '-106.1018957'
image: https://dentedreality.com.au/wp-content/uploads/2018/08/37701694_2215628121993736_8057650640647618560_n.jpg
---

[![Killer ride this afternoon. Absolutely loved it, although it really wore me out.](https://dentedreality.com.au/wp-content/uploads/2018/08/37701694_2215628121993736_8057650640647618560_n.jpg)](https://dentedreality.com.au/2018/08/05/killer-ride-this-afternoon-absolutely-loved-it-although-it-really-wore-me-out/) 

[![Killer ride this afternoon. Absolutely loved it, although it really wore me out.](https://dentedreality.com.au/wp-content/uploads/2018/08/37701694_2215628121993736_8057650640647618560_n.jpg)](https://www.instagram.com/p/BmFlDAgF4u8/)

Killer ride this afternoon. Absolutely loved it, although it really wore me out.

39.0957279-106.1018957




Posted on [Instagram](https://www.instagram.com/p/BmFlDAgF4u8/) [12:29 am, August 5, 2018](https://dentedreality.com.au/2018/08/05/killer-ride-this-afternoon-absolutely-loved-it-although-it-really-wore-me-out/ "12:29 am") 
jQuery(document).ready(function(){
var gmap\_m9fbe8192128051d86c3d7644850107e0 = {
positions : {
681 : new google.maps.LatLng( '39.0957279', '-106.1018957' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9fbe8192128051d86c3d7644850107e0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9fbe8192128051d86c3d7644850107e0.positions ) {
gmap\_m9fbe8192128051d86c3d7644850107e0.bounds.extend( gmap\_m9fbe8192128051d86c3d7644850107e0.positions[m] );
}
// Render markers
for ( var m in gmap\_m9fbe8192128051d86c3d7644850107e0.positions ) {
gmap\_m9fbe8192128051d86c3d7644850107e0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9fbe8192128051d86c3d7644850107e0.map,
position : gmap\_m9fbe8192128051d86c3d7644850107e0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9fbe8192128051d86c3d7644850107e0.map.setCenter( gmap\_m9fbe8192128051d86c3d7644850107e0.positions[681] );
});