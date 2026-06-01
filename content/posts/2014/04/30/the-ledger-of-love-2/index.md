---
title: ''
date: '2014-04-30T15:40:13+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/10254139_777079515659709_531464689_n.jpg?resize=640%2C640
---

[![The Ledger of Love](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/10254139_777079515659709_531464689_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/04/30/the-ledger-of-love-2/) 

The Ledger of Love





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/nbX9KeCmF9/) [3:40 pm, April 30, 2014](http://dentedreality.com.au/2014/04/30/the-ledger-of-love-2/ "3:40 pm") 
jQuery(document).ready(function(){
var gmap\_mc82babae25d142a67f2944d8123baa96 = {
positions : {
760 : new google.maps.LatLng( '53.343236849', '-6.263744981' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc82babae25d142a67f2944d8123baa96' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc82babae25d142a67f2944d8123baa96.positions ) {
gmap\_mc82babae25d142a67f2944d8123baa96.bounds.extend( gmap\_mc82babae25d142a67f2944d8123baa96.positions[m] );
}
// Render markers
for ( var m in gmap\_mc82babae25d142a67f2944d8123baa96.positions ) {
gmap\_mc82babae25d142a67f2944d8123baa96.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc82babae25d142a67f2944d8123baa96.map,
position : gmap\_mc82babae25d142a67f2944d8123baa96.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc82babae25d142a67f2944d8123baa96.map.setCenter( gmap\_mc82babae25d142a67f2944d8123baa96.positions[760] );
});