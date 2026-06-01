---
title: Expensive Coaster
date: '2010-04-28T17:56:37+00:00'
format: image
service: flickr
tags:
- coaster
- iphone
- scotch
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4747049850_b3d627b2ee_o.jpg?resize=607%2C455
---

[![Expensive Coaster](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4747049850_b3d627b2ee_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/28/expensive-coaster/) 
# [Expensive Coaster](http://dentedreality.com.au/2010/04/28/expensive-coaster/)

Yes, that’s an iPhone





* #[coaster](http://dentedreality.com.au/tags/coaster/)
* #[iphone](http://dentedreality.com.au/tags/iphone/)
* #[scotch](http://dentedreality.com.au/tags/scotch/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4747049850/) [5:56 pm, April 28, 2010](http://dentedreality.com.au/2010/04/28/expensive-coaster/ "5:56 pm") 
jQuery(document).ready(function(){
var gmap\_mc536747c006f704286131f1454059b47 = {
positions : {
451 : new google.maps.LatLng( '37.785833', '-122.392334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc536747c006f704286131f1454059b47' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc536747c006f704286131f1454059b47.positions ) {
gmap\_mc536747c006f704286131f1454059b47.bounds.extend( gmap\_mc536747c006f704286131f1454059b47.positions[m] );
}
// Render markers
for ( var m in gmap\_mc536747c006f704286131f1454059b47.positions ) {
gmap\_mc536747c006f704286131f1454059b47.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc536747c006f704286131f1454059b47.map,
position : gmap\_mc536747c006f704286131f1454059b47.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc536747c006f704286131f1454059b47.map.setCenter( gmap\_mc536747c006f704286131f1454059b47.positions[451] );
});