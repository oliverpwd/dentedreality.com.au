---
title: Tea Pot/Cup
date: '2010-01-06T13:22:05+00:00'
format: image
service: flickr
tags:
- Chile
- Santiago
- teacup
- teapot
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/01/4269473482_4727026366_o.jpg?resize=607%2C455
---

[![Tea Pot/Cup](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/01/4269473482_4727026366_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/01/06/tea-potcup/) 
# [Tea Pot/Cup](http://dentedreality.com.au/2010/01/06/tea-potcup/)





* #[Chile](http://dentedreality.com.au/tags/chile/)
* #[Santiago](http://dentedreality.com.au/tags/santiago/)
* #[teacup](http://dentedreality.com.au/tags/teacup/)
* #[teapot](http://dentedreality.com.au/tags/teapot/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4269473482/) [1:22 pm, January 6, 2010](http://dentedreality.com.au/2010/01/06/tea-potcup/ "1:22 pm") 
jQuery(document).ready(function(){
var gmap\_mf4ffb9a11666fcf12554dad16e502331 = {
positions : {
794 : new google.maps.LatLng( '-33.423334', '-70.6165' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf4ffb9a11666fcf12554dad16e502331' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf4ffb9a11666fcf12554dad16e502331.positions ) {
gmap\_mf4ffb9a11666fcf12554dad16e502331.bounds.extend( gmap\_mf4ffb9a11666fcf12554dad16e502331.positions[m] );
}
// Render markers
for ( var m in gmap\_mf4ffb9a11666fcf12554dad16e502331.positions ) {
gmap\_mf4ffb9a11666fcf12554dad16e502331.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf4ffb9a11666fcf12554dad16e502331.map,
position : gmap\_mf4ffb9a11666fcf12554dad16e502331.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf4ffb9a11666fcf12554dad16e502331.map.setCenter( gmap\_mf4ffb9a11666fcf12554dad16e502331.positions[794] );
});