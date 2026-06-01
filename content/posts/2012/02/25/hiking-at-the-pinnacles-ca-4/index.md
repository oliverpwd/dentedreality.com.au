---
title: Hiking at The Pinnacles, CA
date: '2012-02-25T10:16:08+00:00'
format: image
service: flickr
tags:
- california
- hike
- hiking
- pinnacles
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813465348_f7d238e4b4_o.jpg?resize=607%2C452
---

[![Hiking at The Pinnacles, CA](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813465348_f7d238e4b4_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-4/) 
# [Hiking at The Pinnacles, CA](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-4/)





* #[california](http://dentedreality.com.au/tags/california/)
* #[hike](http://dentedreality.com.au/tags/hike/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[pinnacles](http://dentedreality.com.au/tags/pinnacles/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813465348/) [10:16 am, February 25, 2012](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-4/ "10:16 am") 
jQuery(document).ready(function(){
var gmap\_m11b6b3f87e99ab152022f6e07fbd09a5 = {
positions : {
689 : new google.maps.LatLng( '37.163', '-121.7685' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m11b6b3f87e99ab152022f6e07fbd09a5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m11b6b3f87e99ab152022f6e07fbd09a5.positions ) {
gmap\_m11b6b3f87e99ab152022f6e07fbd09a5.bounds.extend( gmap\_m11b6b3f87e99ab152022f6e07fbd09a5.positions[m] );
}
// Render markers
for ( var m in gmap\_m11b6b3f87e99ab152022f6e07fbd09a5.positions ) {
gmap\_m11b6b3f87e99ab152022f6e07fbd09a5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m11b6b3f87e99ab152022f6e07fbd09a5.map,
position : gmap\_m11b6b3f87e99ab152022f6e07fbd09a5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m11b6b3f87e99ab152022f6e07fbd09a5.map.setCenter( gmap\_m11b6b3f87e99ab152022f6e07fbd09a5.positions[689] );
});