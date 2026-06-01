---
title: GAFFTA Galvanize
date: '2011-12-15T13:41:47-07:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- cocktailparty
- gaffta
- gafftagalvanize
- me
- tuxedo
latitude: '37.791333'
longitude: '-122.417834'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/12/14190429/6959388393_33b8068521_o.jpg
---

[![GAFFTA Galvanize](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/12/14190429/6959388393_33b8068521_o.jpg)](https://dentedreality.com.au/2011/12/15/gaffta-galvanize-5/) 
# [GAFFTA Galvanize](https://dentedreality.com.au/2011/12/15/gaffta-galvanize-5/)

[![GAFFTA Galvanize](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/12/14190429/6959388393_33b8068521_o.jpg)](http://www.flickr.com/photos/borkazoid/6959388393/)

"Galvanize", hosted by the Grey Area Foundation For the Arts.

37.791333-122.417834




* #[beau](https://dentedreality.com.au/tags/beau/)
* #[beaulebens](https://dentedreality.com.au/tags/beaulebens/)
* #[cocktailparty](https://dentedreality.com.au/tags/cocktailparty/)
* #[gaffta](https://dentedreality.com.au/tags/gaffta/)
* #[gafftagalvanize](https://dentedreality.com.au/tags/gafftagalvanize/)
* #[me](https://dentedreality.com.au/tags/me/)
* #[tuxedo](https://dentedreality.com.au/tags/tuxedo/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959388393/) [1:41 pm, December 15, 2011](https://dentedreality.com.au/2011/12/15/gaffta-galvanize-5/ "1:41 pm") 
jQuery(document).ready(function(){
var gmap\_m8b64741101def20ffbb75377bfa87e24 = {
positions : {
988 : new google.maps.LatLng( '37.791333', '-122.417834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8b64741101def20ffbb75377bfa87e24' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8b64741101def20ffbb75377bfa87e24.positions ) {
gmap\_m8b64741101def20ffbb75377bfa87e24.bounds.extend( gmap\_m8b64741101def20ffbb75377bfa87e24.positions[m] );
}
// Render markers
for ( var m in gmap\_m8b64741101def20ffbb75377bfa87e24.positions ) {
gmap\_m8b64741101def20ffbb75377bfa87e24.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8b64741101def20ffbb75377bfa87e24.map,
position : gmap\_m8b64741101def20ffbb75377bfa87e24.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8b64741101def20ffbb75377bfa87e24.map.setCenter( gmap\_m8b64741101def20ffbb75377bfa87e24.positions[988] );
});