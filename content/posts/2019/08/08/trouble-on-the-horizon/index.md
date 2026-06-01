---
title: ''
date: '2019-08-08T17:47:07-06:00'
format: image
service: instagram
latitude: '38.4547'
longitude: '-107.327'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/08192454/68982464_650057835485847_5867537661822809371_n.jpg?fit=640%2C640&ssl=1
---

[![Trouble on the horizon.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/08192454/68982464_650057835485847_5867537661822809371_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/08/08/trouble-on-the-horizon/) 

[![Trouble on the horizon.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/08192454/68982464_650057835485847_5867537661822809371_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/B07AXScJMYm/)

Trouble on the horizon.

38.4547-107.327




Posted on [Instagram](https://www.instagram.com/p/B07AXScJMYm/) [5:47 pm, August 8, 2019](https://dentedreality.com.au/2019/08/08/trouble-on-the-horizon/ "5:47 pm") 
jQuery(document).ready(function(){
var gmap\_m347ef00f839bdc723179cdcd4a0c762c = {
positions : {
793 : new google.maps.LatLng( '38.4547', '-107.327' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m347ef00f839bdc723179cdcd4a0c762c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m347ef00f839bdc723179cdcd4a0c762c.positions ) {
gmap\_m347ef00f839bdc723179cdcd4a0c762c.bounds.extend( gmap\_m347ef00f839bdc723179cdcd4a0c762c.positions[m] );
}
// Render markers
for ( var m in gmap\_m347ef00f839bdc723179cdcd4a0c762c.positions ) {
gmap\_m347ef00f839bdc723179cdcd4a0c762c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m347ef00f839bdc723179cdcd4a0c762c.map,
position : gmap\_m347ef00f839bdc723179cdcd4a0c762c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m347ef00f839bdc723179cdcd4a0c762c.map.setCenter( gmap\_m347ef00f839bdc723179cdcd4a0c762c.positions[793] );
});