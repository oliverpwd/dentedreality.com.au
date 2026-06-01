---
title: ''
date: '2017-08-13T15:54:56-06:00'
format: image
service: instagram
latitude: '39.8358205'
longitude: '-105.678059'
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/08/20759738_887671834734195_4929668191384240128_n.jpg?fit=640%2C640&ssl=1
---

[![Afternoon beers after a rough 4wd in, plus rain while setting up camp. Birthday weekend for @akires](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/08/20759738_887671834734195_4929668191384240128_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/08/13/afternoon-beers-after-a-rough-4wd-in-plus-rain-while-setting-up-camp-birthday-weekend-for-akires/) 

[![Afternoon beers after a rough 4wd in, plus rain while setting up camp. Birthday weekend for @akires](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/08/20759738_887671834734195_4929668191384240128_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BXv_NSJBnaE/)

Afternoon beers after a rough 4wd in, plus rain while setting up camp. Birthday weekend for @akires

39.8358205-105.678059




Posted on [Instagram](https://www.instagram.com/p/BXv_NSJBnaE/) [3:54 pm, August 13, 2017](https://dentedreality.com.au/2017/08/13/afternoon-beers-after-a-rough-4wd-in-plus-rain-while-setting-up-camp-birthday-weekend-for-akires/ "3:54 pm") 
jQuery(document).ready(function(){
var gmap\_mb7f7cb13cc27277a72ca4a710c01d67c = {
positions : {
453 : new google.maps.LatLng( '39.8358205', '-105.678059' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb7f7cb13cc27277a72ca4a710c01d67c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb7f7cb13cc27277a72ca4a710c01d67c.positions ) {
gmap\_mb7f7cb13cc27277a72ca4a710c01d67c.bounds.extend( gmap\_mb7f7cb13cc27277a72ca4a710c01d67c.positions[m] );
}
// Render markers
for ( var m in gmap\_mb7f7cb13cc27277a72ca4a710c01d67c.positions ) {
gmap\_mb7f7cb13cc27277a72ca4a710c01d67c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb7f7cb13cc27277a72ca4a710c01d67c.map,
position : gmap\_mb7f7cb13cc27277a72ca4a710c01d67c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb7f7cb13cc27277a72ca4a710c01d67c.map.setCenter( gmap\_mb7f7cb13cc27277a72ca4a710c01d67c.positions[453] );
});