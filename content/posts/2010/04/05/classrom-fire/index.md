---
title: Classrom Fire!
date: '2010-04-05T08:30:01-06:00'
format: image
service: flickr
tags:
- tombrown
- trackerschool
- tracking
latitude: '37.177141'
longitude: '-122.116744'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185627/4516434702_fae2f3c37e_o.jpg
---

[![Classrom Fire!](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185627/4516434702_fae2f3c37e_o.jpg)](https://dentedreality.com.au/2010/04/05/classrom-fire/) 
# [Classrom Fire!](https://dentedreality.com.au/2010/04/05/classrom-fire/)

[![Classrom Fire!](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185627/4516434702_fae2f3c37e_o.jpg)](http://www.flickr.com/photos/borkazoid/4516434702/)

During demonstration of the Bow Drill.

37.177141-122.116744




* #[tombrown](https://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](https://dentedreality.com.au/tags/trackerschool/)
* #[tracking](https://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516434702/) [8:30 am, April 5, 2010](https://dentedreality.com.au/2010/04/05/classrom-fire/ "8:30 am") 
jQuery(document).ready(function(){
var gmap\_mdd4d65da6aac91075db599afd76dafb0 = {
positions : {
22 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdd4d65da6aac91075db599afd76dafb0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdd4d65da6aac91075db599afd76dafb0.positions ) {
gmap\_mdd4d65da6aac91075db599afd76dafb0.bounds.extend( gmap\_mdd4d65da6aac91075db599afd76dafb0.positions[m] );
}
// Render markers
for ( var m in gmap\_mdd4d65da6aac91075db599afd76dafb0.positions ) {
gmap\_mdd4d65da6aac91075db599afd76dafb0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdd4d65da6aac91075db599afd76dafb0.map,
position : gmap\_mdd4d65da6aac91075db599afd76dafb0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdd4d65da6aac91075db599afd76dafb0.map.setCenter( gmap\_mdd4d65da6aac91075db599afd76dafb0.positions[22] );
});