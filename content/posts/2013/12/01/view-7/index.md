---
title: View
date: '2013-12-01T08:17:11+00:00'
format: image
service: flickr
tags:
- france
- paris
- triomphe
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900352811_e2504d0201_o.jpg?fit=1500%2C1500
---

[![View](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900352811_e2504d0201_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/01/view-7/) 
# [View](http://dentedreality.com.au/2013/12/01/view-7/)

From the Arc de Triomphe





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)
* #[triomphe](http://dentedreality.com.au/tags/triomphe/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900352811/) [8:17 am, December 1, 2013](http://dentedreality.com.au/2013/12/01/view-7/ "8:17 am") 
jQuery(document).ready(function(){
var gmap\_me7c8cf4655c447f9d676c09f8321ce4b = {
positions : {
435 : new google.maps.LatLng( '48.873969', '2.294899' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me7c8cf4655c447f9d676c09f8321ce4b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me7c8cf4655c447f9d676c09f8321ce4b.positions ) {
gmap\_me7c8cf4655c447f9d676c09f8321ce4b.bounds.extend( gmap\_me7c8cf4655c447f9d676c09f8321ce4b.positions[m] );
}
// Render markers
for ( var m in gmap\_me7c8cf4655c447f9d676c09f8321ce4b.positions ) {
gmap\_me7c8cf4655c447f9d676c09f8321ce4b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me7c8cf4655c447f9d676c09f8321ce4b.map,
position : gmap\_me7c8cf4655c447f9d676c09f8321ce4b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me7c8cf4655c447f9d676c09f8321ce4b.map.setCenter( gmap\_me7c8cf4655c447f9d676c09f8321ce4b.positions[435] );
});