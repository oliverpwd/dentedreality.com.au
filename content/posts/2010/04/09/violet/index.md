---
title: Violet
date: '2010-04-09T11:15:20-06:00'
format: image
service: flickr
tags:
- tombrown
- trackerschool
- tracking
- violet
latitude: '37.177141'
longitude: '-122.116744'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185650/4515831789_f89a83b11d_o-768x1024.jpg
---

[![Violet](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185650/4515831789_f89a83b11d_o-768x1024.jpg)](https://dentedreality.com.au/2010/04/09/violet/) 
# [Violet](https://dentedreality.com.au/2010/04/09/violet/)

[![Violet](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185650/4515831789_f89a83b11d_o-768x1024.jpg)](http://www.flickr.com/photos/borkazoid/4515831789/)

As seen during our edible/medicinal plant walk.

37.177141-122.116744




* #[tombrown](https://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](https://dentedreality.com.au/tags/trackerschool/)
* #[tracking](https://dentedreality.com.au/tags/tracking/)
* #[violet](https://dentedreality.com.au/tags/violet/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4515831789/) [11:15 am, April 9, 2010](https://dentedreality.com.au/2010/04/09/violet/ "11:15 am") 
jQuery(document).ready(function(){
var gmap\_m5d9bb84c6147f7c54ca2964129af5b08 = {
positions : {
592 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5d9bb84c6147f7c54ca2964129af5b08' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5d9bb84c6147f7c54ca2964129af5b08.positions ) {
gmap\_m5d9bb84c6147f7c54ca2964129af5b08.bounds.extend( gmap\_m5d9bb84c6147f7c54ca2964129af5b08.positions[m] );
}
// Render markers
for ( var m in gmap\_m5d9bb84c6147f7c54ca2964129af5b08.positions ) {
gmap\_m5d9bb84c6147f7c54ca2964129af5b08.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5d9bb84c6147f7c54ca2964129af5b08.map,
position : gmap\_m5d9bb84c6147f7c54ca2964129af5b08.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5d9bb84c6147f7c54ca2964129af5b08.map.setCenter( gmap\_m5d9bb84c6147f7c54ca2964129af5b08.positions[592] );
});