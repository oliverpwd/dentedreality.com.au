---
title: Figure 4 Trap
date: '2010-04-05T17:56:39-06:00'
format: image
service: flickr
tags:
- figure4
- tombrown
- trackerschool
- tracking
- traps
latitude: '37.177141'
longitude: '-122.116744'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185628/4515800399_c451d423d1_o.jpg
---

[![Figure 4 Trap](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185628/4515800399_c451d423d1_o.jpg)](https://dentedreality.com.au/2010/04/05/figure-4-trap/) 
# [Figure 4 Trap](https://dentedreality.com.au/2010/04/05/figure-4-trap/)

[![Figure 4 Trap](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185628/4515800399_c451d423d1_o.jpg)](http://www.flickr.com/photos/borkazoid/4515800399/)

Jorge demonstrates a giant Figure 4 deadfall trap.

37.177141-122.116744




* #[figure4](https://dentedreality.com.au/tags/figure4/)
* #[tombrown](https://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](https://dentedreality.com.au/tags/trackerschool/)
* #[tracking](https://dentedreality.com.au/tags/tracking/)
* #[traps](https://dentedreality.com.au/tags/traps/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4515800399/) [5:56 pm, April 5, 2010](https://dentedreality.com.au/2010/04/05/figure-4-trap/ "5:56 pm") 
jQuery(document).ready(function(){
var gmap\_m07daedb812af477036d1d602f9249c6e = {
positions : {
286 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m07daedb812af477036d1d602f9249c6e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m07daedb812af477036d1d602f9249c6e.positions ) {
gmap\_m07daedb812af477036d1d602f9249c6e.bounds.extend( gmap\_m07daedb812af477036d1d602f9249c6e.positions[m] );
}
// Render markers
for ( var m in gmap\_m07daedb812af477036d1d602f9249c6e.positions ) {
gmap\_m07daedb812af477036d1d602f9249c6e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m07daedb812af477036d1d602f9249c6e.map,
position : gmap\_m07daedb812af477036d1d602f9249c6e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m07daedb812af477036d1d602f9249c6e.map.setCenter( gmap\_m07daedb812af477036d1d602f9249c6e.positions[286] );
});