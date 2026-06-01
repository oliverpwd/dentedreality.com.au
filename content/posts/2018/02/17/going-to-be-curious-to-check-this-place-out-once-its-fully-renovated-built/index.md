---
title: ''
date: '2018-02-17T12:50:11+00:00'
format: image
service: instagram
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2018/02/27579917_161940964597519_2246496955003830272_n.jpg?fit=640%2C640&ssl=1
---

[![Going to be curious to check this place out once it's fully renovated/built.](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2018/02/27579917_161940964597519_2246496955003830272_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2018/02/17/going-to-be-curious-to-check-this-place-out-once-its-fully-renovated-built/) 

[![Going to be curious to check this place out once it's fully renovated/built.](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2018/02/27579917_161940964597519_2246496955003830272_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BfT2YFLhsfY/)

Going to be curious to check this place out once it’s fully renovated/built.





Posted on [Instagram](https://www.instagram.com/p/BfT2YFLhsfY/) [12:50 pm, February 17, 2018](https://dentedreality.com.au/2018/02/17/going-to-be-curious-to-check-this-place-out-once-its-fully-renovated-built/ "12:50 pm") 
jQuery(document).ready(function(){
var gmap\_md93459d5e499db1586b0662cd11216dd = {
positions : {
462 : new google.maps.LatLng( '39.7714227', '-104.9675534' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md93459d5e499db1586b0662cd11216dd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md93459d5e499db1586b0662cd11216dd.positions ) {
gmap\_md93459d5e499db1586b0662cd11216dd.bounds.extend( gmap\_md93459d5e499db1586b0662cd11216dd.positions[m] );
}
// Render markers
for ( var m in gmap\_md93459d5e499db1586b0662cd11216dd.positions ) {
gmap\_md93459d5e499db1586b0662cd11216dd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md93459d5e499db1586b0662cd11216dd.map,
position : gmap\_md93459d5e499db1586b0662cd11216dd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md93459d5e499db1586b0662cd11216dd.map.setCenter( gmap\_md93459d5e499db1586b0662cd11216dd.positions[462] );
});