---
title: Double Wrapped
date: '2012-12-22T09:54:54-07:00'
format: image
service: flickr
tags:
- chipotlemexicangrill
- flickriosapp:filter=iguana
- iguanafilter
- uploaded:by=flickrmobile
latitude: '40.73418'
longitude: '-73.989078'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/12/14190732/8296956531_470450cb45_o.jpg
---

[![Double Wrapped](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/12/14190732/8296956531_470450cb45_o.jpg)](https://dentedreality.com.au/2012/12/22/double-wrapped/) 
# [Double Wrapped](https://dentedreality.com.au/2012/12/22/double-wrapped/)

[![Double Wrapped](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/12/14190732/8296956531_470450cb45_o.jpg)](http://www.flickr.com/photos/borkazoid/8296956531/)

Disaster.

40.73418-73.989078




* #[chipotlemexicangrill](https://dentedreality.com.au/tags/chipotlemexicangrill/)
* #[flickriosapp:filter=iguana](https://dentedreality.com.au/tags/flickriosappfilteriguana/)
* #[iguanafilter](https://dentedreality.com.au/tags/iguanafilter/)
* #[uploaded:by=flickrmobile](https://dentedreality.com.au/tags/uploadedbyflickrmobile/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8296956531/) [9:54 am, December 22, 2012](https://dentedreality.com.au/2012/12/22/double-wrapped/ "9:54 am") 
jQuery(document).ready(function(){
var gmap\_m2808edb0dadc2ce3100db8ab133deb56 = {
positions : {
300 : new google.maps.LatLng( '40.73418', '-73.989078' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2808edb0dadc2ce3100db8ab133deb56' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2808edb0dadc2ce3100db8ab133deb56.positions ) {
gmap\_m2808edb0dadc2ce3100db8ab133deb56.bounds.extend( gmap\_m2808edb0dadc2ce3100db8ab133deb56.positions[m] );
}
// Render markers
for ( var m in gmap\_m2808edb0dadc2ce3100db8ab133deb56.positions ) {
gmap\_m2808edb0dadc2ce3100db8ab133deb56.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2808edb0dadc2ce3100db8ab133deb56.map,
position : gmap\_m2808edb0dadc2ce3100db8ab133deb56.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2808edb0dadc2ce3100db8ab133deb56.map.setCenter( gmap\_m2808edb0dadc2ce3100db8ab133deb56.positions[300] );
});