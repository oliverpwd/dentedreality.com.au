---
title: ''
date: '2017-05-20T18:01:00+00:00'
format: image
service: instagram
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18579686_300846417020039_7193599758672330752_n.jpg?fit=640%2C640
---

[![Anderson Valley Briney Melon Gose](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/05/18579686_300846417020039_7193599758672330752_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2017/05/20/anderson-valley-briney-melon-gose/) 

Anderson Valley Briney Melon Gose





Posted on [Instagram](https://www.instagram.com/p/BUVWER8hYPO/) [6:01 pm, May 20, 2017](https://dentedreality.com.au/2017/05/20/anderson-valley-briney-melon-gose/ "6:01 pm") 
jQuery(document).ready(function(){
var gmap\_m7c4b07114ea616fa2be2c58183423035 = {
positions : {
38 : new google.maps.LatLng( '39.75597', '-104.97679' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7c4b07114ea616fa2be2c58183423035' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7c4b07114ea616fa2be2c58183423035.positions ) {
gmap\_m7c4b07114ea616fa2be2c58183423035.bounds.extend( gmap\_m7c4b07114ea616fa2be2c58183423035.positions[m] );
}
// Render markers
for ( var m in gmap\_m7c4b07114ea616fa2be2c58183423035.positions ) {
gmap\_m7c4b07114ea616fa2be2c58183423035.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7c4b07114ea616fa2be2c58183423035.map,
position : gmap\_m7c4b07114ea616fa2be2c58183423035.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7c4b07114ea616fa2be2c58183423035.map.setCenter( gmap\_m7c4b07114ea616fa2be2c58183423035.positions[38] );
});