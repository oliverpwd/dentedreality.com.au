---
title: ''
date: '2012-11-08T15:30:13+00:00'
format: image
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/b7f32ef229da11e28e8322000a1f9686_7.jpg?resize=607%2C607
---

[![Ginkgo/snow-frosted car.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/b7f32ef229da11e28e8322000a1f9686_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/11/08/ginkgosnow-frosted-car/) 

Ginkgo/snow-frosted car.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/Rx8RzeimIW/) [3:30 pm, November 8, 2012](http://dentedreality.com.au/2012/11/08/ginkgosnow-frosted-car/ "3:30 pm") 
jQuery(document).ready(function(){
var gmap\_mcccd7a7e261b6a99dd2003a8bb5688b7 = {
positions : {
267 : new google.maps.LatLng( '40.667999267', '-73.982002258' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mcccd7a7e261b6a99dd2003a8bb5688b7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mcccd7a7e261b6a99dd2003a8bb5688b7.positions ) {
gmap\_mcccd7a7e261b6a99dd2003a8bb5688b7.bounds.extend( gmap\_mcccd7a7e261b6a99dd2003a8bb5688b7.positions[m] );
}
// Render markers
for ( var m in gmap\_mcccd7a7e261b6a99dd2003a8bb5688b7.positions ) {
gmap\_mcccd7a7e261b6a99dd2003a8bb5688b7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mcccd7a7e261b6a99dd2003a8bb5688b7.map,
position : gmap\_mcccd7a7e261b6a99dd2003a8bb5688b7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mcccd7a7e261b6a99dd2003a8bb5688b7.map.setCenter( gmap\_mcccd7a7e261b6a99dd2003a8bb5688b7.positions[267] );
});