---
title: ''
date: '2017-04-01T17:50:56+00:00'
format: image
service: instagram
tags:
- gardening
- irrigation
- vegetablegarden
image: http://dentedreality.com.au/wp-content/uploads/2017/04/17661813_274057436382687_5558279106610593792_n.jpg
---

[![Heavy modifications required, but getting good coverage now. #gardening #irrigation #vegetablegarden](http://dentedreality.com.au/wp-content/uploads/2017/04/17661813_274057436382687_5558279106610593792_n.jpg)](https://dentedreality.com.au/2017/04/01/heavy-modifications-required-but-getting-good-coverage-now-gardening-irrigation-vegetablegarden/) 

[![Heavy modifications required, but getting good coverage now. #gardening #irrigation #vegetablegarden](http://dentedreality.com.au/wp-content/uploads/2017/04/17661813_274057436382687_5558279106610593792_n.jpg)](https://www.instagram.com/p/BSXJ9rwhVTl/)

Heavy modifications required, but getting good coverage now. #gardening #irrigation #vegetablegarden





* #[gardening](https://dentedreality.com.au/tags/gardening/)
* #[irrigation](https://dentedreality.com.au/tags/irrigation/)
* #[vegetablegarden](https://dentedreality.com.au/tags/vegetablegarden/)

Posted on [Instagram](https://www.instagram.com/p/BSXJ9rwhVTl/) [5:50 pm, April 1, 2017](https://dentedreality.com.au/2017/04/01/heavy-modifications-required-but-getting-good-coverage-now-gardening-irrigation-vegetablegarden/ "5:50 pm") 
jQuery(document).ready(function(){
var gmap\_mcf9873a8f4158f268d441f141a0dd337 = {
positions : {
386 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mcf9873a8f4158f268d441f141a0dd337' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mcf9873a8f4158f268d441f141a0dd337.positions ) {
gmap\_mcf9873a8f4158f268d441f141a0dd337.bounds.extend( gmap\_mcf9873a8f4158f268d441f141a0dd337.positions[m] );
}
// Render markers
for ( var m in gmap\_mcf9873a8f4158f268d441f141a0dd337.positions ) {
gmap\_mcf9873a8f4158f268d441f141a0dd337.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mcf9873a8f4158f268d441f141a0dd337.map,
position : gmap\_mcf9873a8f4158f268d441f141a0dd337.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mcf9873a8f4158f268d441f141a0dd337.map.setCenter( gmap\_mcf9873a8f4158f268d441f141a0dd337.positions[386] );
});