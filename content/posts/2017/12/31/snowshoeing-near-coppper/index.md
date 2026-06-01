---
title: ''
date: '2017-12-31T10:21:31+00:00'
format: image
service: instagram
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/12/26154555_185354808715547_4008062913691516928_n.jpg?fit=640%2C640&ssl=1
---

[![Snowshoeing near Coppper.](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/12/26154555_185354808715547_4008062913691516928_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/12/31/snowshoeing-near-coppper/) 

[![Snowshoeing near Coppper.](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/12/26154555_185354808715547_4008062913691516928_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BdX_NOtBArI/)

Snowshoeing near Coppper.





Posted on [Instagram](https://www.instagram.com/p/BdX_NOtBArI/) [10:21 am, December 31, 2017](https://dentedreality.com.au/2017/12/31/snowshoeing-near-coppper/ "10:21 am") 
jQuery(document).ready(function(){
var gmap\_md704a959ceb96a283e0e1f33210cf25f = {
positions : {
923 : new google.maps.LatLng( '39.500861', '-106.1535167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md704a959ceb96a283e0e1f33210cf25f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md704a959ceb96a283e0e1f33210cf25f.positions ) {
gmap\_md704a959ceb96a283e0e1f33210cf25f.bounds.extend( gmap\_md704a959ceb96a283e0e1f33210cf25f.positions[m] );
}
// Render markers
for ( var m in gmap\_md704a959ceb96a283e0e1f33210cf25f.positions ) {
gmap\_md704a959ceb96a283e0e1f33210cf25f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md704a959ceb96a283e0e1f33210cf25f.map,
position : gmap\_md704a959ceb96a283e0e1f33210cf25f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md704a959ceb96a283e0e1f33210cf25f.map.setCenter( gmap\_md704a959ceb96a283e0e1f33210cf25f.positions[923] );
});