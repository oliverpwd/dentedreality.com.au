---
title: ''
date: '2019-03-09T11:44:31-06:00'
format: image
service: instagram
latitude: '37.7717185'
longitude: '-122.4438929'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/03/14181928/52643288_381003689402862_5398233722619418957_n.jpg?resize=607%2C607&ssl=1
---

[![SF Ocean Beach breakwaters](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/03/14181928/52643288_381003689402862_5398233722619418957_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2019/03/09/sf-ocean-beach-breakwaters/) 

[![SF Ocean Beach breakwaters](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/03/14181928/52643288_381003689402862_5398233722619418957_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/BuzE5_vn6Pw/)

SF Ocean Beach breakwaters

37.7717185-122.4438929




Posted on [Instagram](https://www.instagram.com/p/BuzE5_vn6Pw/) [11:44 am, March 9, 2019](https://dentedreality.com.au/2019/03/09/sf-ocean-beach-breakwaters/ "11:44 am") 
jQuery(document).ready(function(){
var gmap\_m8be0e9c371f751b36fd4883ad4fce5e3 = {
positions : {
542 : new google.maps.LatLng( '37.7717185', '-122.4438929' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8be0e9c371f751b36fd4883ad4fce5e3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8be0e9c371f751b36fd4883ad4fce5e3.positions ) {
gmap\_m8be0e9c371f751b36fd4883ad4fce5e3.bounds.extend( gmap\_m8be0e9c371f751b36fd4883ad4fce5e3.positions[m] );
}
// Render markers
for ( var m in gmap\_m8be0e9c371f751b36fd4883ad4fce5e3.positions ) {
gmap\_m8be0e9c371f751b36fd4883ad4fce5e3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8be0e9c371f751b36fd4883ad4fce5e3.map,
position : gmap\_m8be0e9c371f751b36fd4883ad4fce5e3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8be0e9c371f751b36fd4883ad4fce5e3.map.setCenter( gmap\_m8be0e9c371f751b36fd4883ad4fce5e3.positions[542] );
});