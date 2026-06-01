---
title: Bow drill
date: '2011-12-11T10:17:07+00:00'
format: image
service: flickr
tags:
- camping
- disaster
- outdoors
- survival
- wilderness
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6812216448_19a229e821_o.jpg?resize=607%2C452
---

[![Bow drill](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6812216448_19a229e821_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/12/11/bow-drill/) 
# [Bow drill](http://dentedreality.com.au/2011/12/11/bow-drill/)

The remnants of starting a fire with my bow drill.





* #[camping](http://dentedreality.com.au/tags/camping/)
* #[disaster](http://dentedreality.com.au/tags/disaster/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[survival](http://dentedreality.com.au/tags/survival/)
* #[wilderness](http://dentedreality.com.au/tags/wilderness/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812216448/) [10:17 am, December 11, 2011](http://dentedreality.com.au/2011/12/11/bow-drill/ "10:17 am") 
jQuery(document).ready(function(){
var gmap\_m08d14af93488a4f851e5731af0feabc6 = {
positions : {
447 : new google.maps.LatLng( '37.967333', '-122.555' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m08d14af93488a4f851e5731af0feabc6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m08d14af93488a4f851e5731af0feabc6.positions ) {
gmap\_m08d14af93488a4f851e5731af0feabc6.bounds.extend( gmap\_m08d14af93488a4f851e5731af0feabc6.positions[m] );
}
// Render markers
for ( var m in gmap\_m08d14af93488a4f851e5731af0feabc6.positions ) {
gmap\_m08d14af93488a4f851e5731af0feabc6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m08d14af93488a4f851e5731af0feabc6.map,
position : gmap\_m08d14af93488a4f851e5731af0feabc6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m08d14af93488a4f851e5731af0feabc6.map.setCenter( gmap\_m08d14af93488a4f851e5731af0feabc6.positions[447] );
});