---
title: ''
date: '2019-08-11T15:09:20-06:00'
format: image
service: instagram
latitude: '39.7391'
longitude: '-104.9836'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/11152456/61755107_1433450550164357_1804625735414920028_n.jpg?fit=640%2C640&ssl=1
---

[![Got carried away and now we have unlimited free power FROM THE SKY. Thanks @goalzero](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/11152456/61755107_1433450550164357_1804625735414920028_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/08/11/got-carried-away-and-now-we-have-unlimited-free-power-from-the-sky-thanks-goalzero/) 

[![Got carried away and now we have unlimited free power FROM THE SKY. Thanks @goalzero](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/11152456/61755107_1433450550164357_1804625735414920028_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/B1CcsTaJUb_/)

Got carried away and now we have unlimited free power FROM THE SKY. Thanks @goalzero

39.7391-104.9836




Posted on [Instagram](https://www.instagram.com/p/B1CcsTaJUb_/) [3:09 pm, August 11, 2019](https://dentedreality.com.au/2019/08/11/got-carried-away-and-now-we-have-unlimited-free-power-from-the-sky-thanks-goalzero/ "3:09 pm") 
jQuery(document).ready(function(){
var gmap\_m3c7472e64f0abfaf8b0cddd8927f6623 = {
positions : {
565 : new google.maps.LatLng( '39.7391', '-104.9836' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3c7472e64f0abfaf8b0cddd8927f6623' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3c7472e64f0abfaf8b0cddd8927f6623.positions ) {
gmap\_m3c7472e64f0abfaf8b0cddd8927f6623.bounds.extend( gmap\_m3c7472e64f0abfaf8b0cddd8927f6623.positions[m] );
}
// Render markers
for ( var m in gmap\_m3c7472e64f0abfaf8b0cddd8927f6623.positions ) {
gmap\_m3c7472e64f0abfaf8b0cddd8927f6623.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3c7472e64f0abfaf8b0cddd8927f6623.map,
position : gmap\_m3c7472e64f0abfaf8b0cddd8927f6623.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3c7472e64f0abfaf8b0cddd8927f6623.map.setCenter( gmap\_m3c7472e64f0abfaf8b0cddd8927f6623.positions[565] );
});