---
title: ''
date: '2017-04-24T21:42:23-06:00'
format: image
service: instagram
tags:
- fish
- platacones
- wholefish
latitude: '9.7177712'
longitude: '-84.6317307'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2017/04/14182612/18160524_1896193897270253_5887218707507183616_n.jpg
---

[![Dinner. #fish #wholefish #platacones](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2017/04/14182612/18160524_1896193897270253_5887218707507183616_n.jpg)](https://dentedreality.com.au/2017/04/24/dinner-fish-wholefish-platacones/) 

[![Dinner. #fish #wholefish #platacones](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2017/04/14182612/18160524_1896193897270253_5887218707507183616_n.jpg)](https://www.instagram.com/p/BTSyu8cBR9b/)

Dinner. #fish #wholefish #platacones

9.7177712-84.6317307




* #[fish](https://dentedreality.com.au/tags/fish/)
* #[platacones](https://dentedreality.com.au/tags/platacones/)
* #[wholefish](https://dentedreality.com.au/tags/wholefish/)

Posted on [Instagram](https://www.instagram.com/p/BTSyu8cBR9b/) [9:42 pm, April 24, 2017](https://dentedreality.com.au/2017/04/24/dinner-fish-wholefish-platacones/ "9:42 pm") 
jQuery(document).ready(function(){
var gmap\_m5b63ac04dc0db349e1d74ece45407f97 = {
positions : {
153 : new google.maps.LatLng( '9.7177711688073', '-84.631730737243' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5b63ac04dc0db349e1d74ece45407f97' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5b63ac04dc0db349e1d74ece45407f97.positions ) {
gmap\_m5b63ac04dc0db349e1d74ece45407f97.bounds.extend( gmap\_m5b63ac04dc0db349e1d74ece45407f97.positions[m] );
}
// Render markers
for ( var m in gmap\_m5b63ac04dc0db349e1d74ece45407f97.positions ) {
gmap\_m5b63ac04dc0db349e1d74ece45407f97.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5b63ac04dc0db349e1d74ece45407f97.map,
position : gmap\_m5b63ac04dc0db349e1d74ece45407f97.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5b63ac04dc0db349e1d74ece45407f97.map.setCenter( gmap\_m5b63ac04dc0db349e1d74ece45407f97.positions[153] );
});