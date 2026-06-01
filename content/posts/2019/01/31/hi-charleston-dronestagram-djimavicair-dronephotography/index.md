---
title: ''
date: '2019-01-31T19:24:06-06:00'
format: image
service: instagram
tags:
- djimavicair
- dronephotography
- dronestagram
latitude: '32.81253'
longitude: '-79.95128'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/01/14181943/51114405_602979840141289_7374364844354268624_n.jpg?resize=607%2C343&ssl=1
---

[![Hi Charleston! #dronestagram #djimavicair #dronephotography](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/01/14181943/51114405_602979840141289_7374364844354268624_n.jpg?resize=607%2C343&ssl=1)](https://dentedreality.com.au/2019/01/31/hi-charleston-dronestagram-djimavicair-dronephotography/) 

[![Hi Charleston! #dronestagram #djimavicair #dronephotography](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/01/14181943/51114405_602979840141289_7374364844354268624_n.jpg?resize=607%2C343&ssl=1)](https://www.instagram.com/p/BtUoFyAHlhR/)

Hi Charleston! #dronestagram #djimavicair #dronephotography

32.81253-79.95128




* #[djimavicair](https://dentedreality.com.au/tags/djimavicair/)
* #[dronephotography](https://dentedreality.com.au/tags/dronephotography/)
* #[dronestagram](https://dentedreality.com.au/tags/dronestagram/)

Posted on [Instagram](https://www.instagram.com/p/BtUoFyAHlhR/) [7:24 pm, January 31, 2019](https://dentedreality.com.au/2019/01/31/hi-charleston-dronestagram-djimavicair-dronephotography/ "7:24 pm") 
jQuery(document).ready(function(){
var gmap\_m5e0b837b51b5dd401eb684ee0bfc0e85 = {
positions : {
882 : new google.maps.LatLng( '32.81253', '-79.95128' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5e0b837b51b5dd401eb684ee0bfc0e85' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5e0b837b51b5dd401eb684ee0bfc0e85.positions ) {
gmap\_m5e0b837b51b5dd401eb684ee0bfc0e85.bounds.extend( gmap\_m5e0b837b51b5dd401eb684ee0bfc0e85.positions[m] );
}
// Render markers
for ( var m in gmap\_m5e0b837b51b5dd401eb684ee0bfc0e85.positions ) {
gmap\_m5e0b837b51b5dd401eb684ee0bfc0e85.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5e0b837b51b5dd401eb684ee0bfc0e85.map,
position : gmap\_m5e0b837b51b5dd401eb684ee0bfc0e85.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5e0b837b51b5dd401eb684ee0bfc0e85.map.setCenter( gmap\_m5e0b837b51b5dd401eb684ee0bfc0e85.positions[882] );
});