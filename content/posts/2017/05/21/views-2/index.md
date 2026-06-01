---
title: ''
date: '2017-05-21T18:07:13+00:00'
format: image
service: instagram
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18579894_1209466739162813_5703694548790673408_n.jpg?fit=640%2C640&ssl=1
---

[![Views.](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18579894_1209466739162813_5703694548790673408_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/05/21/views-2/) 

Views.





Posted on [Instagram](https://www.instagram.com/p/BUX7kqIBQzj/) [6:07 pm, May 21, 2017](https://dentedreality.com.au/2017/05/21/views-2/ "6:07 pm") 
jQuery(document).ready(function(){
var gmap\_medb866a6380fea66db444e5292de5609 = {
positions : {
108 : new google.maps.LatLng( '39.7683409616', '-105.215712653' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_medb866a6380fea66db444e5292de5609' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_medb866a6380fea66db444e5292de5609.positions ) {
gmap\_medb866a6380fea66db444e5292de5609.bounds.extend( gmap\_medb866a6380fea66db444e5292de5609.positions[m] );
}
// Render markers
for ( var m in gmap\_medb866a6380fea66db444e5292de5609.positions ) {
gmap\_medb866a6380fea66db444e5292de5609.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_medb866a6380fea66db444e5292de5609.map,
position : gmap\_medb866a6380fea66db444e5292de5609.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_medb866a6380fea66db444e5292de5609.map.setCenter( gmap\_medb866a6380fea66db444e5292de5609.positions[108] );
});