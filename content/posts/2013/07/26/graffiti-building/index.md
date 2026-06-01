---
title: Graffiti Building
date: '2013-07-26T13:45:53-06:00'
format: image
service: flickr
tags:
- building
- graffiti
- tagged
latitude: '37.794999'
longitude: '-122.397334'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2013/07/14190949/9440401324_149635c4e4_o.jpg
---

[![Graffiti Building](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2013/07/14190949/9440401324_149635c4e4_o.jpg)](https://dentedreality.com.au/2013/07/26/graffiti-building/) 
# [Graffiti Building](https://dentedreality.com.au/2013/07/26/graffiti-building/)

[![Graffiti Building](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2013/07/14190949/9440401324_149635c4e4_o.jpg)](http://www.flickr.com/photos/borkazoid/9440401324/)

37.794999-122.397334




* #[building](https://dentedreality.com.au/tags/building/)
* #[graffiti](https://dentedreality.com.au/tags/graffiti/)
* #[tagged](https://dentedreality.com.au/tags/tagged/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9440401324/) [1:45 pm, July 26, 2013](https://dentedreality.com.au/2013/07/26/graffiti-building/ "1:45 pm") 
jQuery(document).ready(function(){
var gmap\_mc982ae376f79e59e8656ce868c53e8c0 = {
positions : {
588 : new google.maps.LatLng( '37.794999', '-122.397334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc982ae376f79e59e8656ce868c53e8c0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc982ae376f79e59e8656ce868c53e8c0.positions ) {
gmap\_mc982ae376f79e59e8656ce868c53e8c0.bounds.extend( gmap\_mc982ae376f79e59e8656ce868c53e8c0.positions[m] );
}
// Render markers
for ( var m in gmap\_mc982ae376f79e59e8656ce868c53e8c0.positions ) {
gmap\_mc982ae376f79e59e8656ce868c53e8c0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc982ae376f79e59e8656ce868c53e8c0.map,
position : gmap\_mc982ae376f79e59e8656ce868c53e8c0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc982ae376f79e59e8656ce868c53e8c0.map.setCenter( gmap\_mc982ae376f79e59e8656ce868c53e8c0.positions[588] );
});