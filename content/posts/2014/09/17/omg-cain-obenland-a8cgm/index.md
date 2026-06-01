---
title: ''
date: '2014-09-17T02:08:35+00:00'
format: image
tags:
- a8cgm
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10693410_952786461403501_1760082197_n.jpg?resize=640%2C640
---

[![OMG Cain & Obenland! #a8cgm](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10693410_952786461403501_1760082197_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/09/17/omg-cain-obenland-a8cgm/) 

OMG Cain & Obenland! #a8cgm





* #[a8cgm](http://dentedreality.com.au/tags/a8cgm/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/tChOmDCmO1/) [2:08 am, September 17, 2014](http://dentedreality.com.au/2014/09/17/omg-cain-obenland-a8cgm/ "2:08 am") 
jQuery(document).ready(function(){
var gmap\_mf485e4374a8a91ef24999b4e5ef3fcaf = {
positions : {
42 : new google.maps.LatLng( '40.68595', '-111.556328333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf485e4374a8a91ef24999b4e5ef3fcaf' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf485e4374a8a91ef24999b4e5ef3fcaf.positions ) {
gmap\_mf485e4374a8a91ef24999b4e5ef3fcaf.bounds.extend( gmap\_mf485e4374a8a91ef24999b4e5ef3fcaf.positions[m] );
}
// Render markers
for ( var m in gmap\_mf485e4374a8a91ef24999b4e5ef3fcaf.positions ) {
gmap\_mf485e4374a8a91ef24999b4e5ef3fcaf.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf485e4374a8a91ef24999b4e5ef3fcaf.map,
position : gmap\_mf485e4374a8a91ef24999b4e5ef3fcaf.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf485e4374a8a91ef24999b4e5ef3fcaf.map.setCenter( gmap\_mf485e4374a8a91ef24999b4e5ef3fcaf.positions[42] );
});