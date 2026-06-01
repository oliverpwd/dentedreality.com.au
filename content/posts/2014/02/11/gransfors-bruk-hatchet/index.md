---
title: Gransfors Bruk Hatchet
date: '2014-02-11T15:27:34+00:00'
format: image
service: flickr
tags:
- axe
- gransforsbruk
- hatchet
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13903827121_89194342d6_o.jpg?fit=1500%2C1500
---

[![Gransfors Bruk Hatchet](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/02/13903827121_89194342d6_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/02/11/gransfors-bruk-hatchet/) 
# [Gransfors Bruk Hatchet](http://dentedreality.com.au/2014/02/11/gransfors-bruk-hatchet/)

Modified to add the red highlight on the handle (Plasti-dip).





* #[axe](http://dentedreality.com.au/tags/axe/)
* #[gransforsbruk](http://dentedreality.com.au/tags/gransforsbruk/)
* #[hatchet](http://dentedreality.com.au/tags/hatchet/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13903827121/) [3:27 pm, February 11, 2014](http://dentedreality.com.au/2014/02/11/gransfors-bruk-hatchet/ "3:27 pm") 
jQuery(document).ready(function(){
var gmap\_ma1426638e7ca4960e3dffb6c8e66a52c = {
positions : {
945 : new google.maps.LatLng( '40.669433', '-73.984948' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma1426638e7ca4960e3dffb6c8e66a52c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma1426638e7ca4960e3dffb6c8e66a52c.positions ) {
gmap\_ma1426638e7ca4960e3dffb6c8e66a52c.bounds.extend( gmap\_ma1426638e7ca4960e3dffb6c8e66a52c.positions[m] );
}
// Render markers
for ( var m in gmap\_ma1426638e7ca4960e3dffb6c8e66a52c.positions ) {
gmap\_ma1426638e7ca4960e3dffb6c8e66a52c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma1426638e7ca4960e3dffb6c8e66a52c.map,
position : gmap\_ma1426638e7ca4960e3dffb6c8e66a52c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma1426638e7ca4960e3dffb6c8e66a52c.map.setCenter( gmap\_ma1426638e7ca4960e3dffb6c8e66a52c.positions[945] );
});