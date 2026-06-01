---
title: GAFFTA Galvanize
date: '2011-12-15T16:57:06-07:00'
format: image
service: flickr
tags:
- cocktailparty
- gaffta
- gafftagalvanize
- tuxedo
latitude: '37.7825'
longitude: '-122.410334'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/12/14190430/6813277386_0ee93e3bfd_o.jpg
---

[![GAFFTA Galvanize](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/12/14190430/6813277386_0ee93e3bfd_o.jpg)](https://dentedreality.com.au/2011/12/15/gaffta-galvanize-4/) 
# [GAFFTA Galvanize](https://dentedreality.com.au/2011/12/15/gaffta-galvanize-4/)

[![GAFFTA Galvanize](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/12/14190430/6813277386_0ee93e3bfd_o.jpg)](http://www.flickr.com/photos/borkazoid/6813277386/)

"Galvanize", hosted by the Grey Area Foundation For the Arts.

37.7825-122.410334




* #[cocktailparty](https://dentedreality.com.au/tags/cocktailparty/)
* #[gaffta](https://dentedreality.com.au/tags/gaffta/)
* #[gafftagalvanize](https://dentedreality.com.au/tags/gafftagalvanize/)
* #[tuxedo](https://dentedreality.com.au/tags/tuxedo/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813277386/) [4:57 pm, December 15, 2011](https://dentedreality.com.au/2011/12/15/gaffta-galvanize-4/ "4:57 pm") 
jQuery(document).ready(function(){
var gmap\_ma18824fa90cb6f10c658adb9f8b71539 = {
positions : {
32 : new google.maps.LatLng( '37.7825', '-122.410334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma18824fa90cb6f10c658adb9f8b71539' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma18824fa90cb6f10c658adb9f8b71539.positions ) {
gmap\_ma18824fa90cb6f10c658adb9f8b71539.bounds.extend( gmap\_ma18824fa90cb6f10c658adb9f8b71539.positions[m] );
}
// Render markers
for ( var m in gmap\_ma18824fa90cb6f10c658adb9f8b71539.positions ) {
gmap\_ma18824fa90cb6f10c658adb9f8b71539.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma18824fa90cb6f10c658adb9f8b71539.map,
position : gmap\_ma18824fa90cb6f10c658adb9f8b71539.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma18824fa90cb6f10c658adb9f8b71539.map.setCenter( gmap\_ma18824fa90cb6f10c658adb9f8b71539.positions[32] );
});