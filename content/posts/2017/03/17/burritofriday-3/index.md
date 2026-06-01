---
title: ''
date: '2017-03-17T14:08:08-07:00'
format: image
service: instagram
tags:
- burritofriday
latitude: '39.7401244'
longitude: '-104.963292'
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/03/17332658_1835558530032147_3082453579722653696_n.jpg?fit=640%2C640&ssl=1
---

[![#burritofriday](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/03/17332658_1835558530032147_3082453579722653696_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/03/17/burritofriday-3/) 

[![#burritofriday](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/03/17332658_1835558530032147_3082453579722653696_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BRwIiuVhT8H/)

#burritofriday

39.7401244-104.963292




* #[burritofriday](https://dentedreality.com.au/tags/burritofriday/)

Posted on [Instagram](https://www.instagram.com/p/BRwIiuVhT8H/) [2:08 pm, March 17, 2017](https://dentedreality.com.au/2017/03/17/burritofriday-3/ "2:08 pm") 
jQuery(document).ready(function(){
var gmap\_mc4e0573bd447bd7597143c62f63c5e45 = {
positions : {
285 : new google.maps.LatLng( '39.740124419831', '-104.96329197258' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc4e0573bd447bd7597143c62f63c5e45' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc4e0573bd447bd7597143c62f63c5e45.positions ) {
gmap\_mc4e0573bd447bd7597143c62f63c5e45.bounds.extend( gmap\_mc4e0573bd447bd7597143c62f63c5e45.positions[m] );
}
// Render markers
for ( var m in gmap\_mc4e0573bd447bd7597143c62f63c5e45.positions ) {
gmap\_mc4e0573bd447bd7597143c62f63c5e45.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc4e0573bd447bd7597143c62f63c5e45.map,
position : gmap\_mc4e0573bd447bd7597143c62f63c5e45.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc4e0573bd447bd7597143c62f63c5e45.map.setCenter( gmap\_mc4e0573bd447bd7597143c62f63c5e45.positions[285] );
});