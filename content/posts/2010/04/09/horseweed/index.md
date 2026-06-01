---
title: Horseweed
date: '2010-04-09T10:16:10-06:00'
format: image
service: flickr
tags:
- horseweed
- tombrown
- trackerschool
- tracking
latitude: '37.177141'
longitude: '-122.116744'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185643/4516461466_bdcab9912e_o-768x1024.jpg
---

[![Horseweed](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185643/4516461466_bdcab9912e_o-768x1024.jpg)](https://dentedreality.com.au/2010/04/09/horseweed/) 
# [Horseweed](https://dentedreality.com.au/2010/04/09/horseweed/)

[![Horseweed](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185643/4516461466_bdcab9912e_o-768x1024.jpg)](http://www.flickr.com/photos/borkazoid/4516461466/)

As seen during our edible/medicinal plant walk.

37.177141-122.116744




* #[horseweed](https://dentedreality.com.au/tags/horseweed/)
* #[tombrown](https://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](https://dentedreality.com.au/tags/trackerschool/)
* #[tracking](https://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516461466/) [10:16 am, April 9, 2010](https://dentedreality.com.au/2010/04/09/horseweed/ "10:16 am") 
jQuery(document).ready(function(){
var gmap\_m023c198ed0ccf31341d812a3d8e2d0a8 = {
positions : {
684 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m023c198ed0ccf31341d812a3d8e2d0a8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m023c198ed0ccf31341d812a3d8e2d0a8.positions ) {
gmap\_m023c198ed0ccf31341d812a3d8e2d0a8.bounds.extend( gmap\_m023c198ed0ccf31341d812a3d8e2d0a8.positions[m] );
}
// Render markers
for ( var m in gmap\_m023c198ed0ccf31341d812a3d8e2d0a8.positions ) {
gmap\_m023c198ed0ccf31341d812a3d8e2d0a8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m023c198ed0ccf31341d812a3d8e2d0a8.map,
position : gmap\_m023c198ed0ccf31341d812a3d8e2d0a8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m023c198ed0ccf31341d812a3d8e2d0a8.map.setCenter( gmap\_m023c198ed0ccf31341d812a3d8e2d0a8.positions[684] );
});