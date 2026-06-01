---
title: Hiking at The Pinnacles, CA
date: '2012-02-25T07:47:53+00:00'
format: image
service: flickr
tags:
- california
- hike
- hiking
- pinnacles
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813463390_62b92e269b_o.jpg?resize=607%2C452
---

[![Hiking at The Pinnacles, CA](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813463390_62b92e269b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-10/) 
# [Hiking at The Pinnacles, CA](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-10/)





* #[california](http://dentedreality.com.au/tags/california/)
* #[hike](http://dentedreality.com.au/tags/hike/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[pinnacles](http://dentedreality.com.au/tags/pinnacles/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813463390/) [7:47 am, February 25, 2012](http://dentedreality.com.au/2012/02/25/hiking-at-the-pinnacles-ca-10/ "7:47 am") 
jQuery(document).ready(function(){
var gmap\_mb612dcdb9c9f8266025eff1b54de464b = {
positions : {
869 : new google.maps.LatLng( '37.163', '-121.7685' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb612dcdb9c9f8266025eff1b54de464b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb612dcdb9c9f8266025eff1b54de464b.positions ) {
gmap\_mb612dcdb9c9f8266025eff1b54de464b.bounds.extend( gmap\_mb612dcdb9c9f8266025eff1b54de464b.positions[m] );
}
// Render markers
for ( var m in gmap\_mb612dcdb9c9f8266025eff1b54de464b.positions ) {
gmap\_mb612dcdb9c9f8266025eff1b54de464b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb612dcdb9c9f8266025eff1b54de464b.map,
position : gmap\_mb612dcdb9c9f8266025eff1b54de464b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb612dcdb9c9f8266025eff1b54de464b.map.setCenter( gmap\_mb612dcdb9c9f8266025eff1b54de464b.positions[869] );
});