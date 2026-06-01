---
title: ''
date: '2014-11-09T14:26:09+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/10735329_876165712395540_2039179870_n.jpg?resize=640%2C640
---

[![Bambi doesn't want anyone to have any fun. Growling at 2 other dogs playing fetch.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/10735329_876165712395540_2039179870_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/11/09/bambi-doesnt-want-anyone-to-have-any-fun-growling-at-2-other-dogs-playing-fetch/) 

Bambi doesn’t want anyone to have any fun. Growling at 2 other dogs playing fetch.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/vMaofsCmB-/) [2:26 pm, November 9, 2014](http://dentedreality.com.au/2014/11/09/bambi-doesnt-want-anyone-to-have-any-fun-growling-at-2-other-dogs-playing-fetch/ "2:26 pm") 
jQuery(document).ready(function(){
var gmap\_m0104c9256dfd3e370d284d48473734a9 = {
positions : {
709 : new google.maps.LatLng( '39.8185745', '-105.286428802' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0104c9256dfd3e370d284d48473734a9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0104c9256dfd3e370d284d48473734a9.positions ) {
gmap\_m0104c9256dfd3e370d284d48473734a9.bounds.extend( gmap\_m0104c9256dfd3e370d284d48473734a9.positions[m] );
}
// Render markers
for ( var m in gmap\_m0104c9256dfd3e370d284d48473734a9.positions ) {
gmap\_m0104c9256dfd3e370d284d48473734a9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0104c9256dfd3e370d284d48473734a9.map,
position : gmap\_m0104c9256dfd3e370d284d48473734a9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0104c9256dfd3e370d284d48473734a9.map.setCenter( gmap\_m0104c9256dfd3e370d284d48473734a9.positions[709] );
});