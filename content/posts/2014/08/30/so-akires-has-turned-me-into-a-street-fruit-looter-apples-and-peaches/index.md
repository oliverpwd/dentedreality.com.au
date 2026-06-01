---
title: ''
date: '2014-08-30T19:16:39+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/08/10655083_693278787415328_1832626606_n.jpg?resize=640%2C640
---

[![So @akires has turned me into a street fruit looter (apples and peaches!)](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/08/10655083_693278787415328_1832626606_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/08/30/so-akires-has-turned-me-into-a-street-fruit-looter-apples-and-peaches/) 

So @akires has turned me into a street fruit looter (apples and peaches!)





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/sWAkkTCmCh/) [7:16 pm, August 30, 2014](http://dentedreality.com.au/2014/08/30/so-akires-has-turned-me-into-a-street-fruit-looter-apples-and-peaches/ "7:16 pm") 
jQuery(document).ready(function(){
var gmap\_m4a4cc9dda24a623a79f0da9a190d06c6 = {
positions : {
419 : new google.maps.LatLng( '39.734836667', '-104.978395' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4a4cc9dda24a623a79f0da9a190d06c6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4a4cc9dda24a623a79f0da9a190d06c6.positions ) {
gmap\_m4a4cc9dda24a623a79f0da9a190d06c6.bounds.extend( gmap\_m4a4cc9dda24a623a79f0da9a190d06c6.positions[m] );
}
// Render markers
for ( var m in gmap\_m4a4cc9dda24a623a79f0da9a190d06c6.positions ) {
gmap\_m4a4cc9dda24a623a79f0da9a190d06c6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4a4cc9dda24a623a79f0da9a190d06c6.map,
position : gmap\_m4a4cc9dda24a623a79f0da9a190d06c6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4a4cc9dda24a623a79f0da9a190d06c6.map.setCenter( gmap\_m4a4cc9dda24a623a79f0da9a190d06c6.positions[419] );
});