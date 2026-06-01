---
title: La Observatorio
date: '2010-01-13T12:43:49-07:00'
format: image
service: flickr
tags:
- cafe
- Chile
- observatorio
- office
- Santiago
latitude: '-33.434667'
longitude: '-70.641167'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/01/14185528/4285237534_5ccf20b563_o.jpg
---

[![La Observatorio](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/01/14185528/4285237534_5ccf20b563_o.jpg)](https://dentedreality.com.au/2010/01/13/la-observatorio/) 
# [La Observatorio](https://dentedreality.com.au/2010/01/13/la-observatorio/)

[![La Observatorio](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/01/14185528/4285237534_5ccf20b563_o.jpg)](http://www.flickr.com/photos/borkazoid/4285237534/)

I think that was the name.

-33.434667-70.641167




* #[cafe](https://dentedreality.com.au/tags/cafe/)
* #[Chile](https://dentedreality.com.au/tags/chile/)
* #[observatorio](https://dentedreality.com.au/tags/observatorio/)
* #[office](https://dentedreality.com.au/tags/office/)
* #[Santiago](https://dentedreality.com.au/tags/santiago/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4285237534/) [12:43 pm, January 13, 2010](https://dentedreality.com.au/2010/01/13/la-observatorio/ "12:43 pm") 
jQuery(document).ready(function(){
var gmap\_mba5592d21c8522b0fbd67488a7d77962 = {
positions : {
820 : new google.maps.LatLng( '-33.434667', '-70.641167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mba5592d21c8522b0fbd67488a7d77962' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mba5592d21c8522b0fbd67488a7d77962.positions ) {
gmap\_mba5592d21c8522b0fbd67488a7d77962.bounds.extend( gmap\_mba5592d21c8522b0fbd67488a7d77962.positions[m] );
}
// Render markers
for ( var m in gmap\_mba5592d21c8522b0fbd67488a7d77962.positions ) {
gmap\_mba5592d21c8522b0fbd67488a7d77962.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mba5592d21c8522b0fbd67488a7d77962.map,
position : gmap\_mba5592d21c8522b0fbd67488a7d77962.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mba5592d21c8522b0fbd67488a7d77962.map.setCenter( gmap\_mba5592d21c8522b0fbd67488a7d77962.positions[820] );
});