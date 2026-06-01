---
title: ''
date: '2016-08-07T14:39:19+00:00'
format: image
service: instagram
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13774602_1172320792839599_1250786946_n.jpg?fit=640%2C640
---

[![Early morning ride in Crested Butte before hitting the road.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13774602_1172320792839599_1250786946_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/08/07/early-morning-ride-in-crested-butte-before-hitting-the-road/) 

Early morning ride in Crested Butte before hitting the road.





Posted on [Instagram](https://www.instagram.com/p/BI0jo19gQ9V/) [2:39 pm, August 7, 2016](http://dentedreality.com.au/2016/08/07/early-morning-ride-in-crested-butte-before-hitting-the-road/ "2:39 pm") 
jQuery(document).ready(function(){
var gmap\_m8cfcb7af236d7b34c085b57d09337dd6 = {
positions : {
352 : new google.maps.LatLng( '38.9017', '-106.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8cfcb7af236d7b34c085b57d09337dd6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8cfcb7af236d7b34c085b57d09337dd6.positions ) {
gmap\_m8cfcb7af236d7b34c085b57d09337dd6.bounds.extend( gmap\_m8cfcb7af236d7b34c085b57d09337dd6.positions[m] );
}
// Render markers
for ( var m in gmap\_m8cfcb7af236d7b34c085b57d09337dd6.positions ) {
gmap\_m8cfcb7af236d7b34c085b57d09337dd6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8cfcb7af236d7b34c085b57d09337dd6.map,
position : gmap\_m8cfcb7af236d7b34c085b57d09337dd6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8cfcb7af236d7b34c085b57d09337dd6.map.setCenter( gmap\_m8cfcb7af236d7b34c085b57d09337dd6.positions[352] );
});