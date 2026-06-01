---
title: Harriman State Park
date: '2013-08-31T10:34:14+00:00'
format: image
tags:
- backpacking
- harriman
- harrimanstatepark
- hiking
- newyork
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767907895_37e0e2f2e4_o.jpg?resize=607%2C452
---

[![Harriman State Park](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767907895_37e0e2f2e4_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/08/31/harriman-state-park-4/) 
# [Harriman State Park](http://dentedreality.com.au/2013/08/31/harriman-state-park-4/)

Tom Jones Shelter





* #[backpacking](http://dentedreality.com.au/tags/backpacking/)
* #[harriman](http://dentedreality.com.au/tags/harriman/)
* #[harrimanstatepark](http://dentedreality.com.au/tags/harrimanstatepark/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9767907895/) [10:34 am, August 31, 2013](http://dentedreality.com.au/2013/08/31/harriman-state-park-4/ "10:34 am") 
jQuery(document).ready(function(){
var gmap\_m88ca031380edf2abb0056de6aa8c4503 = {
positions : {
500 : new google.maps.LatLng( '41.224666', '-74.142001' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m88ca031380edf2abb0056de6aa8c4503' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m88ca031380edf2abb0056de6aa8c4503.positions ) {
gmap\_m88ca031380edf2abb0056de6aa8c4503.bounds.extend( gmap\_m88ca031380edf2abb0056de6aa8c4503.positions[m] );
}
// Render markers
for ( var m in gmap\_m88ca031380edf2abb0056de6aa8c4503.positions ) {
gmap\_m88ca031380edf2abb0056de6aa8c4503.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m88ca031380edf2abb0056de6aa8c4503.map,
position : gmap\_m88ca031380edf2abb0056de6aa8c4503.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m88ca031380edf2abb0056de6aa8c4503.map.setCenter( gmap\_m88ca031380edf2abb0056de6aa8c4503.positions[500] );
});