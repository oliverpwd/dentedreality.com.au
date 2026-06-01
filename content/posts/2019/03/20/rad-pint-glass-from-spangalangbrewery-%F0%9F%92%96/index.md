---
title: ''
date: '2019-03-20T15:51:41-06:00'
format: image
service: instagram
latitude: '39.7551834'
longitude: '-104.9770549'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/03/21162503/54446770_839253493080886_5316612237431615721_n.jpg?fit=640%2C640&ssl=1
---

[![Rad pint glass from @spangalangbrewery. 💖](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/03/21162503/54446770_839253493080886_5316612237431615721_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/03/20/rad-pint-glass-from-spangalangbrewery-%f0%9f%92%96/) 

[![Rad pint glass from @spangalangbrewery. 💖](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/03/21162503/54446770_839253493080886_5316612237431615721_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BvPvEjOnEhA/)

Rad pint glass from @spangalangbrewery. 💖

39.7551834-104.9770549




Posted on [Instagram](https://www.instagram.com/p/BvPvEjOnEhA/) [3:51 pm, March 20, 2019](https://dentedreality.com.au/2019/03/20/rad-pint-glass-from-spangalangbrewery-%f0%9f%92%96/ "3:51 pm") 
jQuery(document).ready(function(){
var gmap\_m40fd49c39d87818083b3aa14f4253eec = {
positions : {
738 : new google.maps.LatLng( '39.7551834', '-104.9770549' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m40fd49c39d87818083b3aa14f4253eec' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m40fd49c39d87818083b3aa14f4253eec.positions ) {
gmap\_m40fd49c39d87818083b3aa14f4253eec.bounds.extend( gmap\_m40fd49c39d87818083b3aa14f4253eec.positions[m] );
}
// Render markers
for ( var m in gmap\_m40fd49c39d87818083b3aa14f4253eec.positions ) {
gmap\_m40fd49c39d87818083b3aa14f4253eec.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m40fd49c39d87818083b3aa14f4253eec.map,
position : gmap\_m40fd49c39d87818083b3aa14f4253eec.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m40fd49c39d87818083b3aa14f4253eec.map.setCenter( gmap\_m40fd49c39d87818083b3aa14f4253eec.positions[738] );
});