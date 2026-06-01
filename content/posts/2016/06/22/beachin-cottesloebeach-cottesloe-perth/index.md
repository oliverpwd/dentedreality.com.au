---
title: ''
date: '2016-06-22T00:45:18+00:00'
format: image
service: instagram
tags:
- cottesloe
- cottesloebeach
- perth
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13398865_1768904566676265_276815848_n.jpg?fit=640%2C640
---

[![Beachin' #cottesloebeach #cottesloe #perth](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13398865_1768904566676265_276815848_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/06/22/beachin-cottesloebeach-cottesloe-perth/) 

Beachin’ #cottesloebeach #cottesloe #perth





* #[cottesloe](http://dentedreality.com.au/tags/cottesloe/)
* #[cottesloebeach](http://dentedreality.com.au/tags/cottesloebeach/)
* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Instagram](https://www.instagram.com/p/BG8noHLCmDa/) [12:45 am, June 22, 2016](http://dentedreality.com.au/2016/06/22/beachin-cottesloebeach-cottesloe-perth/ "12:45 am") 
jQuery(document).ready(function(){
var gmap\_m87422f3285c87f82652654edad434a5d = {
positions : {
635 : new google.maps.LatLng( '-31.995081929915', '115.75170019926' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m87422f3285c87f82652654edad434a5d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m87422f3285c87f82652654edad434a5d.positions ) {
gmap\_m87422f3285c87f82652654edad434a5d.bounds.extend( gmap\_m87422f3285c87f82652654edad434a5d.positions[m] );
}
// Render markers
for ( var m in gmap\_m87422f3285c87f82652654edad434a5d.positions ) {
gmap\_m87422f3285c87f82652654edad434a5d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m87422f3285c87f82652654edad434a5d.map,
position : gmap\_m87422f3285c87f82652654edad434a5d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m87422f3285c87f82652654edad434a5d.map.setCenter( gmap\_m87422f3285c87f82652654edad434a5d.positions[635] );
});