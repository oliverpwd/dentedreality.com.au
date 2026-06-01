---
title: ''
date: '2013-08-24T19:14:55+00:00'
format: image
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/fcf9259e0d1211e3bf5322000a9e17ee_7.jpg?resize=607%2C607
---

[![Impromptu hike with a view.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/fcf9259e0d1211e3bf5322000a9e17ee_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2013/08/24/impromptu-hike-with-a-view-2/) 

Impromptu hike with a view.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/dafuYMimGQ/) [7:14 pm, August 24, 2013](http://dentedreality.com.au/2013/08/24/impromptu-hike-with-a-view-2/ "7:14 pm") 
jQuery(document).ready(function(){
var gmap\_mb060d17112fd48efb358d94d59685457 = {
positions : {
238 : new google.maps.LatLng( '41.31852163', '-73.975843217' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb060d17112fd48efb358d94d59685457' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb060d17112fd48efb358d94d59685457.positions ) {
gmap\_mb060d17112fd48efb358d94d59685457.bounds.extend( gmap\_mb060d17112fd48efb358d94d59685457.positions[m] );
}
// Render markers
for ( var m in gmap\_mb060d17112fd48efb358d94d59685457.positions ) {
gmap\_mb060d17112fd48efb358d94d59685457.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb060d17112fd48efb358d94d59685457.map,
position : gmap\_mb060d17112fd48efb358d94d59685457.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb060d17112fd48efb358d94d59685457.map.setCenter( gmap\_mb060d17112fd48efb358d94d59685457.positions[238] );
});