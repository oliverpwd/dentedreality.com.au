---
title: Republica Dominica
date: '2013-12-30T12:52:15+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
- panorama
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901135011_7f268c6cd4_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901135011_7f268c6cd4_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/30/republica-dominica-2/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/30/republica-dominica-2/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)
* #[panorama](http://dentedreality.com.au/tags/panorama/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901135011/) [12:52 pm, December 30, 2013](http://dentedreality.com.au/2013/12/30/republica-dominica-2/ "12:52 pm") 
jQuery(document).ready(function(){
var gmap\_ma2bb55c68cc133ada10abd7f1d44c7e2 = {
positions : {
566 : new google.maps.LatLng( '19.087972', '-70.642023' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma2bb55c68cc133ada10abd7f1d44c7e2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma2bb55c68cc133ada10abd7f1d44c7e2.positions ) {
gmap\_ma2bb55c68cc133ada10abd7f1d44c7e2.bounds.extend( gmap\_ma2bb55c68cc133ada10abd7f1d44c7e2.positions[m] );
}
// Render markers
for ( var m in gmap\_ma2bb55c68cc133ada10abd7f1d44c7e2.positions ) {
gmap\_ma2bb55c68cc133ada10abd7f1d44c7e2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma2bb55c68cc133ada10abd7f1d44c7e2.map,
position : gmap\_ma2bb55c68cc133ada10abd7f1d44c7e2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma2bb55c68cc133ada10abd7f1d44c7e2.map.setCenter( gmap\_ma2bb55c68cc133ada10abd7f1d44c7e2.positions[566] );
});