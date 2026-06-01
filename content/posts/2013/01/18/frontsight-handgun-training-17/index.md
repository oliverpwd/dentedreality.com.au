---
title: Frontsight Handgun Training
date: '2013-01-18T12:11:08+00:00'
format: image
service: flickr
tags:
- frontsight
- gun
- gunrange
- handgun
- pistol
- shooting
- training
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/01/8460184982_88ed1e88d4_o.jpg?resize=607%2C813
---

[![Frontsight Handgun Training](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/01/8460184982_88ed1e88d4_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2013/01/18/frontsight-handgun-training-17/) 
# [Frontsight Handgun Training](http://dentedreality.com.au/2013/01/18/frontsight-handgun-training-17/)





* #[frontsight](http://dentedreality.com.au/tags/frontsight/)
* #[gun](http://dentedreality.com.au/tags/gun/)
* #[gunrange](http://dentedreality.com.au/tags/gunrange/)
* #[handgun](http://dentedreality.com.au/tags/handgun/)
* #[pistol](http://dentedreality.com.au/tags/pistol/)
* #[shooting](http://dentedreality.com.au/tags/shooting/)
* #[training](http://dentedreality.com.au/tags/training/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460184982/) [12:11 pm, January 18, 2013](http://dentedreality.com.au/2013/01/18/frontsight-handgun-training-17/ "12:11 pm") 
jQuery(document).ready(function(){
var gmap\_mbbb0945afe4625d21ae3053e0abbef73 = {
positions : {
397 : new google.maps.LatLng( '36.031333', '-115.883334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbbb0945afe4625d21ae3053e0abbef73' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbbb0945afe4625d21ae3053e0abbef73.positions ) {
gmap\_mbbb0945afe4625d21ae3053e0abbef73.bounds.extend( gmap\_mbbb0945afe4625d21ae3053e0abbef73.positions[m] );
}
// Render markers
for ( var m in gmap\_mbbb0945afe4625d21ae3053e0abbef73.positions ) {
gmap\_mbbb0945afe4625d21ae3053e0abbef73.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbbb0945afe4625d21ae3053e0abbef73.map,
position : gmap\_mbbb0945afe4625d21ae3053e0abbef73.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbbb0945afe4625d21ae3053e0abbef73.map.setCenter( gmap\_mbbb0945afe4625d21ae3053e0abbef73.positions[397] );
});