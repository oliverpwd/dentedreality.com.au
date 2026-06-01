---
title: Ermagherd Burzse Crurze with COED.com
date: '2012-08-16T18:01:27+00:00'
format: image
service: flickr
tags:
- boozecruise
- cityscape
- coed
- EastRiver
- newyork
- skyline
---

[![Ermagherd Burzse Crurze with COED.com](http://i2.wp.com/farm9.staticflickr.com/8209/8244767653_7aaab225a8_o.jpg?w=607)](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-2/) 
# [Ermagherd Burzse Crurze with COED.com](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-2/)





* #[boozecruise](http://dentedreality.com.au/tags/boozecruise/)
* #[cityscape](http://dentedreality.com.au/tags/cityscape/)
* #[coed](http://dentedreality.com.au/tags/coed/)
* #[EastRiver](http://dentedreality.com.au/tags/eastriver/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[skyline](http://dentedreality.com.au/tags/skyline/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8244767653/) [6:01 pm, August 16, 2012](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-2/ "6:01 pm") 
jQuery(document).ready(function(){
var gmap\_m452c1b3e728d65cd9345f67c74007ee6 = {
positions : {
341 : new google.maps.LatLng( '40.751', '-73.9565' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m452c1b3e728d65cd9345f67c74007ee6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m452c1b3e728d65cd9345f67c74007ee6.positions ) {
gmap\_m452c1b3e728d65cd9345f67c74007ee6.bounds.extend( gmap\_m452c1b3e728d65cd9345f67c74007ee6.positions[m] );
}
// Render markers
for ( var m in gmap\_m452c1b3e728d65cd9345f67c74007ee6.positions ) {
gmap\_m452c1b3e728d65cd9345f67c74007ee6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m452c1b3e728d65cd9345f67c74007ee6.map,
position : gmap\_m452c1b3e728d65cd9345f67c74007ee6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m452c1b3e728d65cd9345f67c74007ee6.map.setCenter( gmap\_m452c1b3e728d65cd9345f67c74007ee6.positions[341] );
});