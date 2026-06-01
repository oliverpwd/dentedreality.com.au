---
title: ''
date: '2017-03-26T22:35:35-06:00'
format: image
service: instagram
tags:
- garden
- irrigation
- spring
- vegetablegarden
latitude: '39.7572'
longitude: '-104.967'
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/03/17494797_283927198709655_7228191451044118528_n.jpg?fit=640%2C640&ssl=1
---

[![Finally got all of our irrigation in on all the beds. Officially ready for planting #garden #vegetablegarden #spring #irrigation](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/03/17494797_283927198709655_7228191451044118528_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/03/26/finally-got-all-of-our-irrigation-in-on-all-the-beds-officially-ready-for-planting-garden-vegetablegarden-spring-irrigation/) 

[![Finally got all of our irrigation in on all the beds. Officially ready for planting #garden #vegetablegarden #spring #irrigation](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/03/17494797_283927198709655_7228191451044118528_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BSINxNPBRmV/)

Finally got all of our irrigation in on all the beds. Officially ready for planting #garden #vegetablegarden #spring #irrigation

39.7572-104.967




* #[garden](https://dentedreality.com.au/tags/garden/)
* #[irrigation](https://dentedreality.com.au/tags/irrigation/)
* #[spring](https://dentedreality.com.au/tags/spring/)
* #[vegetablegarden](https://dentedreality.com.au/tags/vegetablegarden/)

Posted on [Instagram](https://www.instagram.com/p/BSINxNPBRmV/) [10:35 pm, March 26, 2017](https://dentedreality.com.au/2017/03/26/finally-got-all-of-our-irrigation-in-on-all-the-beds-officially-ready-for-planting-garden-vegetablegarden-spring-irrigation/ "10:35 pm") 
jQuery(document).ready(function(){
var gmap\_m84a8b9e37f86d81e612cb82863ba0ee1 = {
positions : {
358 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m84a8b9e37f86d81e612cb82863ba0ee1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m84a8b9e37f86d81e612cb82863ba0ee1.positions ) {
gmap\_m84a8b9e37f86d81e612cb82863ba0ee1.bounds.extend( gmap\_m84a8b9e37f86d81e612cb82863ba0ee1.positions[m] );
}
// Render markers
for ( var m in gmap\_m84a8b9e37f86d81e612cb82863ba0ee1.positions ) {
gmap\_m84a8b9e37f86d81e612cb82863ba0ee1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m84a8b9e37f86d81e612cb82863ba0ee1.map,
position : gmap\_m84a8b9e37f86d81e612cb82863ba0ee1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m84a8b9e37f86d81e612cb82863ba0ee1.map.setCenter( gmap\_m84a8b9e37f86d81e612cb82863ba0ee1.positions[358] );
});