---
title: ''
date: '2014-11-23T23:36:21+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/10755829_1510758552508626_971635366_n.jpg?resize=640%2C640
---

[![More pretty Colorado.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/10755829_1510758552508626_971635366_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/11/23/more-pretty-colorado/) 

More pretty Colorado.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/vxcuksCmCU/) [11:36 pm, November 23, 2014](http://dentedreality.com.au/2014/11/23/more-pretty-colorado/ "11:36 pm") 
jQuery(document).ready(function(){
var gmap\_m8a0a6bdb4ba3fc53868dc2bc254ff43a = {
positions : {
362 : new google.maps.LatLng( '39.36112', '-105.166938333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8a0a6bdb4ba3fc53868dc2bc254ff43a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8a0a6bdb4ba3fc53868dc2bc254ff43a.positions ) {
gmap\_m8a0a6bdb4ba3fc53868dc2bc254ff43a.bounds.extend( gmap\_m8a0a6bdb4ba3fc53868dc2bc254ff43a.positions[m] );
}
// Render markers
for ( var m in gmap\_m8a0a6bdb4ba3fc53868dc2bc254ff43a.positions ) {
gmap\_m8a0a6bdb4ba3fc53868dc2bc254ff43a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8a0a6bdb4ba3fc53868dc2bc254ff43a.map,
position : gmap\_m8a0a6bdb4ba3fc53868dc2bc254ff43a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8a0a6bdb4ba3fc53868dc2bc254ff43a.map.setCenter( gmap\_m8a0a6bdb4ba3fc53868dc2bc254ff43a.positions[362] );
});