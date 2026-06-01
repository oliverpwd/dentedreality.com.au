---
title: BBQ
date: '2013-05-05T11:21:36+00:00'
format: image
service: flickr
tags:
- bbq
- delicious
- meat
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436924655_275be1f98d_o.jpg?resize=607%2C452
---

[![BBQ](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436924655_275be1f98d_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/05/05/bbq-2/) 
# [BBQ](http://dentedreality.com.au/2013/05/05/bbq-2/)

From Fette Sau





* #[bbq](http://dentedreality.com.au/tags/bbq/)
* #[delicious](http://dentedreality.com.au/tags/delicious-2/)
* #[meat](http://dentedreality.com.au/tags/meat/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9436924655/) [11:21 am, May 5, 2013](http://dentedreality.com.au/2013/05/05/bbq-2/ "11:21 am") 
jQuery(document).ready(function(){
var gmap\_m2b033b079494b9cd8659105407e2cae3 = {
positions : {
323 : new google.maps.LatLng( '40.714166', '-73.9565' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2b033b079494b9cd8659105407e2cae3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2b033b079494b9cd8659105407e2cae3.positions ) {
gmap\_m2b033b079494b9cd8659105407e2cae3.bounds.extend( gmap\_m2b033b079494b9cd8659105407e2cae3.positions[m] );
}
// Render markers
for ( var m in gmap\_m2b033b079494b9cd8659105407e2cae3.positions ) {
gmap\_m2b033b079494b9cd8659105407e2cae3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2b033b079494b9cd8659105407e2cae3.map,
position : gmap\_m2b033b079494b9cd8659105407e2cae3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2b033b079494b9cd8659105407e2cae3.map.setCenter( gmap\_m2b033b079494b9cd8659105407e2cae3.positions[323] );
});