---
title: ''
date: '2016-09-01T15:32:46+00:00'
format: image
service: instagram
tags:
- alpinelake
- colorado
- creek
- lake
- river
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14072817_1720770751517674_1287846505_n.jpg?fit=640%2C640
---

[![Feeding from lake to lake. #creek #river #lake #alpinelake #colorado](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14072817_1720770751517674_1287846505_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/09/01/feeding-from-lake-to-lake-creek-river-lake-alpinelake-colorado/) 

Feeding from lake to lake. #creek #river #lake #alpinelake #colorado





* #[alpinelake](http://dentedreality.com.au/tags/alpinelake/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[creek](http://dentedreality.com.au/tags/creek/)
* #[lake](http://dentedreality.com.au/tags/lake/)
* #[river](http://dentedreality.com.au/tags/river/)

Posted on [Instagram](https://www.instagram.com/p/BJ1BoPXAIki/) [3:32 pm, September 1, 2016](http://dentedreality.com.au/2016/09/01/feeding-from-lake-to-lake-creek-river-lake-alpinelake-colorado/ "3:32 pm") 
jQuery(document).ready(function(){
var gmap\_m7c2fbe4cef33a606d00dbe805eb24a67 = {
positions : {
624 : new google.maps.LatLng( '39.7935969', '-106.3350285' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7c2fbe4cef33a606d00dbe805eb24a67' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7c2fbe4cef33a606d00dbe805eb24a67.positions ) {
gmap\_m7c2fbe4cef33a606d00dbe805eb24a67.bounds.extend( gmap\_m7c2fbe4cef33a606d00dbe805eb24a67.positions[m] );
}
// Render markers
for ( var m in gmap\_m7c2fbe4cef33a606d00dbe805eb24a67.positions ) {
gmap\_m7c2fbe4cef33a606d00dbe805eb24a67.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7c2fbe4cef33a606d00dbe805eb24a67.map,
position : gmap\_m7c2fbe4cef33a606d00dbe805eb24a67.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7c2fbe4cef33a606d00dbe805eb24a67.map.setCenter( gmap\_m7c2fbe4cef33a606d00dbe805eb24a67.positions[624] );
});