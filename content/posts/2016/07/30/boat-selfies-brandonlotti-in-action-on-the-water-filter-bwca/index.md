---
title: ''
date: '2016-07-30T10:00:02-06:00'
format: image
service: instagram
tags:
- bwca
latitude: '47.9637014'
longitude: '-91.5469748'
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13721231_879908758781454_534542354_n.jpg?fit=640%2C640
---

[![Boat selfies. @brandonlotti in action on the water filter. #bwca](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13721231_879908758781454_534542354_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/07/30/boat-selfies-brandonlotti-in-action-on-the-water-filter-bwca/) 

[![Boat selfies. @brandonlotti in action on the water filter. #bwca](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13721231_879908758781454_534542354_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BIfdUXTgPZ7/)

Boat selfies. @brandonlotti in action on the water filter. #bwca

47.9637014-91.5469748




* #[bwca](https://dentedreality.com.au/tags/bwca/)

Posted on [Instagram](https://www.instagram.com/p/BIfdUXTgPZ7/) [10:00 am, July 30, 2016](https://dentedreality.com.au/2016/07/30/boat-selfies-brandonlotti-in-action-on-the-water-filter-bwca/ "10:00 am") 
jQuery(document).ready(function(){
var gmap\_m8b4038fae748c94506001f180034af78 = {
positions : {
542 : new google.maps.LatLng( '47.963701444723', '-91.546974778261' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8b4038fae748c94506001f180034af78' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8b4038fae748c94506001f180034af78.positions ) {
gmap\_m8b4038fae748c94506001f180034af78.bounds.extend( gmap\_m8b4038fae748c94506001f180034af78.positions[m] );
}
// Render markers
for ( var m in gmap\_m8b4038fae748c94506001f180034af78.positions ) {
gmap\_m8b4038fae748c94506001f180034af78.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8b4038fae748c94506001f180034af78.map,
position : gmap\_m8b4038fae748c94506001f180034af78.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8b4038fae748c94506001f180034af78.map.setCenter( gmap\_m8b4038fae748c94506001f180034af78.positions[542] );
});