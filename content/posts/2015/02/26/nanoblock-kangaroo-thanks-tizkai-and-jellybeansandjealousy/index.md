---
title: ''
date: '2015-02-26T18:07:11+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/10995066_1575951542643398_355971179_n.jpg?resize=640%2C640
---

[![Nanoblock Kangaroo! Thanks @tizkai and @jellybeansandjealousy!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/10995066_1575951542643398_355971179_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/02/26/nanoblock-kangaroo-thanks-tizkai-and-jellybeansandjealousy/) 

Nanoblock Kangaroo! Thanks @tizkai and @jellybeansandjealousy!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/zlektVCmKh/) [6:07 pm, February 26, 2015](http://dentedreality.com.au/2015/02/26/nanoblock-kangaroo-thanks-tizkai-and-jellybeansandjealousy/ "6:07 pm") 
jQuery(document).ready(function(){
var gmap\_md1e5157ef277c35de1c79ae388d420fd = {
positions : {
161 : new google.maps.LatLng( '39.73475', '-104.978491667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md1e5157ef277c35de1c79ae388d420fd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md1e5157ef277c35de1c79ae388d420fd.positions ) {
gmap\_md1e5157ef277c35de1c79ae388d420fd.bounds.extend( gmap\_md1e5157ef277c35de1c79ae388d420fd.positions[m] );
}
// Render markers
for ( var m in gmap\_md1e5157ef277c35de1c79ae388d420fd.positions ) {
gmap\_md1e5157ef277c35de1c79ae388d420fd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md1e5157ef277c35de1c79ae388d420fd.map,
position : gmap\_md1e5157ef277c35de1c79ae388d420fd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md1e5157ef277c35de1c79ae388d420fd.map.setCenter( gmap\_md1e5157ef277c35de1c79ae388d420fd.positions[161] );
});