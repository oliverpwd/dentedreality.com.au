---
title: Dad and Me
date: '2008-04-08T13:08:01+00:00'
format: image
service: flickr
tags:
- australia
- beau
- beaulebens
- bremerbay
- craig
- dad
- me
- westernaustralia
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2436621667_18e24cc869_o.jpg?resize=607%2C455
---

[![Dad and Me](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2436621667_18e24cc869_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2008/04/08/dad-and-me/) 
# [Dad and Me](http://dentedreality.com.au/2008/04/08/dad-and-me/)

The morning we left from Bremer Bay.





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[bremerbay](http://dentedreality.com.au/tags/bremerbay/)
* #[craig](http://dentedreality.com.au/tags/craig/)
* #[dad](http://dentedreality.com.au/tags/dad/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[westernaustralia](http://dentedreality.com.au/tags/westernaustralia/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2436621667/) [1:08 pm, April 8, 2008](http://dentedreality.com.au/2008/04/08/dad-and-me/ "1:08 pm") 
jQuery(document).ready(function(){
var gmap\_m09db43ffef6d4d7b8623f50aa3cc00be = {
positions : {
627 : new google.maps.LatLng( '-34.397703', '119.387397' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m09db43ffef6d4d7b8623f50aa3cc00be' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m09db43ffef6d4d7b8623f50aa3cc00be.positions ) {
gmap\_m09db43ffef6d4d7b8623f50aa3cc00be.bounds.extend( gmap\_m09db43ffef6d4d7b8623f50aa3cc00be.positions[m] );
}
// Render markers
for ( var m in gmap\_m09db43ffef6d4d7b8623f50aa3cc00be.positions ) {
gmap\_m09db43ffef6d4d7b8623f50aa3cc00be.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m09db43ffef6d4d7b8623f50aa3cc00be.map,
position : gmap\_m09db43ffef6d4d7b8623f50aa3cc00be.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m09db43ffef6d4d7b8623f50aa3cc00be.map.setCenter( gmap\_m09db43ffef6d4d7b8623f50aa3cc00be.positions[627] );
});