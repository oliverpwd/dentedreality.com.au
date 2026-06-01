---
title: New York
date: '2011-07-23T20:25:23+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- me
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6322934645_e6656f6b33_o.jpg?resize=607%2C453
---

[![New York](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6322934645_e6656f6b33_o.jpg?resize=607%2C453)](http://dentedreality.com.au/2011/07/23/new-york-14/) 
# [New York](http://dentedreality.com.au/2011/07/23/new-york-14/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6322934645/) [8:25 pm, July 23, 2011](http://dentedreality.com.au/2011/07/23/new-york-14/ "8:25 pm") 
jQuery(document).ready(function(){
var gmap\_m4f05a1d4972da98b20460dc399e38ed2 = {
positions : {
315 : new google.maps.LatLng( '40.727833', '-73.979334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4f05a1d4972da98b20460dc399e38ed2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4f05a1d4972da98b20460dc399e38ed2.positions ) {
gmap\_m4f05a1d4972da98b20460dc399e38ed2.bounds.extend( gmap\_m4f05a1d4972da98b20460dc399e38ed2.positions[m] );
}
// Render markers
for ( var m in gmap\_m4f05a1d4972da98b20460dc399e38ed2.positions ) {
gmap\_m4f05a1d4972da98b20460dc399e38ed2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4f05a1d4972da98b20460dc399e38ed2.map,
position : gmap\_m4f05a1d4972da98b20460dc399e38ed2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4f05a1d4972da98b20460dc399e38ed2.map.setCenter( gmap\_m4f05a1d4972da98b20460dc399e38ed2.positions[315] );
});