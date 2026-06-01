---
title: ''
date: '2015-01-09T21:05:34+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/01/10919722_837351696324230_1341737867_n.jpg?resize=640%2C640
---

[![Third annual Christmas Puzzle (NYC) complete!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/01/10919722_837351696324230_1341737867_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/01/09/third-annual-christmas-puzzle-nyc-complete/) 

Third annual Christmas Puzzle (NYC) complete!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/xqM1PgimB3/) [9:05 pm, January 9, 2015](http://dentedreality.com.au/2015/01/09/third-annual-christmas-puzzle-nyc-complete/ "9:05 pm") 
jQuery(document).ready(function(){
var gmap\_mca298bea74dd6f73d10cf826eaeb2273 = {
positions : {
594 : new google.maps.LatLng( '39.734766667', '-104.97847' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mca298bea74dd6f73d10cf826eaeb2273' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mca298bea74dd6f73d10cf826eaeb2273.positions ) {
gmap\_mca298bea74dd6f73d10cf826eaeb2273.bounds.extend( gmap\_mca298bea74dd6f73d10cf826eaeb2273.positions[m] );
}
// Render markers
for ( var m in gmap\_mca298bea74dd6f73d10cf826eaeb2273.positions ) {
gmap\_mca298bea74dd6f73d10cf826eaeb2273.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mca298bea74dd6f73d10cf826eaeb2273.map,
position : gmap\_mca298bea74dd6f73d10cf826eaeb2273.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mca298bea74dd6f73d10cf826eaeb2273.map.setCenter( gmap\_mca298bea74dd6f73d10cf826eaeb2273.positions[594] );
});