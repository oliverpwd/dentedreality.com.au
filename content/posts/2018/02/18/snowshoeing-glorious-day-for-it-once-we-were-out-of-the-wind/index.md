---
title: ''
date: '2018-02-18T18:48:41+00:00'
format: image
service: instagram
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2018/02/27878610_189478838486984_962855157215789056_n.jpg?fit=640%2C640&ssl=1
---

[![Snowshoeing! Glorious day for it once we were out of the wind.](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2018/02/27878610_189478838486984_962855157215789056_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2018/02/18/snowshoeing-glorious-day-for-it-once-we-were-out-of-the-wind/) 

[![Snowshoeing! Glorious day for it once we were out of the wind.](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2018/02/27878610_189478838486984_962855157215789056_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BfXEMsiBk-v/)

Snowshoeing! Glorious day for it once we were out of the wind.





Posted on [Instagram](https://www.instagram.com/p/BfXEMsiBk-v/) [6:48 pm, February 18, 2018](https://dentedreality.com.au/2018/02/18/snowshoeing-glorious-day-for-it-once-we-were-out-of-the-wind/ "6:48 pm") 
jQuery(document).ready(function(){
var gmap\_m0374e97f6e62238853710879d3c06f0f = {
positions : {
775 : new google.maps.LatLng( '39.9024', '-105.646' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0374e97f6e62238853710879d3c06f0f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0374e97f6e62238853710879d3c06f0f.positions ) {
gmap\_m0374e97f6e62238853710879d3c06f0f.bounds.extend( gmap\_m0374e97f6e62238853710879d3c06f0f.positions[m] );
}
// Render markers
for ( var m in gmap\_m0374e97f6e62238853710879d3c06f0f.positions ) {
gmap\_m0374e97f6e62238853710879d3c06f0f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0374e97f6e62238853710879d3c06f0f.map,
position : gmap\_m0374e97f6e62238853710879d3c06f0f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0374e97f6e62238853710879d3c06f0f.map.setCenter( gmap\_m0374e97f6e62238853710879d3c06f0f.positions[775] );
});