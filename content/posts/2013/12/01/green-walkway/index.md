---
title: Green Walkway
date: '2013-12-01T09:21:15+00:00'
format: image
service: flickr
tags:
- france
- paris
- trees
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923930284_33137ac1f4_o.jpg?fit=1500%2C1500
---

[![Green Walkway](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13923930284_33137ac1f4_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/01/green-walkway/) 
# [Green Walkway](http://dentedreality.com.au/2013/12/01/green-walkway/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)
* #[trees](http://dentedreality.com.au/tags/trees/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13923930284/) [9:21 am, December 1, 2013](http://dentedreality.com.au/2013/12/01/green-walkway/ "9:21 am") 
jQuery(document).ready(function(){
var gmap\_m20ffe1dc8d4b8beb1324187397c71a32 = {
positions : {
689 : new google.maps.LatLng( '48.858294', '2.2962' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m20ffe1dc8d4b8beb1324187397c71a32' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m20ffe1dc8d4b8beb1324187397c71a32.positions ) {
gmap\_m20ffe1dc8d4b8beb1324187397c71a32.bounds.extend( gmap\_m20ffe1dc8d4b8beb1324187397c71a32.positions[m] );
}
// Render markers
for ( var m in gmap\_m20ffe1dc8d4b8beb1324187397c71a32.positions ) {
gmap\_m20ffe1dc8d4b8beb1324187397c71a32.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m20ffe1dc8d4b8beb1324187397c71a32.map,
position : gmap\_m20ffe1dc8d4b8beb1324187397c71a32.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m20ffe1dc8d4b8beb1324187397c71a32.map.setCenter( gmap\_m20ffe1dc8d4b8beb1324187397c71a32.positions[689] );
});