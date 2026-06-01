---
title: ''
date: '2019-08-23T19:26:56-06:00'
format: image
service: instagram
latitude: '39.75034'
longitude: '-104.98401'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/23202454/67683184_2716129278406104_666393861655493082_n.jpg?fit=640%2C640&ssl=1
---

[![Solar powered USB ports on a patio umbrella 🤯🤯🤯](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/23202454/67683184_2716129278406104_666393861655493082_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/08/23/solar-powered-usb-ports-on-a-patio-umbrella-%f0%9f%a4%af%f0%9f%a4%af%f0%9f%a4%af/) 

[![Solar powered USB ports on a patio umbrella 🤯🤯🤯](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/23202454/67683184_2716129278406104_666393861655493082_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/B1hztjHpp84/)

Solar powered USB ports on a patio umbrella 🤯🤯🤯

39.75034-104.98401




Posted on [Instagram](https://www.instagram.com/p/B1hztjHpp84/) [7:26 pm, August 23, 2019](https://dentedreality.com.au/2019/08/23/solar-powered-usb-ports-on-a-patio-umbrella-%f0%9f%a4%af%f0%9f%a4%af%f0%9f%a4%af/ "7:26 pm") 
jQuery(document).ready(function(){
var gmap\_m54ef7ff5b2253d6883236ef85c424f24 = {
positions : {
940 : new google.maps.LatLng( '39.75034', '-104.98401' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m54ef7ff5b2253d6883236ef85c424f24' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m54ef7ff5b2253d6883236ef85c424f24.positions ) {
gmap\_m54ef7ff5b2253d6883236ef85c424f24.bounds.extend( gmap\_m54ef7ff5b2253d6883236ef85c424f24.positions[m] );
}
// Render markers
for ( var m in gmap\_m54ef7ff5b2253d6883236ef85c424f24.positions ) {
gmap\_m54ef7ff5b2253d6883236ef85c424f24.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m54ef7ff5b2253d6883236ef85c424f24.map,
position : gmap\_m54ef7ff5b2253d6883236ef85c424f24.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m54ef7ff5b2253d6883236ef85c424f24.map.setCenter( gmap\_m54ef7ff5b2253d6883236ef85c424f24.positions[940] );
});