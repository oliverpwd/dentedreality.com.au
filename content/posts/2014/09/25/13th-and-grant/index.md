---
title: ''
date: '2014-09-25T18:54:40+00:00'
format: image
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10706861_651244088323382_19790079_n.jpg?resize=640%2C640
---

[![13th and Grant.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10706861_651244088323382_19790079_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/09/25/13th-and-grant/) 

13th and Grant.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/tY6uXuCmNR/) [6:54 pm, September 25, 2014](http://dentedreality.com.au/2014/09/25/13th-and-grant/ "6:54 pm") 
jQuery(document).ready(function(){
var gmap\_m5e0008ada91f37d7f2eeade40a2e5a40 = {
positions : {
902 : new google.maps.LatLng( '39.736678333', '-104.983933333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5e0008ada91f37d7f2eeade40a2e5a40' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5e0008ada91f37d7f2eeade40a2e5a40.positions ) {
gmap\_m5e0008ada91f37d7f2eeade40a2e5a40.bounds.extend( gmap\_m5e0008ada91f37d7f2eeade40a2e5a40.positions[m] );
}
// Render markers
for ( var m in gmap\_m5e0008ada91f37d7f2eeade40a2e5a40.positions ) {
gmap\_m5e0008ada91f37d7f2eeade40a2e5a40.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5e0008ada91f37d7f2eeade40a2e5a40.map,
position : gmap\_m5e0008ada91f37d7f2eeade40a2e5a40.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5e0008ada91f37d7f2eeade40a2e5a40.map.setCenter( gmap\_m5e0008ada91f37d7f2eeade40a2e5a40.positions[902] );
});