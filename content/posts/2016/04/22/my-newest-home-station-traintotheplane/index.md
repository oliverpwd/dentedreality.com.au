---
title: ''
date: '2016-04-22T16:55:24+00:00'
format: image
service: instagram
tags:
- traintotheplane
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/04/12930954_1531362767173145_684978334_n.jpg?fit=640%2C640
---

[![My newest home station #traintotheplane](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/04/12930954_1531362767173145_684978334_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/04/22/my-newest-home-station-traintotheplane/) 

My newest home station #traintotheplane





* #[traintotheplane](http://dentedreality.com.au/tags/traintotheplane/)

Posted on [Instagram](https://www.instagram.com/p/BEhSJ-ximKf/) [4:55 pm, April 22, 2016](http://dentedreality.com.au/2016/04/22/my-newest-home-station-traintotheplane/ "4:55 pm") 
jQuery(document).ready(function(){
var gmap\_m8e5da33072eadf033168d2cfab8200db = {
positions : {
623 : new google.maps.LatLng( '39.7702581', '-104.97382942' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8e5da33072eadf033168d2cfab8200db' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8e5da33072eadf033168d2cfab8200db.positions ) {
gmap\_m8e5da33072eadf033168d2cfab8200db.bounds.extend( gmap\_m8e5da33072eadf033168d2cfab8200db.positions[m] );
}
// Render markers
for ( var m in gmap\_m8e5da33072eadf033168d2cfab8200db.positions ) {
gmap\_m8e5da33072eadf033168d2cfab8200db.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8e5da33072eadf033168d2cfab8200db.map,
position : gmap\_m8e5da33072eadf033168d2cfab8200db.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8e5da33072eadf033168d2cfab8200db.map.setCenter( gmap\_m8e5da33072eadf033168d2cfab8200db.positions[623] );
});