---
title: Hiking at The Pinnacles, CA
date: '2012-02-25T09:38:52+00:00'
format: image
service: flickr
tags:
- california
- hike
- hiking
- pinnacles
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813464358_aa5a66cfba_o.jpg?resize=607%2C452
---

[![Hiking at The Pinnacles, CA](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813464358_aa5a66cfba_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-7/) 
# [Hiking at The Pinnacles, CA](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-7/)





* #[california](http://dentedreality.com.au/tags/california/)
* #[hike](http://dentedreality.com.au/tags/hike/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[pinnacles](http://dentedreality.com.au/tags/pinnacles/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813464358/) [9:38 am, February 25, 2012](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-7/ "9:38 am") 
jQuery(document).ready(function(){
var gmap\_m2ddb15b266cbd011f698c42a52011306 = {
positions : {
986 : new google.maps.LatLng( '37.163', '-121.7685' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2ddb15b266cbd011f698c42a52011306' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2ddb15b266cbd011f698c42a52011306.positions ) {
gmap\_m2ddb15b266cbd011f698c42a52011306.bounds.extend( gmap\_m2ddb15b266cbd011f698c42a52011306.positions[m] );
}
// Render markers
for ( var m in gmap\_m2ddb15b266cbd011f698c42a52011306.positions ) {
gmap\_m2ddb15b266cbd011f698c42a52011306.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2ddb15b266cbd011f698c42a52011306.map,
position : gmap\_m2ddb15b266cbd011f698c42a52011306.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2ddb15b266cbd011f698c42a52011306.map.setCenter( gmap\_m2ddb15b266cbd011f698c42a52011306.positions[986] );
});