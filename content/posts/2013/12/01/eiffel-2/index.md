---
title: Eiffel
date: '2013-12-01T09:11:27+00:00'
format: image
service: flickr
tags:
- eiffel
- france
- paris
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900379482_935dda6a8e_o.jpg?fit=1500%2C1500
---

[![Eiffel](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900379482_935dda6a8e_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/01/eiffel-2/) 
# [Eiffel](http://dentedreality.com.au/2013/12/01/eiffel-2/)





* #[eiffel](http://dentedreality.com.au/tags/eiffel/)
* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900379482/) [9:11 am, December 1, 2013](http://dentedreality.com.au/2013/12/01/eiffel-2/ "9:11 am") 
jQuery(document).ready(function(){
var gmap\_mff4b3d5172b80be23189f0d6f4661f09 = {
positions : {
602 : new google.maps.LatLng( '48.859016', '2.292802' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mff4b3d5172b80be23189f0d6f4661f09' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mff4b3d5172b80be23189f0d6f4661f09.positions ) {
gmap\_mff4b3d5172b80be23189f0d6f4661f09.bounds.extend( gmap\_mff4b3d5172b80be23189f0d6f4661f09.positions[m] );
}
// Render markers
for ( var m in gmap\_mff4b3d5172b80be23189f0d6f4661f09.positions ) {
gmap\_mff4b3d5172b80be23189f0d6f4661f09.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mff4b3d5172b80be23189f0d6f4661f09.map,
position : gmap\_mff4b3d5172b80be23189f0d6f4661f09.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mff4b3d5172b80be23189f0d6f4661f09.map.setCenter( gmap\_mff4b3d5172b80be23189f0d6f4661f09.positions[602] );
});