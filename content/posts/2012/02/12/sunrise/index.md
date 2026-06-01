---
title: Sunrise
date: '2012-02-12T03:07:15+00:00'
format: image
service: flickr
tags:
- powerline
- sunrise
- tahoe
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813459206_fd32670c9f_o.jpg?resize=607%2C452
---

[![Sunrise](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813459206_fd32670c9f_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/02/12/sunrise/) 
# [Sunrise](http://dentedreality.com.au/2012/02/12/sunrise/)

We had to leave \*very\* early to get to Tahoe for a day trip





* #[powerline](http://dentedreality.com.au/tags/powerline/)
* #[sunrise](http://dentedreality.com.au/tags/sunrise/)
* #[tahoe](http://dentedreality.com.au/tags/tahoe/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813459206/) [3:07 am, February 12, 2012](http://dentedreality.com.au/2012/02/12/sunrise/ "3:07 am") 
jQuery(document).ready(function(){
var gmap\_m5eb5d9cbaea3e1b95d2101431d5f74a4 = {
positions : {
537 : new google.maps.LatLng( '38.400333', '-121.918' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5eb5d9cbaea3e1b95d2101431d5f74a4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5eb5d9cbaea3e1b95d2101431d5f74a4.positions ) {
gmap\_m5eb5d9cbaea3e1b95d2101431d5f74a4.bounds.extend( gmap\_m5eb5d9cbaea3e1b95d2101431d5f74a4.positions[m] );
}
// Render markers
for ( var m in gmap\_m5eb5d9cbaea3e1b95d2101431d5f74a4.positions ) {
gmap\_m5eb5d9cbaea3e1b95d2101431d5f74a4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5eb5d9cbaea3e1b95d2101431d5f74a4.map,
position : gmap\_m5eb5d9cbaea3e1b95d2101431d5f74a4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5eb5d9cbaea3e1b95d2101431d5f74a4.map.setCenter( gmap\_m5eb5d9cbaea3e1b95d2101431d5f74a4.positions[537] );
});