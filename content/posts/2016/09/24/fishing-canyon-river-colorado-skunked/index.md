---
title: ''
date: '2016-09-24T14:11:55+00:00'
format: image
service: instagram
tags:
- canyon
- colorado
- fishing
- river
- skunked
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14474358_1759981650910602_7310464861018783744_n.jpg?fit=640%2C640
---

[![#fishing #canyon #river #colorado #skunked](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14474358_1759981650910602_7310464861018783744_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/09/24/fishing-canyon-river-colorado-skunked/) 

#fishing #canyon #river #colorado #skunked





* #[canyon](http://dentedreality.com.au/tags/canyon/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[fishing](http://dentedreality.com.au/tags/fishing/)
* #[river](http://dentedreality.com.au/tags/river/)
* #[skunked](http://dentedreality.com.au/tags/skunked/)

Posted on [Instagram](https://www.instagram.com/p/BKwGqLTjjx6/) [2:11 pm, September 24, 2016](http://dentedreality.com.au/2016/09/24/fishing-canyon-river-colorado-skunked/ "2:11 pm") 
jQuery(document).ready(function(){
var gmap\_m061d2ce63dc770b81c4b88ad421f6295 = {
positions : {
517 : new google.maps.LatLng( '39.753785964028', '-105.23999925811' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m061d2ce63dc770b81c4b88ad421f6295' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m061d2ce63dc770b81c4b88ad421f6295.positions ) {
gmap\_m061d2ce63dc770b81c4b88ad421f6295.bounds.extend( gmap\_m061d2ce63dc770b81c4b88ad421f6295.positions[m] );
}
// Render markers
for ( var m in gmap\_m061d2ce63dc770b81c4b88ad421f6295.positions ) {
gmap\_m061d2ce63dc770b81c4b88ad421f6295.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m061d2ce63dc770b81c4b88ad421f6295.map,
position : gmap\_m061d2ce63dc770b81c4b88ad421f6295.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m061d2ce63dc770b81c4b88ad421f6295.map.setCenter( gmap\_m061d2ce63dc770b81c4b88ad421f6295.positions[517] );
});