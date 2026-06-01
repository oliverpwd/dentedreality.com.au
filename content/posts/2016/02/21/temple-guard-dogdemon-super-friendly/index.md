---
title: ''
date: '2016-02-21T08:09:20+00:00'
format: image
service: instagram
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/02/12747635_562215990620829_1909401419_n.jpg?fit=640%2C640
---

[![Temple Guard Dog/Demon. Super friendly.](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/02/12747635_562215990620829_1909401419_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/02/21/temple-guard-dogdemon-super-friendly/) 

Temple Guard Dog/Demon. Super friendly.





Posted on [Instagram](https://www.instagram.com/p/BCDYU8mCmB3/) [8:09 am, February 21, 2016](http://dentedreality.com.au/2016/02/21/temple-guard-dogdemon-super-friendly/ "8:09 am") 
jQuery(document).ready(function(){
var gmap\_m6958f335bc4859d03095001a0efc54b0 = {
positions : {
618 : new google.maps.LatLng( '-12.096739259', '-77.040403152' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6958f335bc4859d03095001a0efc54b0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6958f335bc4859d03095001a0efc54b0.positions ) {
gmap\_m6958f335bc4859d03095001a0efc54b0.bounds.extend( gmap\_m6958f335bc4859d03095001a0efc54b0.positions[m] );
}
// Render markers
for ( var m in gmap\_m6958f335bc4859d03095001a0efc54b0.positions ) {
gmap\_m6958f335bc4859d03095001a0efc54b0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6958f335bc4859d03095001a0efc54b0.map,
position : gmap\_m6958f335bc4859d03095001a0efc54b0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6958f335bc4859d03095001a0efc54b0.map.setCenter( gmap\_m6958f335bc4859d03095001a0efc54b0.positions[618] );
});