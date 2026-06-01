---
title: ''
date: '2014-10-26T13:30:17+00:00'
format: image
tags:
- hyperlapse
- photo
- WCSF14
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/10724732_331958440309007_653488233_n.jpg?resize=640%2C640
---

[![#wcsf14 BBQ migration #hyperlapse](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/10724732_331958440309007_653488233_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/10/26/wcsf14-bbq-migration-hyperlapse-2/) 

#wcsf14 BBQ migration #hyperlapse





* #[hyperlapse](http://dentedreality.com.au/tags/hyperlapse/)
* #[photo](http://dentedreality.com.au/tags/photo/)
* #[WCSF14](http://dentedreality.com.au/tags/wcsf14/)

Posted on [Instagram](http://instagram.com/p/uoKPmcimFF/) [1:30 pm, October 26, 2014](http://dentedreality.com.au/2014/10/26/wcsf14-bbq-migration-hyperlapse-2/ "1:30 pm") 
jQuery(document).ready(function(){
var gmap\_mecc7d9015da906289f36825db641b305 = {
positions : {
983 : new google.maps.LatLng( '37.767929532', '-122.392871019' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mecc7d9015da906289f36825db641b305' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mecc7d9015da906289f36825db641b305.positions ) {
gmap\_mecc7d9015da906289f36825db641b305.bounds.extend( gmap\_mecc7d9015da906289f36825db641b305.positions[m] );
}
// Render markers
for ( var m in gmap\_mecc7d9015da906289f36825db641b305.positions ) {
gmap\_mecc7d9015da906289f36825db641b305.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mecc7d9015da906289f36825db641b305.map,
position : gmap\_mecc7d9015da906289f36825db641b305.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mecc7d9015da906289f36825db641b305.map.setCenter( gmap\_mecc7d9015da906289f36825db641b305.positions[983] );
});