---
title: The Ceremony
date: '2008-04-04T20:28:32+00:00'
format: image
service: flickr
tags:
- australia
- ceremony
- renniewedding
- timswedding
- westernaustraliadenmark
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433427510_eceb08340c_o.jpg?resize=607%2C808
---

[![The Ceremony](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433427510_eceb08340c_o.jpg?resize=607%2C808)](http://dentedreality.com.au/2008/04/04/the-ceremony/) 
# [The Ceremony](http://dentedreality.com.au/2008/04/04/the-ceremony/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[ceremony](http://dentedreality.com.au/tags/ceremony/)
* #[renniewedding](http://dentedreality.com.au/tags/renniewedding/)
* #[timswedding](http://dentedreality.com.au/tags/timswedding/)
* #[westernaustraliadenmark](http://dentedreality.com.au/tags/westernaustraliadenmark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2433427510/) [8:28 pm, April 4, 2008](http://dentedreality.com.au/2008/04/04/the-ceremony/ "8:28 pm") 
jQuery(document).ready(function(){
var gmap\_mdc51d5589e5e0014a29a198b2ed6a7ca = {
positions : {
602 : new google.maps.LatLng( '-35.03604', '117.329177' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdc51d5589e5e0014a29a198b2ed6a7ca' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdc51d5589e5e0014a29a198b2ed6a7ca.positions ) {
gmap\_mdc51d5589e5e0014a29a198b2ed6a7ca.bounds.extend( gmap\_mdc51d5589e5e0014a29a198b2ed6a7ca.positions[m] );
}
// Render markers
for ( var m in gmap\_mdc51d5589e5e0014a29a198b2ed6a7ca.positions ) {
gmap\_mdc51d5589e5e0014a29a198b2ed6a7ca.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdc51d5589e5e0014a29a198b2ed6a7ca.map,
position : gmap\_mdc51d5589e5e0014a29a198b2ed6a7ca.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdc51d5589e5e0014a29a198b2ed6a7ca.map.setCenter( gmap\_mdc51d5589e5e0014a29a198b2ed6a7ca.positions[602] );
});