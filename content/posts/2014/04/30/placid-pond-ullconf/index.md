---
title: ''
date: '2014-04-30T05:03:09+00:00'
format: image
service: instagram
tags:
- photo
- ullconf
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/10299776_1394185347531546_1678166455_n.jpg?resize=640%2C640
---

[![Placid Pond. #ullconf](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/10299776_1394185347531546_1678166455_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/04/30/placid-pond-ullconf/) 

Placid Pond. #ullconf





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[ullconf](http://dentedreality.com.au/tags/ullconf/)

Posted on [Instagram](http://instagram.com/p/naPDH_CmCi/) [5:03 am, April 30, 2014](http://dentedreality.com.au/2014/04/30/placid-pond-ullconf/ "5:03 am") 
jQuery(document).ready(function(){
var gmap\_meb54f8d167e4ffba4f9e27f68c0935b3 = {
positions : {
770 : new google.maps.LatLng( '52.648536667', '-7.194963333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_meb54f8d167e4ffba4f9e27f68c0935b3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_meb54f8d167e4ffba4f9e27f68c0935b3.positions ) {
gmap\_meb54f8d167e4ffba4f9e27f68c0935b3.bounds.extend( gmap\_meb54f8d167e4ffba4f9e27f68c0935b3.positions[m] );
}
// Render markers
for ( var m in gmap\_meb54f8d167e4ffba4f9e27f68c0935b3.positions ) {
gmap\_meb54f8d167e4ffba4f9e27f68c0935b3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_meb54f8d167e4ffba4f9e27f68c0935b3.map,
position : gmap\_meb54f8d167e4ffba4f9e27f68c0935b3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_meb54f8d167e4ffba4f9e27f68c0935b3.map.setCenter( gmap\_meb54f8d167e4ffba4f9e27f68c0935b3.positions[770] );
});