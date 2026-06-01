---
title: ''
date: '2018-03-20T21:22:50+00:00'
format: image
service: instagram
image: https://dentedreality.com.au/wp-content/uploads/2018/03/29093129_2053095898301696_4103848286484430848_n.jpg
---

[![Two new places to try in the neighborhood, both opened this week!](https://dentedreality.com.au/wp-content/uploads/2018/03/29093129_2053095898301696_4103848286484430848_n.jpg)](https://dentedreality.com.au/2018/03/20/two-new-places-to-try-in-the-neighborhood-both-opened-this-week/) 

[![Two new places to try in the neighborhood, both opened this week!](https://dentedreality.com.au/wp-content/uploads/2018/03/29093129_2053095898301696_4103848286484430848_n.jpg)](https://www.instagram.com/p/Bgke0guDVo1/)

Two new places to try in the neighborhood, both opened this week!





Posted on [Instagram](https://www.instagram.com/p/Bgke0guDVo1/) [9:22 pm, March 20, 2018](https://dentedreality.com.au/2018/03/20/two-new-places-to-try-in-the-neighborhood-both-opened-this-week/ "9:22 pm") 
jQuery(document).ready(function(){
var gmap\_m3a1d9348e70bb27226f4b4b236283d74 = {
positions : {
243 : new google.maps.LatLng( '39.76129', '-104.98129' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3a1d9348e70bb27226f4b4b236283d74' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3a1d9348e70bb27226f4b4b236283d74.positions ) {
gmap\_m3a1d9348e70bb27226f4b4b236283d74.bounds.extend( gmap\_m3a1d9348e70bb27226f4b4b236283d74.positions[m] );
}
// Render markers
for ( var m in gmap\_m3a1d9348e70bb27226f4b4b236283d74.positions ) {
gmap\_m3a1d9348e70bb27226f4b4b236283d74.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3a1d9348e70bb27226f4b4b236283d74.map,
position : gmap\_m3a1d9348e70bb27226f4b4b236283d74.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3a1d9348e70bb27226f4b4b236283d74.map.setCenter( gmap\_m3a1d9348e70bb27226f4b4b236283d74.positions[243] );
});