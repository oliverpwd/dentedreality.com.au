---
title: ''
date: '2018-06-29T22:30:53-06:00'
format: image
service: instagram
tags:
- fjallravenclassicusa
latitude: '39.4585981'
longitude: '-106.2278022'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182136/36085550_204097630311077_1882737276849487872_n.jpg?resize=607%2C607&ssl=1
---

[![@michaelarestad demonstrating how to use @thegrayl during #fjallravenclassicusa. This thing is a super convenient way to filter on the trail.](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182136/36085550_204097630311077_1882737276849487872_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/06/29/michaelarestad-demonstrating-how-to-use-thegrayl-during-fjallravenclassicusa-this-thing-is-a-super-convenient-way-to-filter-on-the-trail/) 

[![@michaelarestad demonstrating how to use @thegrayl during #fjallravenclassicusa. This thing is a super convenient way to filter on the trail.](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/06/14182136/36085550_204097630311077_1882737276849487872_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/Bkoq5Sylnme/)

@michaelarestad demonstrating how to use @thegrayl during #fjallravenclassicusa. This thing is a super convenient way to filter on the trail.

39.4585981-106.2278022




* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/Bkoq5Sylnme/) [10:30 pm, June 29, 2018](https://dentedreality.com.au/2018/06/29/michaelarestad-demonstrating-how-to-use-thegrayl-during-fjallravenclassicusa-this-thing-is-a-super-convenient-way-to-filter-on-the-trail/ "10:30 pm") 
jQuery(document).ready(function(){
var gmap\_m3c28e61547724b2a3010fb2d9a08607d = {
positions : {
502 : new google.maps.LatLng( '39.4585981', '-106.2278022' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3c28e61547724b2a3010fb2d9a08607d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3c28e61547724b2a3010fb2d9a08607d.positions ) {
gmap\_m3c28e61547724b2a3010fb2d9a08607d.bounds.extend( gmap\_m3c28e61547724b2a3010fb2d9a08607d.positions[m] );
}
// Render markers
for ( var m in gmap\_m3c28e61547724b2a3010fb2d9a08607d.positions ) {
gmap\_m3c28e61547724b2a3010fb2d9a08607d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3c28e61547724b2a3010fb2d9a08607d.map,
position : gmap\_m3c28e61547724b2a3010fb2d9a08607d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3c28e61547724b2a3010fb2d9a08607d.map.setCenter( gmap\_m3c28e61547724b2a3010fb2d9a08607d.positions[502] );
});