---
title: Republica Dominica
date: '2013-12-27T18:50:29+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
- panorama
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924301653_54016fd1c9_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924301653_54016fd1c9_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/27/republica-dominica-14/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/27/republica-dominica-14/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)
* #[panorama](http://dentedreality.com.au/tags/panorama/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924301653/) [6:50 pm, December 27, 2013](http://dentedreality.com.au/2013/12/27/republica-dominica-14/ "6:50 pm") 
jQuery(document).ready(function(){
var gmap\_mb904ea228d4ea7367c2064eaf93bc3e2 = {
positions : {
220 : new google.maps.LatLng( '19.750466', '-70.408251' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb904ea228d4ea7367c2064eaf93bc3e2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb904ea228d4ea7367c2064eaf93bc3e2.positions ) {
gmap\_mb904ea228d4ea7367c2064eaf93bc3e2.bounds.extend( gmap\_mb904ea228d4ea7367c2064eaf93bc3e2.positions[m] );
}
// Render markers
for ( var m in gmap\_mb904ea228d4ea7367c2064eaf93bc3e2.positions ) {
gmap\_mb904ea228d4ea7367c2064eaf93bc3e2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb904ea228d4ea7367c2064eaf93bc3e2.map,
position : gmap\_mb904ea228d4ea7367c2064eaf93bc3e2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb904ea228d4ea7367c2064eaf93bc3e2.map.setCenter( gmap\_mb904ea228d4ea7367c2064eaf93bc3e2.positions[220] );
});