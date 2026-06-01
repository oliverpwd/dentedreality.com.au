---
title: ''
date: '2017-05-21T18:03:18+00:00'
format: image
service: instagram
tags:
- fjällrävenclassic2017
- fjallravenclassicusa
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18644907_435049506860932_2818105536724074496_n.jpg?fit=640%2C640&ssl=1
---

[![Another training hike for #fjällrävenclassic2017. Accidentally 10 miles.](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18644907_435049506860932_2818105536724074496_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/05/21/another-training-hike-for-fjallravenclassic2017-accidentally-10-miles/) 

Another training hike for #fjällrävenclassic2017. Accidentally 10 miles.





* #[fjällrävenclassic2017](https://dentedreality.com.au/tags/fjallravenclassic2017/)
* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BUX7H7NBw-p/) [6:03 pm, May 21, 2017](https://dentedreality.com.au/2017/05/21/another-training-hike-for-fjallravenclassic2017-accidentally-10-miles/ "6:03 pm") 
jQuery(document).ready(function(){
var gmap\_m0a8309a1044ae11fae92242018353ef2 = {
positions : {
37 : new google.maps.LatLng( '39.7683409616', '-105.215712653' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0a8309a1044ae11fae92242018353ef2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0a8309a1044ae11fae92242018353ef2.positions ) {
gmap\_m0a8309a1044ae11fae92242018353ef2.bounds.extend( gmap\_m0a8309a1044ae11fae92242018353ef2.positions[m] );
}
// Render markers
for ( var m in gmap\_m0a8309a1044ae11fae92242018353ef2.positions ) {
gmap\_m0a8309a1044ae11fae92242018353ef2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0a8309a1044ae11fae92242018353ef2.map,
position : gmap\_m0a8309a1044ae11fae92242018353ef2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0a8309a1044ae11fae92242018353ef2.map.setCenter( gmap\_m0a8309a1044ae11fae92242018353ef2.positions[37] );
});