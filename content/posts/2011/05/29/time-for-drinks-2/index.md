---
title: Time for Drinks!
date: '2011-05-29T13:32:43+00:00'
format: image
service: flickr
tags:
- owenswedding
- renee
- wedding
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802875267_2ed76c397b_o.jpg?resize=607%2C813
---

[![Time for Drinks!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802875267_2ed76c397b_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/29/time-for-drinks-2/) 
# [Time for Drinks!](http://dentedreality.com.au/2011/05/29/time-for-drinks-2/)





* #[owenswedding](http://dentedreality.com.au/tags/owenswedding/)
* #[renee](http://dentedreality.com.au/tags/renee/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802875267/) [1:32 pm, May 29, 2011](http://dentedreality.com.au/2011/05/29/time-for-drinks-2/ "1:32 pm") 
jQuery(document).ready(function(){
var gmap\_mdb478a47a2654e2aa19e82b276400a7d = {
positions : {
127 : new google.maps.LatLng( '37.776166', '-122.3935' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdb478a47a2654e2aa19e82b276400a7d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdb478a47a2654e2aa19e82b276400a7d.positions ) {
gmap\_mdb478a47a2654e2aa19e82b276400a7d.bounds.extend( gmap\_mdb478a47a2654e2aa19e82b276400a7d.positions[m] );
}
// Render markers
for ( var m in gmap\_mdb478a47a2654e2aa19e82b276400a7d.positions ) {
gmap\_mdb478a47a2654e2aa19e82b276400a7d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdb478a47a2654e2aa19e82b276400a7d.map,
position : gmap\_mdb478a47a2654e2aa19e82b276400a7d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdb478a47a2654e2aa19e82b276400a7d.map.setCenter( gmap\_mdb478a47a2654e2aa19e82b276400a7d.positions[127] );
});