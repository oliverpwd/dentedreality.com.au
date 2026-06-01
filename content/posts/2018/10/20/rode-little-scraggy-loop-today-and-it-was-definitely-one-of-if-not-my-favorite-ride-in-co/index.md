---
title: ''
date: '2018-10-20T18:39:49-06:00'
format: image
service: instagram
latitude: '39.3867'
longitude: '-105.27'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/10/14182049/43706243_500807493731348_6840986939405781803_n.jpg?resize=607%2C607&ssl=1
---

[![Rode Little Scraggy Loop today and it was definitely one of, if not my favorite ride in CO.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/10/14182049/43706243_500807493731348_6840986939405781803_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/10/20/rode-little-scraggy-loop-today-and-it-was-definitely-one-of-if-not-my-favorite-ride-in-co/) 

[![Rode Little Scraggy Loop today and it was definitely one of, if not my favorite ride in CO.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/10/14182049/43706243_500807493731348_6840986939405781803_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/BpLORz-F5oN/)

Rode Little Scraggy Loop today and it was definitely one of, if not my favorite ride in CO.

39.3867-105.27




Posted on [Instagram](https://www.instagram.com/p/BpLORz-F5oN/) [6:39 pm, October 20, 2018](https://dentedreality.com.au/2018/10/20/rode-little-scraggy-loop-today-and-it-was-definitely-one-of-if-not-my-favorite-ride-in-co/ "6:39 pm") 
jQuery(document).ready(function(){
var gmap\_m0679642a484232146ad39f4ea75bc02a = {
positions : {
509 : new google.maps.LatLng( '39.3867', '-105.27' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0679642a484232146ad39f4ea75bc02a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0679642a484232146ad39f4ea75bc02a.positions ) {
gmap\_m0679642a484232146ad39f4ea75bc02a.bounds.extend( gmap\_m0679642a484232146ad39f4ea75bc02a.positions[m] );
}
// Render markers
for ( var m in gmap\_m0679642a484232146ad39f4ea75bc02a.positions ) {
gmap\_m0679642a484232146ad39f4ea75bc02a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0679642a484232146ad39f4ea75bc02a.map,
position : gmap\_m0679642a484232146ad39f4ea75bc02a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0679642a484232146ad39f4ea75bc02a.map.setCenter( gmap\_m0679642a484232146ad39f4ea75bc02a.positions[509] );
});