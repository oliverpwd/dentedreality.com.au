---
title: Poison Oak
date: '2010-04-09T10:25:17+00:00'
format: image
service: flickr
tags:
- poisonoak
- tombrown
- trackerschool
- tracking
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516463496_a3c1af73cf_o.jpg?resize=607%2C455
---

[![Poison Oak](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516463496_a3c1af73cf_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/09/poison-oak/) 
# [Poison Oak](http://dentedreality.com.au/2010/04/09/poison-oak/)

As seen during our edible/medicinal plant walk.





* #[poisonoak](http://dentedreality.com.au/tags/poisonoak/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516463496/) [10:25 am, April 9, 2010](http://dentedreality.com.au/2010/04/09/poison-oak/ "10:25 am") 
jQuery(document).ready(function(){
var gmap\_m69d858a95bb83d9c4b0e79e4407a0732 = {
positions : {
498 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m69d858a95bb83d9c4b0e79e4407a0732' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m69d858a95bb83d9c4b0e79e4407a0732.positions ) {
gmap\_m69d858a95bb83d9c4b0e79e4407a0732.bounds.extend( gmap\_m69d858a95bb83d9c4b0e79e4407a0732.positions[m] );
}
// Render markers
for ( var m in gmap\_m69d858a95bb83d9c4b0e79e4407a0732.positions ) {
gmap\_m69d858a95bb83d9c4b0e79e4407a0732.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m69d858a95bb83d9c4b0e79e4407a0732.map,
position : gmap\_m69d858a95bb83d9c4b0e79e4407a0732.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m69d858a95bb83d9c4b0e79e4407a0732.map.setCenter( gmap\_m69d858a95bb83d9c4b0e79e4407a0732.positions[498] );
});