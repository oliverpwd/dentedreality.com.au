---
title: Epic Australian Adventure, 2014
date: '2014-03-20T09:25:13+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- me
- mooloolaba
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927898723_43d41145d0_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927898723_43d41145d0_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/20/epic-australian-adventure-2014-13/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/20/epic-australian-adventure-2014-13/)

Perth, Mooloolaba and Melbourne





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[mooloolaba](http://dentedreality.com.au/tags/mooloolaba/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927898723/) [9:25 am, March 20, 2014](http://dentedreality.com.au/2014/03/20/epic-australian-adventure-2014-13/ "9:25 am") 
jQuery(document).ready(function(){
var gmap\_meee224bd0627a2137518ecc2a1171d0e = {
positions : {
646 : new google.maps.LatLng( '-26.736914', '153.063111' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_meee224bd0627a2137518ecc2a1171d0e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_meee224bd0627a2137518ecc2a1171d0e.positions ) {
gmap\_meee224bd0627a2137518ecc2a1171d0e.bounds.extend( gmap\_meee224bd0627a2137518ecc2a1171d0e.positions[m] );
}
// Render markers
for ( var m in gmap\_meee224bd0627a2137518ecc2a1171d0e.positions ) {
gmap\_meee224bd0627a2137518ecc2a1171d0e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_meee224bd0627a2137518ecc2a1171d0e.map,
position : gmap\_meee224bd0627a2137518ecc2a1171d0e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_meee224bd0627a2137518ecc2a1171d0e.map.setCenter( gmap\_meee224bd0627a2137518ecc2a1171d0e.positions[646] );
});