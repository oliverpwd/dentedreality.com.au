---
title: Train Selfie
date: '2013-11-30T16:08:14+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- france
- me
- paris
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13923921654_3936822383_o.jpg?fit=1500%2C1500
---

[![Train Selfie](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13923921654_3936822383_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/11/30/train-selfie/) 
# [Train Selfie](http://dentedreality.com.au/2013/11/30/train-selfie/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[france](http://dentedreality.com.au/tags/france/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13923921654/) [4:08 pm, November 30, 2013](http://dentedreality.com.au/2013/11/30/train-selfie/ "4:08 pm") 
jQuery(document).ready(function(){
var gmap\_mfae6a3c3802dfa471e8582a138ac64e2 = {
positions : {
31 : new google.maps.LatLng( '48.874458', '2.340294' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mfae6a3c3802dfa471e8582a138ac64e2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mfae6a3c3802dfa471e8582a138ac64e2.positions ) {
gmap\_mfae6a3c3802dfa471e8582a138ac64e2.bounds.extend( gmap\_mfae6a3c3802dfa471e8582a138ac64e2.positions[m] );
}
// Render markers
for ( var m in gmap\_mfae6a3c3802dfa471e8582a138ac64e2.positions ) {
gmap\_mfae6a3c3802dfa471e8582a138ac64e2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mfae6a3c3802dfa471e8582a138ac64e2.map,
position : gmap\_mfae6a3c3802dfa471e8582a138ac64e2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mfae6a3c3802dfa471e8582a138ac64e2.map.setCenter( gmap\_mfae6a3c3802dfa471e8582a138ac64e2.positions[31] );
});