---
title: ''
date: '2016-06-28T17:07:02+00:00'
format: image
service: instagram
tags:
- perth
- westernaustralia
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13549612_539483556176772_986444862_n.jpg?fit=640%2C640&ssl=1
---

[![#perth #westernaustralia](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13549612_539483556176772_986444862_n.jpg?fit=640%2C640&ssl=1)](http://dentedreality.com.au/2016/06/28/perth-westernaustralia/) 

#perth #westernaustralia





* #[perth](http://dentedreality.com.au/tags/perth/)
* #[westernaustralia](http://dentedreality.com.au/tags/westernaustralia/)

Posted on [Instagram](https://www.instagram.com/p/BHN0vzqAK9W/) [5:07 pm, June 28, 2016](http://dentedreality.com.au/2016/06/28/perth-westernaustralia/ "5:07 pm") 
jQuery(document).ready(function(){
var gmap\_m0bb7187fdf7a637319e1b06983412ca6 = {
positions : {
77 : new google.maps.LatLng( '-31.9522', '115.859' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0bb7187fdf7a637319e1b06983412ca6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0bb7187fdf7a637319e1b06983412ca6.positions ) {
gmap\_m0bb7187fdf7a637319e1b06983412ca6.bounds.extend( gmap\_m0bb7187fdf7a637319e1b06983412ca6.positions[m] );
}
// Render markers
for ( var m in gmap\_m0bb7187fdf7a637319e1b06983412ca6.positions ) {
gmap\_m0bb7187fdf7a637319e1b06983412ca6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0bb7187fdf7a637319e1b06983412ca6.map,
position : gmap\_m0bb7187fdf7a637319e1b06983412ca6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0bb7187fdf7a637319e1b06983412ca6.map.setCenter( gmap\_m0bb7187fdf7a637319e1b06983412ca6.positions[77] );
});