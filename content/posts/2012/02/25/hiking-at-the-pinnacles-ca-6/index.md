---
title: Hiking at The Pinnacles, CA
date: '2012-02-25T09:41:49+00:00'
format: image
service: flickr
tags:
- california
- hike
- hiking
- pinnacles
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813464672_c90aff06e7_o.jpg?resize=607%2C813
---

[![Hiking at The Pinnacles, CA](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813464672_c90aff06e7_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-6/) 
# [Hiking at The Pinnacles, CA](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-6/)





* #[california](http://dentedreality.com.au/tags/california/)
* #[hike](http://dentedreality.com.au/tags/hike/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[pinnacles](http://dentedreality.com.au/tags/pinnacles/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813464672/) [9:41 am, February 25, 2012](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-6/ "9:41 am") 
jQuery(document).ready(function(){
var gmap\_me1c0076d4b53bd2a3e9b7bce95f1adbe = {
positions : {
322 : new google.maps.LatLng( '37.163', '-121.7685' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me1c0076d4b53bd2a3e9b7bce95f1adbe' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me1c0076d4b53bd2a3e9b7bce95f1adbe.positions ) {
gmap\_me1c0076d4b53bd2a3e9b7bce95f1adbe.bounds.extend( gmap\_me1c0076d4b53bd2a3e9b7bce95f1adbe.positions[m] );
}
// Render markers
for ( var m in gmap\_me1c0076d4b53bd2a3e9b7bce95f1adbe.positions ) {
gmap\_me1c0076d4b53bd2a3e9b7bce95f1adbe.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me1c0076d4b53bd2a3e9b7bce95f1adbe.map,
position : gmap\_me1c0076d4b53bd2a3e9b7bce95f1adbe.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me1c0076d4b53bd2a3e9b7bce95f1adbe.map.setCenter( gmap\_me1c0076d4b53bd2a3e9b7bce95f1adbe.positions[322] );
});