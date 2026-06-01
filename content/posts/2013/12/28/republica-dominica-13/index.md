---
title: Republica Dominica
date: '2013-12-28T10:45:40+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901143612_ef678449a7_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901143612_ef678449a7_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/28/republica-dominica-13/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/28/republica-dominica-13/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901143612/) [10:45 am, December 28, 2013](http://dentedreality.com.au/2013/12/28/republica-dominica-13/ "10:45 am") 
jQuery(document).ready(function(){
var gmap\_m2c1fe325023d267b73a8fafff45c8655 = {
positions : {
136 : new google.maps.LatLng( '19.861036', '-71.658189' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2c1fe325023d267b73a8fafff45c8655' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2c1fe325023d267b73a8fafff45c8655.positions ) {
gmap\_m2c1fe325023d267b73a8fafff45c8655.bounds.extend( gmap\_m2c1fe325023d267b73a8fafff45c8655.positions[m] );
}
// Render markers
for ( var m in gmap\_m2c1fe325023d267b73a8fafff45c8655.positions ) {
gmap\_m2c1fe325023d267b73a8fafff45c8655.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2c1fe325023d267b73a8fafff45c8655.map,
position : gmap\_m2c1fe325023d267b73a8fafff45c8655.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2c1fe325023d267b73a8fafff45c8655.map.setCenter( gmap\_m2c1fe325023d267b73a8fafff45c8655.positions[136] );
});