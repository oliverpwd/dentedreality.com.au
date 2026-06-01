---
title: Grand Central
date: '2011-02-25T21:01:09+00:00'
format: image
service: flickr
tags:
- grandcentral
- newyork
- newyorkcity
- NYC
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802618716_7da17b1c0e_o.jpg?resize=607%2C452
---

[![Grand Central](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802618716_7da17b1c0e_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/02/25/grand-central/) 
# [Grand Central](http://dentedreality.com.au/2011/02/25/grand-central/)





* #[grandcentral](http://dentedreality.com.au/tags/grandcentral/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[newyorkcity](http://dentedreality.com.au/tags/newyorkcity/)
* #[NYC](http://dentedreality.com.au/tags/nyc/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802618716/) [9:01 pm, February 25, 2011](http://dentedreality.com.au/2011/02/25/grand-central/ "9:01 pm") 
jQuery(document).ready(function(){
var gmap\_m19b3b03319e869ed6c6509a6876ccc6f = {
positions : {
294 : new google.maps.LatLng( '40.752666', '-73.9775' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m19b3b03319e869ed6c6509a6876ccc6f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m19b3b03319e869ed6c6509a6876ccc6f.positions ) {
gmap\_m19b3b03319e869ed6c6509a6876ccc6f.bounds.extend( gmap\_m19b3b03319e869ed6c6509a6876ccc6f.positions[m] );
}
// Render markers
for ( var m in gmap\_m19b3b03319e869ed6c6509a6876ccc6f.positions ) {
gmap\_m19b3b03319e869ed6c6509a6876ccc6f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m19b3b03319e869ed6c6509a6876ccc6f.map,
position : gmap\_m19b3b03319e869ed6c6509a6876ccc6f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m19b3b03319e869ed6c6509a6876ccc6f.map.setCenter( gmap\_m19b3b03319e869ed6c6509a6876ccc6f.positions[294] );
});