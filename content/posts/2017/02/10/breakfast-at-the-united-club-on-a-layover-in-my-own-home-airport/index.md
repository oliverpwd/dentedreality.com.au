---
title: ''
date: '2017-02-10T09:46:25+00:00'
format: image
service: instagram
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16583410_1817773021806469_2320304971553177600_n.jpg?fit=640%2C640
---

[![Breakfast at the United Club, on a layover in my own home airport.](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/02/16583410_1817773021806469_2320304971553177600_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2017/02/10/breakfast-at-the-united-club-on-a-layover-in-my-own-home-airport/) 

Breakfast at the United Club, on a layover in my own home airport.





Posted on [Instagram](https://www.instagram.com/p/BQVpopdjfq7/) [9:46 am, February 10, 2017](http://dentedreality.com.au/2017/02/10/breakfast-at-the-united-club-on-a-layover-in-my-own-home-airport/ "9:46 am") 
jQuery(document).ready(function(){
var gmap\_m237d47208ba4fd11862df73d49c57ec9 = {
positions : {
44 : new google.maps.LatLng( '39.859107020826', '-104.67350164725' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m237d47208ba4fd11862df73d49c57ec9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m237d47208ba4fd11862df73d49c57ec9.positions ) {
gmap\_m237d47208ba4fd11862df73d49c57ec9.bounds.extend( gmap\_m237d47208ba4fd11862df73d49c57ec9.positions[m] );
}
// Render markers
for ( var m in gmap\_m237d47208ba4fd11862df73d49c57ec9.positions ) {
gmap\_m237d47208ba4fd11862df73d49c57ec9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m237d47208ba4fd11862df73d49c57ec9.map,
position : gmap\_m237d47208ba4fd11862df73d49c57ec9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m237d47208ba4fd11862df73d49c57ec9.map.setCenter( gmap\_m237d47208ba4fd11862df73d49c57ec9.positions[44] );
});