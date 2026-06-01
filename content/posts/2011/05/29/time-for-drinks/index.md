---
title: Time for Drinks!
date: '2011-05-29T13:34:41+00:00'
format: image
service: flickr
tags:
- kara
- owenswedding
- renee
- wedding
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803432454_862f19315a_o.jpg?resize=607%2C813
---

[![Time for Drinks!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803432454_862f19315a_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/29/time-for-drinks/) 
# [Time for Drinks!](http://dentedreality.com.au/2011/05/29/time-for-drinks/)





* #[kara](http://dentedreality.com.au/tags/kara/)
* #[owenswedding](http://dentedreality.com.au/tags/owenswedding/)
* #[renee](http://dentedreality.com.au/tags/renee/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5803432454/) [1:34 pm, May 29, 2011](http://dentedreality.com.au/2011/05/29/time-for-drinks/ "1:34 pm") 
jQuery(document).ready(function(){
var gmap\_mfd51a407d1e6dae274c2650565e51ba3 = {
positions : {
643 : new google.maps.LatLng( '37.776333', '-122.393667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mfd51a407d1e6dae274c2650565e51ba3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mfd51a407d1e6dae274c2650565e51ba3.positions ) {
gmap\_mfd51a407d1e6dae274c2650565e51ba3.bounds.extend( gmap\_mfd51a407d1e6dae274c2650565e51ba3.positions[m] );
}
// Render markers
for ( var m in gmap\_mfd51a407d1e6dae274c2650565e51ba3.positions ) {
gmap\_mfd51a407d1e6dae274c2650565e51ba3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mfd51a407d1e6dae274c2650565e51ba3.map,
position : gmap\_mfd51a407d1e6dae274c2650565e51ba3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mfd51a407d1e6dae274c2650565e51ba3.map.setCenter( gmap\_mfd51a407d1e6dae274c2650565e51ba3.positions[643] );
});