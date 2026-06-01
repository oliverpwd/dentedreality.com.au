---
title: ''
date: '2014-07-01T20:20:20+00:00'
format: image
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/07/10514094_310558392436111_588398374_n.jpg?resize=640%2C640
---

[![Zr. King. Killing it!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/07/10514094_310558392436111_588398374_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/07/01/zr-king-killing-it/) 

Zr. King. Killing it!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/p7hTCzCmAd/) [8:20 pm, July 1, 2014](http://dentedreality.com.au/2014/07/01/zr-king-killing-it/ "8:20 pm") 
jQuery(document).ready(function(){
var gmap\_m7155c4b93fc6bd1242735850294a5b36 = {
positions : {
590 : new google.maps.LatLng( '40.7221582', '-73.986756723' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7155c4b93fc6bd1242735850294a5b36' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7155c4b93fc6bd1242735850294a5b36.positions ) {
gmap\_m7155c4b93fc6bd1242735850294a5b36.bounds.extend( gmap\_m7155c4b93fc6bd1242735850294a5b36.positions[m] );
}
// Render markers
for ( var m in gmap\_m7155c4b93fc6bd1242735850294a5b36.positions ) {
gmap\_m7155c4b93fc6bd1242735850294a5b36.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7155c4b93fc6bd1242735850294a5b36.map,
position : gmap\_m7155c4b93fc6bd1242735850294a5b36.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7155c4b93fc6bd1242735850294a5b36.map.setCenter( gmap\_m7155c4b93fc6bd1242735850294a5b36.positions[590] );
});