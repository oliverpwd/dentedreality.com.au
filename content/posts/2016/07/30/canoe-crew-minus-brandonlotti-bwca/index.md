---
title: ''
date: '2016-07-30T09:55:38-06:00'
format: image
service: instagram
tags:
- bwca
latitude: '47.9637014'
longitude: '-91.5469748'
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13732266_139223616514127_1055630610_n.jpg?fit=640%2C640
---

[![Canoe crew (minus @brandonlotti) #bwca](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13732266_139223616514127_1055630610_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/07/30/canoe-crew-minus-brandonlotti-bwca/) 

[![Canoe crew (minus @brandonlotti) #bwca](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13732266_139223616514127_1055630610_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BIfc0IGAvIF/)

Canoe crew (minus @brandonlotti) #bwca

47.9637014-91.5469748




* #[bwca](https://dentedreality.com.au/tags/bwca/)

Posted on [Instagram](https://www.instagram.com/p/BIfc0IGAvIF/) [9:55 am, July 30, 2016](https://dentedreality.com.au/2016/07/30/canoe-crew-minus-brandonlotti-bwca/ "9:55 am") 
jQuery(document).ready(function(){
var gmap\_m4702c2c64dc69e0a9340661c4de314ad = {
positions : {
221 : new google.maps.LatLng( '47.963701444723', '-91.546974778261' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4702c2c64dc69e0a9340661c4de314ad' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4702c2c64dc69e0a9340661c4de314ad.positions ) {
gmap\_m4702c2c64dc69e0a9340661c4de314ad.bounds.extend( gmap\_m4702c2c64dc69e0a9340661c4de314ad.positions[m] );
}
// Render markers
for ( var m in gmap\_m4702c2c64dc69e0a9340661c4de314ad.positions ) {
gmap\_m4702c2c64dc69e0a9340661c4de314ad.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4702c2c64dc69e0a9340661c4de314ad.map,
position : gmap\_m4702c2c64dc69e0a9340661c4de314ad.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4702c2c64dc69e0a9340661c4de314ad.map.setCenter( gmap\_m4702c2c64dc69e0a9340661c4de314ad.positions[221] );
});