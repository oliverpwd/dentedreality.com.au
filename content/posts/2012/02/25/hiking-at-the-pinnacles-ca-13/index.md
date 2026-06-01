---
title: Hiking at The Pinnacles, CA
date: '2012-02-25T07:19:48+00:00'
format: image
service: flickr
tags:
- california
- hike
- hiking
- pinnacles
- wallpaper
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959574991_129b8c8de2_o.jpg?resize=607%2C452
---

[![Hiking at The Pinnacles, CA](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959574991_129b8c8de2_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-13/) 
# [Hiking at The Pinnacles, CA](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-13/)





* #[california](http://dentedreality.com.au/tags/california/)
* #[hike](http://dentedreality.com.au/tags/hike/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[pinnacles](http://dentedreality.com.au/tags/pinnacles/)
* #[wallpaper](http://dentedreality.com.au/tags/wallpaper/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959574991/) [7:19 am, February 25, 2012](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-13/ "7:19 am") 
jQuery(document).ready(function(){
var gmap\_me93ba55e2f51f9540a239965d9a92046 = {
positions : {
97 : new google.maps.LatLng( '37.163', '-121.7685' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me93ba55e2f51f9540a239965d9a92046' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me93ba55e2f51f9540a239965d9a92046.positions ) {
gmap\_me93ba55e2f51f9540a239965d9a92046.bounds.extend( gmap\_me93ba55e2f51f9540a239965d9a92046.positions[m] );
}
// Render markers
for ( var m in gmap\_me93ba55e2f51f9540a239965d9a92046.positions ) {
gmap\_me93ba55e2f51f9540a239965d9a92046.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me93ba55e2f51f9540a239965d9a92046.map,
position : gmap\_me93ba55e2f51f9540a239965d9a92046.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me93ba55e2f51f9540a239965d9a92046.map.setCenter( gmap\_me93ba55e2f51f9540a239965d9a92046.positions[97] );
});