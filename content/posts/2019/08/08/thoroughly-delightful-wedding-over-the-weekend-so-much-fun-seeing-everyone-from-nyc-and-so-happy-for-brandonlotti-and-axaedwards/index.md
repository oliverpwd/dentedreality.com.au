---
title: ''
date: '2019-08-08T17:29:19-06:00'
format: image
service: instagram
latitude: '40.67364'
longitude: '-73.99176'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/08192501/67122173_401111850517246_4021543737572729731_n.jpg?fit=640%2C640&ssl=1
---

[![Thoroughly delightful wedding over the weekend. So much fun seeing everyone from NYC and so happy for @brandonlotti and @axaedwards](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/08192501/67122173_401111850517246_4021543737572729731_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/08/08/thoroughly-delightful-wedding-over-the-weekend-so-much-fun-seeing-everyone-from-nyc-and-so-happy-for-brandonlotti-and-axaedwards/) 

[![Thoroughly delightful wedding over the weekend. So much fun seeing everyone from NYC and so happy for @brandonlotti and @axaedwards](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/08192501/67122173_401111850517246_4021543737572729731_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/B06-U9Xpwuk/)

Thoroughly delightful wedding over the weekend. So much fun seeing everyone from NYC and so happy for @brandonlotti and @axaedwards

40.67364-73.99176




Posted on [Instagram](https://www.instagram.com/p/B06-U9Xpwuk/) [5:29 pm, August 8, 2019](https://dentedreality.com.au/2019/08/08/thoroughly-delightful-wedding-over-the-weekend-so-much-fun-seeing-everyone-from-nyc-and-so-happy-for-brandonlotti-and-axaedwards/ "5:29 pm") 
jQuery(document).ready(function(){
var gmap\_m0e28be9bde9f1feafbde65d14ed6d4d2 = {
positions : {
841 : new google.maps.LatLng( '40.67364', '-73.99176' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0e28be9bde9f1feafbde65d14ed6d4d2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0e28be9bde9f1feafbde65d14ed6d4d2.positions ) {
gmap\_m0e28be9bde9f1feafbde65d14ed6d4d2.bounds.extend( gmap\_m0e28be9bde9f1feafbde65d14ed6d4d2.positions[m] );
}
// Render markers
for ( var m in gmap\_m0e28be9bde9f1feafbde65d14ed6d4d2.positions ) {
gmap\_m0e28be9bde9f1feafbde65d14ed6d4d2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0e28be9bde9f1feafbde65d14ed6d4d2.map,
position : gmap\_m0e28be9bde9f1feafbde65d14ed6d4d2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0e28be9bde9f1feafbde65d14ed6d4d2.map.setCenter( gmap\_m0e28be9bde9f1feafbde65d14ed6d4d2.positions[841] );
});