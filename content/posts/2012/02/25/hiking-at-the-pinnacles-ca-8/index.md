---
title: Hiking at The Pinnacles, CA
date: '2012-02-25T09:31:34+00:00'
format: image
service: flickr
tags:
- california
- hike
- hiking
- pinnacles
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959576235_31a65b9c38_o.jpg?resize=607%2C452
---

[![Hiking at The Pinnacles, CA](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6959576235_31a65b9c38_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-8/) 
# [Hiking at The Pinnacles, CA](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-8/)





* #[california](http://dentedreality.com.au/tags/california/)
* #[hike](http://dentedreality.com.au/tags/hike/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[pinnacles](http://dentedreality.com.au/tags/pinnacles/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959576235/) [9:31 am, February 25, 2012](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-8/ "9:31 am") 
jQuery(document).ready(function(){
var gmap\_m1b023e992f6ad980c2fb13f8511c63b9 = {
positions : {
5 : new google.maps.LatLng( '37.163', '-121.7685' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1b023e992f6ad980c2fb13f8511c63b9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1b023e992f6ad980c2fb13f8511c63b9.positions ) {
gmap\_m1b023e992f6ad980c2fb13f8511c63b9.bounds.extend( gmap\_m1b023e992f6ad980c2fb13f8511c63b9.positions[m] );
}
// Render markers
for ( var m in gmap\_m1b023e992f6ad980c2fb13f8511c63b9.positions ) {
gmap\_m1b023e992f6ad980c2fb13f8511c63b9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1b023e992f6ad980c2fb13f8511c63b9.map,
position : gmap\_m1b023e992f6ad980c2fb13f8511c63b9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1b023e992f6ad980c2fb13f8511c63b9.map.setCenter( gmap\_m1b023e992f6ad980c2fb13f8511c63b9.positions[5] );
});