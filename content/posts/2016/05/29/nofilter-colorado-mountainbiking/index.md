---
title: ''
date: '2016-05-29T23:24:11-06:00'
format: image
service: instagram
tags:
- colorado
- mountainbiking
- nofilter
latitude: '39.623617'
longitude: '-105.3464684'
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/05/13248847_476053422599232_1193380844_n.jpg?fit=640%2C640
---

[![#nofilter #colorado #mountainbiking](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/05/13248847_476053422599232_1193380844_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/05/29/nofilter-colorado-mountainbiking/) 

[![#nofilter #colorado #mountainbiking](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/05/13248847_476053422599232_1193380844_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BGBQD4GCmEV/)

#nofilter #colorado #mountainbiking

39.623617-105.3464684




* #[colorado](https://dentedreality.com.au/tags/colorado/)
* #[mountainbiking](https://dentedreality.com.au/tags/mountainbiking/)
* #[nofilter](https://dentedreality.com.au/tags/nofilter/)

Posted on [Instagram](https://www.instagram.com/p/BGBQD4GCmEV/) [11:24 pm, May 29, 2016](https://dentedreality.com.au/2016/05/29/nofilter-colorado-mountainbiking/ "11:24 pm") 
jQuery(document).ready(function(){
var gmap\_m2cfa26360fdc9dbee77b65e619b2afb7 = {
positions : {
860 : new google.maps.LatLng( '39.623616950172', '-105.34646842473' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2cfa26360fdc9dbee77b65e619b2afb7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2cfa26360fdc9dbee77b65e619b2afb7.positions ) {
gmap\_m2cfa26360fdc9dbee77b65e619b2afb7.bounds.extend( gmap\_m2cfa26360fdc9dbee77b65e619b2afb7.positions[m] );
}
// Render markers
for ( var m in gmap\_m2cfa26360fdc9dbee77b65e619b2afb7.positions ) {
gmap\_m2cfa26360fdc9dbee77b65e619b2afb7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2cfa26360fdc9dbee77b65e619b2afb7.map,
position : gmap\_m2cfa26360fdc9dbee77b65e619b2afb7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2cfa26360fdc9dbee77b65e619b2afb7.map.setCenter( gmap\_m2cfa26360fdc9dbee77b65e619b2afb7.positions[860] );
});