---
title: ''
date: '2014-08-01T13:56:09+00:00'
format: image
service: instagram
tags:
- burritofriday
- dvlpdnvr
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/08/10584822_561176890672518_1603921645_n.jpg?resize=640%2C640
---

[![#burritofriday during #dvlpdnvr. Awesome.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/08/10584822_561176890672518_1603921645_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/08/01/burritofriday-during-dvlpdnvr-awesome-2/) 

#burritofriday during #dvlpdnvr. Awesome.





* #[burritofriday](http://dentedreality.com.au/tags/burritofriday/)
* #[dvlpdnvr](http://dentedreality.com.au/tags/dvlpdnvr/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/rKp-VjimNh/) [1:56 pm, August 1, 2014](http://dentedreality.com.au/2014/08/01/burritofriday-during-dvlpdnvr-awesome-2/ "1:56 pm") 
jQuery(document).ready(function(){
var gmap\_m958215233a40f936ac56189dd804b58e = {
positions : {
847 : new google.maps.LatLng( '39.740070001', '-104.980883185' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m958215233a40f936ac56189dd804b58e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m958215233a40f936ac56189dd804b58e.positions ) {
gmap\_m958215233a40f936ac56189dd804b58e.bounds.extend( gmap\_m958215233a40f936ac56189dd804b58e.positions[m] );
}
// Render markers
for ( var m in gmap\_m958215233a40f936ac56189dd804b58e.positions ) {
gmap\_m958215233a40f936ac56189dd804b58e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m958215233a40f936ac56189dd804b58e.map,
position : gmap\_m958215233a40f936ac56189dd804b58e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m958215233a40f936ac56189dd804b58e.map.setCenter( gmap\_m958215233a40f936ac56189dd804b58e.positions[847] );
});