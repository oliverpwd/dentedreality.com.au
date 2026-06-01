---
title: ''
date: '2019-03-23T11:49:07-06:00'
format: image
service: instagram
latitude: '39.7532'
longitude: '-105.05363'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/03/23122513/53822853_2688168897920946_68893446977784979_n.jpg?fit=640%2C640&ssl=1
---

[![First day on the rooftop at @joyridebrewing!](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/03/23122513/53822853_2688168897920946_68893446977784979_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/03/23/first-day-on-the-rooftop-at-joyridebrewing/) 

[![First day on the rooftop at @joyridebrewing!](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/03/23122513/53822853_2688168897920946_68893446977784979_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BvXBshNnamO/)

First day on the rooftop at @joyridebrewing!

39.7532-105.05363




Posted on [Instagram](https://www.instagram.com/p/BvXBshNnamO/) [11:49 am, March 23, 2019](https://dentedreality.com.au/2019/03/23/first-day-on-the-rooftop-at-joyridebrewing/ "11:49 am") 
jQuery(document).ready(function(){
var gmap\_mc17a204fa82745771d2959e7d20104a6 = {
positions : {
773 : new google.maps.LatLng( '39.7532', '-105.05363' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc17a204fa82745771d2959e7d20104a6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc17a204fa82745771d2959e7d20104a6.positions ) {
gmap\_mc17a204fa82745771d2959e7d20104a6.bounds.extend( gmap\_mc17a204fa82745771d2959e7d20104a6.positions[m] );
}
// Render markers
for ( var m in gmap\_mc17a204fa82745771d2959e7d20104a6.positions ) {
gmap\_mc17a204fa82745771d2959e7d20104a6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc17a204fa82745771d2959e7d20104a6.map,
position : gmap\_mc17a204fa82745771d2959e7d20104a6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc17a204fa82745771d2959e7d20104a6.map.setCenter( gmap\_mc17a204fa82745771d2959e7d20104a6.positions[773] );
});