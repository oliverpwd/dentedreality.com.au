---
title: ''
date: '2016-07-30T10:01:57-06:00'
format: image
service: instagram
tags:
- bwca
latitude: '47.9637014'
longitude: '-91.5469748'
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13704197_1641062296207858_560320903_n.jpg?fit=640%2C640
---

[![Rapids/waterfall #bwca](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13704197_1641062296207858_560320903_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/07/30/rapidswaterfall-bwca/) 

[![Rapids/waterfall #bwca](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13704197_1641062296207858_560320903_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BIfdiZFgmu1/)

Rapids/waterfall #bwca

47.9637014-91.5469748




* #[bwca](https://dentedreality.com.au/tags/bwca/)

Posted on [Instagram](https://www.instagram.com/p/BIfdiZFgmu1/) [10:01 am, July 30, 2016](https://dentedreality.com.au/2016/07/30/rapidswaterfall-bwca/ "10:01 am") 
jQuery(document).ready(function(){
var gmap\_m17ffbdf753986a0f3cc025dd695a4dd2 = {
positions : {
699 : new google.maps.LatLng( '47.963701444723', '-91.546974778261' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m17ffbdf753986a0f3cc025dd695a4dd2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m17ffbdf753986a0f3cc025dd695a4dd2.positions ) {
gmap\_m17ffbdf753986a0f3cc025dd695a4dd2.bounds.extend( gmap\_m17ffbdf753986a0f3cc025dd695a4dd2.positions[m] );
}
// Render markers
for ( var m in gmap\_m17ffbdf753986a0f3cc025dd695a4dd2.positions ) {
gmap\_m17ffbdf753986a0f3cc025dd695a4dd2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m17ffbdf753986a0f3cc025dd695a4dd2.map,
position : gmap\_m17ffbdf753986a0f3cc025dd695a4dd2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m17ffbdf753986a0f3cc025dd695a4dd2.map.setCenter( gmap\_m17ffbdf753986a0f3cc025dd695a4dd2.positions[699] );
});