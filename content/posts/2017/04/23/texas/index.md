---
title: ''
date: '2017-04-23T15:39:50-06:00'
format: image
service: instagram
latitude: '29.9844444'
longitude: '-95.3413889'
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/04/18095092_1394092673986228_1838894426785579008_n.jpg?fit=640%2C640
---

[![Texas!](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/04/18095092_1394092673986228_1838894426785579008_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2017/04/23/texas/) 

[![Texas!](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/04/18095092_1394092673986228_1838894426785579008_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BTPkcqRhg2k/)

Texas!

29.9844444-95.3413889




Posted on [Instagram](https://www.instagram.com/p/BTPkcqRhg2k/) [3:39 pm, April 23, 2017](https://dentedreality.com.au/2017/04/23/texas/ "3:39 pm") 
jQuery(document).ready(function(){
var gmap\_m03d94a8bb6bf09129fa50eef60814e3d = {
positions : {
377 : new google.maps.LatLng( '29.984444444444', '-95.341388888889' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m03d94a8bb6bf09129fa50eef60814e3d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m03d94a8bb6bf09129fa50eef60814e3d.positions ) {
gmap\_m03d94a8bb6bf09129fa50eef60814e3d.bounds.extend( gmap\_m03d94a8bb6bf09129fa50eef60814e3d.positions[m] );
}
// Render markers
for ( var m in gmap\_m03d94a8bb6bf09129fa50eef60814e3d.positions ) {
gmap\_m03d94a8bb6bf09129fa50eef60814e3d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m03d94a8bb6bf09129fa50eef60814e3d.map,
position : gmap\_m03d94a8bb6bf09129fa50eef60814e3d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m03d94a8bb6bf09129fa50eef60814e3d.map.setCenter( gmap\_m03d94a8bb6bf09129fa50eef60814e3d.positions[377] );
});