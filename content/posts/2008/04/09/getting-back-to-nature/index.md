---
title: Getting Back to Nature
date: '2008-04-09T17:51:49+00:00'
format: image
service: flickr
tags:
- australia
- beau
- beaulebens
- botanicalgardens
- me
- sydney
- tree
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2437453346_060c1c3a3b_o.jpg?resize=607%2C808
---

[![Getting Back to Nature](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2437453346_060c1c3a3b_o.jpg?resize=607%2C808)](http://dentedreality.com.au/2008/04/09/getting-back-to-nature/) 
# [Getting Back to Nature](http://dentedreality.com.au/2008/04/09/getting-back-to-nature/)

In the Sydney Botanical Gardens





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[botanicalgardens](http://dentedreality.com.au/tags/botanicalgardens/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[sydney](http://dentedreality.com.au/tags/sydney/)
* #[tree](http://dentedreality.com.au/tags/tree/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2437453346/) [5:51 pm, April 9, 2008](http://dentedreality.com.au/2008/04/09/getting-back-to-nature/ "5:51 pm") 
jQuery(document).ready(function(){
var gmap\_m88cfe4c45eeec3532eb76452bf67e58d = {
positions : {
100 : new google.maps.LatLng( '-33.871555', '151.226291' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m88cfe4c45eeec3532eb76452bf67e58d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m88cfe4c45eeec3532eb76452bf67e58d.positions ) {
gmap\_m88cfe4c45eeec3532eb76452bf67e58d.bounds.extend( gmap\_m88cfe4c45eeec3532eb76452bf67e58d.positions[m] );
}
// Render markers
for ( var m in gmap\_m88cfe4c45eeec3532eb76452bf67e58d.positions ) {
gmap\_m88cfe4c45eeec3532eb76452bf67e58d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m88cfe4c45eeec3532eb76452bf67e58d.map,
position : gmap\_m88cfe4c45eeec3532eb76452bf67e58d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m88cfe4c45eeec3532eb76452bf67e58d.map.setCenter( gmap\_m88cfe4c45eeec3532eb76452bf67e58d.positions[100] );
});