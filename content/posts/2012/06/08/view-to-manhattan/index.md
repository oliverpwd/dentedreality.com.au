---
title: View to Manhattan
date: '2012-06-08T07:36:03+00:00'
format: image
service: flickr
tags:
- brooklyn
- Manhattan
- view
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7911183414_56383dd5f9_o.jpg?resize=607%2C455
---

[![View to Manhattan](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7911183414_56383dd5f9_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2012/06/08/view-to-manhattan/) 
# [View to Manhattan](http://dentedreality.com.au/2012/06/08/view-to-manhattan/)

From the roof of our apartment





* #[brooklyn](http://dentedreality.com.au/tags/brooklyn/)
* #[Manhattan](http://dentedreality.com.au/tags/manhattan/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7911183414/) [7:36 am, June 8, 2012](http://dentedreality.com.au/2012/06/08/view-to-manhattan/ "7:36 am") 
jQuery(document).ready(function(){
var gmap\_m1e4eb3d6ed7278b7108bc123c5b517af = {
positions : {
502 : new google.maps.LatLng( '40.669363', '-73.984984' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1e4eb3d6ed7278b7108bc123c5b517af' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1e4eb3d6ed7278b7108bc123c5b517af.positions ) {
gmap\_m1e4eb3d6ed7278b7108bc123c5b517af.bounds.extend( gmap\_m1e4eb3d6ed7278b7108bc123c5b517af.positions[m] );
}
// Render markers
for ( var m in gmap\_m1e4eb3d6ed7278b7108bc123c5b517af.positions ) {
gmap\_m1e4eb3d6ed7278b7108bc123c5b517af.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1e4eb3d6ed7278b7108bc123c5b517af.map,
position : gmap\_m1e4eb3d6ed7278b7108bc123c5b517af.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1e4eb3d6ed7278b7108bc123c5b517af.map.setCenter( gmap\_m1e4eb3d6ed7278b7108bc123c5b517af.positions[502] );
});