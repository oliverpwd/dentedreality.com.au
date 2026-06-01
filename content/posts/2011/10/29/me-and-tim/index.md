---
title: Me and Tim
date: '2011-10-29T10:47:13+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- me
- norway
- Oslo
- tim
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812168954_3181aa7d8b_o.jpg?resize=607%2C452
---

[![Me and Tim](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812168954_3181aa7d8b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/10/29/me-and-tim/) 
# [Me and Tim](http://dentedreality.com.au/2011/10/29/me-and-tim/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[norway](http://dentedreality.com.au/tags/norway/)
* #[Oslo](http://dentedreality.com.au/tags/oslo/)
* #[tim](http://dentedreality.com.au/tags/tim/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812168954/) [10:47 am, October 29, 2011](http://dentedreality.com.au/2011/10/29/me-and-tim/ "10:47 am") 
jQuery(document).ready(function(){
var gmap\_mae4e173d5e6aec6498c59ccf1c97a38b = {
positions : {
250 : new google.maps.LatLng( '59.9605', '10.666833' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mae4e173d5e6aec6498c59ccf1c97a38b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mae4e173d5e6aec6498c59ccf1c97a38b.positions ) {
gmap\_mae4e173d5e6aec6498c59ccf1c97a38b.bounds.extend( gmap\_mae4e173d5e6aec6498c59ccf1c97a38b.positions[m] );
}
// Render markers
for ( var m in gmap\_mae4e173d5e6aec6498c59ccf1c97a38b.positions ) {
gmap\_mae4e173d5e6aec6498c59ccf1c97a38b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mae4e173d5e6aec6498c59ccf1c97a38b.map,
position : gmap\_mae4e173d5e6aec6498c59ccf1c97a38b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mae4e173d5e6aec6498c59ccf1c97a38b.map.setCenter( gmap\_mae4e173d5e6aec6498c59ccf1c97a38b.positions[250] );
});