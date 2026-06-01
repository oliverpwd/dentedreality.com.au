---
title: ''
date: '2018-06-29T22:26:54-06:00'
format: image
service: instagram
tags:
- fjallravenclassicusa
latitude: '39.4285985'
longitude: '-106.2272464'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182136/35616857_217619839064248_2122499930613350400_n.jpg?resize=607%2C607&ssl=1
---

[![Some absolutely stunning views on the #fjallravenclassicusa these past few days.](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182136/35616857_217619839064248_2122499930613350400_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/06/29/some-absolutely-stunning-views-on-the-fjallravenclassicusa-these-past-few-days/) 

[![Some absolutely stunning views on the #fjallravenclassicusa these past few days.](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182136/35616857_217619839064248_2122499930613350400_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/BkoqcLaFOa_/)

Some absolutely stunning views on the #fjallravenclassicusa these past few days.

39.4285985-106.2272464




* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BkoqcLaFOa_/) [10:26 pm, June 29, 2018](https://dentedreality.com.au/2018/06/29/some-absolutely-stunning-views-on-the-fjallravenclassicusa-these-past-few-days/ "10:26 pm") 
jQuery(document).ready(function(){
var gmap\_m6ecfcb728a9e4e0de430911fbef7162e = {
positions : {
226 : new google.maps.LatLng( '39.4285985', '-106.2272464' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6ecfcb728a9e4e0de430911fbef7162e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6ecfcb728a9e4e0de430911fbef7162e.positions ) {
gmap\_m6ecfcb728a9e4e0de430911fbef7162e.bounds.extend( gmap\_m6ecfcb728a9e4e0de430911fbef7162e.positions[m] );
}
// Render markers
for ( var m in gmap\_m6ecfcb728a9e4e0de430911fbef7162e.positions ) {
gmap\_m6ecfcb728a9e4e0de430911fbef7162e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6ecfcb728a9e4e0de430911fbef7162e.map,
position : gmap\_m6ecfcb728a9e4e0de430911fbef7162e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6ecfcb728a9e4e0de430911fbef7162e.map.setCenter( gmap\_m6ecfcb728a9e4e0de430911fbef7162e.positions[226] );
});