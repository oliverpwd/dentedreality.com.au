---
title: ''
date: '2014-05-31T15:13:22+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/05/10358260_1511156945773593_1373096135_n.jpg?resize=640%2C640
---

[![Hatchetin'](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/05/10358260_1511156945773593_1373096135_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/05/31/hatchetin/) 

Hatchetin’





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/orJhm7CmP-/) [3:13 pm, May 31, 2014](http://dentedreality.com.au/2014/05/31/hatchetin/ "3:13 pm") 
jQuery(document).ready(function(){
var gmap\_mc9c1576aa1d3a47c900c67acf2217fd8 = {
positions : {
681 : new google.maps.LatLng( '41.18327', '-74.165702833' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc9c1576aa1d3a47c900c67acf2217fd8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc9c1576aa1d3a47c900c67acf2217fd8.positions ) {
gmap\_mc9c1576aa1d3a47c900c67acf2217fd8.bounds.extend( gmap\_mc9c1576aa1d3a47c900c67acf2217fd8.positions[m] );
}
// Render markers
for ( var m in gmap\_mc9c1576aa1d3a47c900c67acf2217fd8.positions ) {
gmap\_mc9c1576aa1d3a47c900c67acf2217fd8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc9c1576aa1d3a47c900c67acf2217fd8.map,
position : gmap\_mc9c1576aa1d3a47c900c67acf2217fd8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc9c1576aa1d3a47c900c67acf2217fd8.map.setCenter( gmap\_mc9c1576aa1d3a47c900c67acf2217fd8.positions[681] );
});