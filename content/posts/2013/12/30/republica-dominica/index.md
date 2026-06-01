---
title: Republica Dominica
date: '2013-12-30T13:34:09+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924262145_128b7e10a7_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924262145_128b7e10a7_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/30/republica-dominica/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/30/republica-dominica/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924262145/) [1:34 pm, December 30, 2013](http://dentedreality.com.au/2013/12/30/republica-dominica/ "1:34 pm") 
jQuery(document).ready(function(){
var gmap\_md201a7c13c96ea6555bf0c7c38b9d125 = {
positions : {
515 : new google.maps.LatLng( '19.088013', '-70.641992' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md201a7c13c96ea6555bf0c7c38b9d125' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md201a7c13c96ea6555bf0c7c38b9d125.positions ) {
gmap\_md201a7c13c96ea6555bf0c7c38b9d125.bounds.extend( gmap\_md201a7c13c96ea6555bf0c7c38b9d125.positions[m] );
}
// Render markers
for ( var m in gmap\_md201a7c13c96ea6555bf0c7c38b9d125.positions ) {
gmap\_md201a7c13c96ea6555bf0c7c38b9d125.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md201a7c13c96ea6555bf0c7c38b9d125.map,
position : gmap\_md201a7c13c96ea6555bf0c7c38b9d125.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md201a7c13c96ea6555bf0c7c38b9d125.map.setCenter( gmap\_md201a7c13c96ea6555bf0c7c38b9d125.positions[515] );
});