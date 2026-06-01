---
title: Surfboard Bench
date: '2014-03-20T05:32:59+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- me
- mooloolaba
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927850445_e59ca60ef7_o.jpg?resize=607%2C455
---

[![Surfboard Bench](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927850445_e59ca60ef7_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/20/surfboard-bench/) 
# [Surfboard Bench](http://dentedreality.com.au/2014/03/20/surfboard-bench/)

Perth, Mooloolaba and Melbourne





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[mooloolaba](http://dentedreality.com.au/tags/mooloolaba/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927850445/) [5:32 am, March 20, 2014](http://dentedreality.com.au/2014/03/20/surfboard-bench/ "5:32 am") 
jQuery(document).ready(function(){
var gmap\_m61adfd24c2fffbc523dc27e7d18c34ef = {
positions : {
249 : new google.maps.LatLng( '-26.680364', '153.120558' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m61adfd24c2fffbc523dc27e7d18c34ef' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m61adfd24c2fffbc523dc27e7d18c34ef.positions ) {
gmap\_m61adfd24c2fffbc523dc27e7d18c34ef.bounds.extend( gmap\_m61adfd24c2fffbc523dc27e7d18c34ef.positions[m] );
}
// Render markers
for ( var m in gmap\_m61adfd24c2fffbc523dc27e7d18c34ef.positions ) {
gmap\_m61adfd24c2fffbc523dc27e7d18c34ef.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m61adfd24c2fffbc523dc27e7d18c34ef.map,
position : gmap\_m61adfd24c2fffbc523dc27e7d18c34ef.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m61adfd24c2fffbc523dc27e7d18c34ef.map.setCenter( gmap\_m61adfd24c2fffbc523dc27e7d18c34ef.positions[249] );
});