---
title: Ermagherd Burzse Crurze with COED.com
date: '2012-08-16T17:21:03+00:00'
format: image
service: flickr
tags:
- boozecruise
- coed
- EastRiver
- erika
- newyork
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8245835274_3a8562ed0e_o.jpg?resize=607%2C813
---

[![Ermagherd Burzse Crurze with COED.com](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8245835274_3a8562ed0e_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-4/) 
# [Ermagherd Burzse Crurze with COED.com](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-4/)

Stylin’ glasses





* #[boozecruise](http://dentedreality.com.au/tags/boozecruise/)
* #[coed](http://dentedreality.com.au/tags/coed/)
* #[EastRiver](http://dentedreality.com.au/tags/eastriver/)
* #[erika](http://dentedreality.com.au/tags/erika/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245835274/) [5:21 pm, August 16, 2012](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-4/ "5:21 pm") 
jQuery(document).ready(function(){
var gmap\_m7bef71eb92c02c79eee2edcafcfe9784 = {
positions : {
707 : new google.maps.LatLng( '40.703666', '-74.001667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7bef71eb92c02c79eee2edcafcfe9784' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7bef71eb92c02c79eee2edcafcfe9784.positions ) {
gmap\_m7bef71eb92c02c79eee2edcafcfe9784.bounds.extend( gmap\_m7bef71eb92c02c79eee2edcafcfe9784.positions[m] );
}
// Render markers
for ( var m in gmap\_m7bef71eb92c02c79eee2edcafcfe9784.positions ) {
gmap\_m7bef71eb92c02c79eee2edcafcfe9784.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7bef71eb92c02c79eee2edcafcfe9784.map,
position : gmap\_m7bef71eb92c02c79eee2edcafcfe9784.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7bef71eb92c02c79eee2edcafcfe9784.map.setCenter( gmap\_m7bef71eb92c02c79eee2edcafcfe9784.positions[707] );
});