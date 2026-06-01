---
title: That’s our plane
date: '2006-12-22T23:49:38+00:00'
format: image
service: flickr
tags:
- airplane
- plane
- thailand06
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348123119_eecb6156cd_o.jpg?resize=607%2C455
---

[![That's our plane](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348123119_eecb6156cd_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/22/thats-our-plane/) 
# [That’s our plane](http://dentedreality.com.au/2006/12/22/thats-our-plane/)





* #[airplane](http://dentedreality.com.au/tags/airplane/)
* #[plane](http://dentedreality.com.au/tags/plane/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348123119/) [11:49 pm, December 22, 2006](http://dentedreality.com.au/2006/12/22/thats-our-plane/ "11:49 pm") 
jQuery(document).ready(function(){
var gmap\_m3502d9997860ade3188ad44591751227 = {
positions : {
823 : new google.maps.LatLng( '1.35514', '103.99229' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3502d9997860ade3188ad44591751227' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3502d9997860ade3188ad44591751227.positions ) {
gmap\_m3502d9997860ade3188ad44591751227.bounds.extend( gmap\_m3502d9997860ade3188ad44591751227.positions[m] );
}
// Render markers
for ( var m in gmap\_m3502d9997860ade3188ad44591751227.positions ) {
gmap\_m3502d9997860ade3188ad44591751227.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3502d9997860ade3188ad44591751227.map,
position : gmap\_m3502d9997860ade3188ad44591751227.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3502d9997860ade3188ad44591751227.map.setCenter( gmap\_m3502d9997860ade3188ad44591751227.positions[823] );
});