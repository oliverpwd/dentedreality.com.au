---
title: ''
date: '2014-09-26T18:21:00+00:00'
format: image
tags:
- burritofriday
- photo
- redrocks
- selfie
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10691701_341241936000638_885166346_n.jpg?resize=640%2C640
---

[![#burritofriday #redrocks #selfie!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10691701_341241936000638_885166346_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/09/26/burritofriday-redrocks-selfie/) 

#burritofriday #redrocks #selfie!





* #[burritofriday](http://dentedreality.com.au/tags/burritofriday/)
* #[photo](http://dentedreality.com.au/tags/photo/)
* #[redrocks](http://dentedreality.com.au/tags/redrocks/)
* #[selfie](http://dentedreality.com.au/tags/selfie/)

Posted on [Instagram](http://instagram.com/p/tbbqotimI_/) [6:21 pm, September 26, 2014](http://dentedreality.com.au/2014/09/26/burritofriday-redrocks-selfie/ "6:21 pm") 
jQuery(document).ready(function(){
var gmap\_macf015cba50d32f1b8c4be53d0cc7597 = {
positions : {
899 : new google.maps.LatLng( '39.665590501', '-105.20567503' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_macf015cba50d32f1b8c4be53d0cc7597' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_macf015cba50d32f1b8c4be53d0cc7597.positions ) {
gmap\_macf015cba50d32f1b8c4be53d0cc7597.bounds.extend( gmap\_macf015cba50d32f1b8c4be53d0cc7597.positions[m] );
}
// Render markers
for ( var m in gmap\_macf015cba50d32f1b8c4be53d0cc7597.positions ) {
gmap\_macf015cba50d32f1b8c4be53d0cc7597.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_macf015cba50d32f1b8c4be53d0cc7597.map,
position : gmap\_macf015cba50d32f1b8c4be53d0cc7597.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_macf015cba50d32f1b8c4be53d0cc7597.map.setCenter( gmap\_macf015cba50d32f1b8c4be53d0cc7597.positions[899] );
});