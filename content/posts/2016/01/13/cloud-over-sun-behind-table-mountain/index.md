---
title: ''
date: '2016-01-13T22:11:44+00:00'
format: image
service: instagram
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/01/12530739_669656253137653_990301284_n.jpg?resize=607%2C607
---

[![Cloud over, sun behind, Table Mountain](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/01/12530739_669656253137653_990301284_n.jpg?resize=607%2C607)](http://dentedreality.com.au/2016/01/13/cloud-over-sun-behind-table-mountain/) 

Cloud over, sun behind, Table Mountain





Posted on [Instagram](https://www.instagram.com/p/BAgduzeimAM/) [10:11 pm, January 13, 2016](http://dentedreality.com.au/2016/01/13/cloud-over-sun-behind-table-mountain/ "10:11 pm") 
jQuery(document).ready(function(){
var gmap\_m19e49ced69afd01f74022ac06723fa8b = {
positions : {
629 : new google.maps.LatLng( '-33.927485885', '18.457789727' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m19e49ced69afd01f74022ac06723fa8b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m19e49ced69afd01f74022ac06723fa8b.positions ) {
gmap\_m19e49ced69afd01f74022ac06723fa8b.bounds.extend( gmap\_m19e49ced69afd01f74022ac06723fa8b.positions[m] );
}
// Render markers
for ( var m in gmap\_m19e49ced69afd01f74022ac06723fa8b.positions ) {
gmap\_m19e49ced69afd01f74022ac06723fa8b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m19e49ced69afd01f74022ac06723fa8b.map,
position : gmap\_m19e49ced69afd01f74022ac06723fa8b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m19e49ced69afd01f74022ac06723fa8b.map.setCenter( gmap\_m19e49ced69afd01f74022ac06723fa8b.positions[629] );
});