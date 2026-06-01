---
title: ''
date: '2017-01-15T12:48:34+00:00'
format: image
service: instagram
tags:
- colorado
- snow
- trees
- winter
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/01/15877052_1354783907928892_3178151820514033664_n.jpg?fit=640%2C640
---

[![Snowshoeing. Blazing trails. #snow #trees #winter #colorado](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/01/15877052_1354783907928892_3178151820514033664_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2017/01/15/snowshoeing-blazing-trails-snow-trees-winter-colorado/) 

Snowshoeing. Blazing trails. #snow #trees #winter #colorado





* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[snow](http://dentedreality.com.au/tags/snow/)
* #[trees](http://dentedreality.com.au/tags/trees/)
* #[winter](http://dentedreality.com.au/tags/winter/)

Posted on [Instagram](https://www.instagram.com/p/BPTB0DtDIDJ/) [12:48 pm, January 15, 2017](http://dentedreality.com.au/2017/01/15/snowshoeing-blazing-trails-snow-trees-winter-colorado/ "12:48 pm") 
jQuery(document).ready(function(){
var gmap\_m20952802e6711907d186d8d79948f4eb = {
positions : {
279 : new google.maps.LatLng( '39.5815', '-105.868' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m20952802e6711907d186d8d79948f4eb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m20952802e6711907d186d8d79948f4eb.positions ) {
gmap\_m20952802e6711907d186d8d79948f4eb.bounds.extend( gmap\_m20952802e6711907d186d8d79948f4eb.positions[m] );
}
// Render markers
for ( var m in gmap\_m20952802e6711907d186d8d79948f4eb.positions ) {
gmap\_m20952802e6711907d186d8d79948f4eb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m20952802e6711907d186d8d79948f4eb.map,
position : gmap\_m20952802e6711907d186d8d79948f4eb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m20952802e6711907d186d8d79948f4eb.map.setCenter( gmap\_m20952802e6711907d186d8d79948f4eb.positions[279] );
});