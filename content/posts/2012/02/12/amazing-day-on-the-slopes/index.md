---
title: Amazing Day on the Slopes
date: '2012-02-12T10:15:40+00:00'
format: image
service: flickr
tags:
- mountain
- skiing
- snow
- snowboarding
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959571817_0cd873c000_o.jpg?resize=607%2C452
---

[![Amazing Day on the Slopes](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959571817_0cd873c000_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/02/12/amazing-day-on-the-slopes/) 
# [Amazing Day on the Slopes](http://dentedreality.com.au/2012/02/12/amazing-day-on-the-slopes/)





* #[mountain](http://dentedreality.com.au/tags/mountain/)
* #[skiing](http://dentedreality.com.au/tags/skiing/)
* #[snow](http://dentedreality.com.au/tags/snow/)
* #[snowboarding](http://dentedreality.com.au/tags/snowboarding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959571817/) [10:15 am, February 12, 2012](http://dentedreality.com.au/2012/02/12/amazing-day-on-the-slopes/ "10:15 am") 
jQuery(document).ready(function(){
var gmap\_m7b81db75565b484bb28b8f9b3c892dae = {
positions : {
904 : new google.maps.LatLng( '38.952166', '-119.949334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7b81db75565b484bb28b8f9b3c892dae' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7b81db75565b484bb28b8f9b3c892dae.positions ) {
gmap\_m7b81db75565b484bb28b8f9b3c892dae.bounds.extend( gmap\_m7b81db75565b484bb28b8f9b3c892dae.positions[m] );
}
// Render markers
for ( var m in gmap\_m7b81db75565b484bb28b8f9b3c892dae.positions ) {
gmap\_m7b81db75565b484bb28b8f9b3c892dae.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7b81db75565b484bb28b8f9b3c892dae.map,
position : gmap\_m7b81db75565b484bb28b8f9b3c892dae.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7b81db75565b484bb28b8f9b3c892dae.map.setCenter( gmap\_m7b81db75565b484bb28b8f9b3c892dae.positions[904] );
});