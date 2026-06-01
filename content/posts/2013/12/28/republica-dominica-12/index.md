---
title: Republica Dominica
date: '2013-12-28T10:46:01+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- dominicanrepublic
- me
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901144582_671be5f0a4_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901144582_671be5f0a4_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/28/republica-dominica-12/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/28/republica-dominica-12/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)
* #[me](http://dentedreality.com.au/tags/me/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901144582/) [10:46 am, December 28, 2013](http://dentedreality.com.au/2013/12/28/republica-dominica-12/ "10:46 am") 
jQuery(document).ready(function(){
var gmap\_m626bb450d8e632e35f45f164e9370a05 = {
positions : {
457 : new google.maps.LatLng( '19.861411', '-71.657823' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m626bb450d8e632e35f45f164e9370a05' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m626bb450d8e632e35f45f164e9370a05.positions ) {
gmap\_m626bb450d8e632e35f45f164e9370a05.bounds.extend( gmap\_m626bb450d8e632e35f45f164e9370a05.positions[m] );
}
// Render markers
for ( var m in gmap\_m626bb450d8e632e35f45f164e9370a05.positions ) {
gmap\_m626bb450d8e632e35f45f164e9370a05.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m626bb450d8e632e35f45f164e9370a05.map,
position : gmap\_m626bb450d8e632e35f45f164e9370a05.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m626bb450d8e632e35f45f164e9370a05.map.setCenter( gmap\_m626bb450d8e632e35f45f164e9370a05.positions[457] );
});