---
title: ''
date: '2018-03-14T20:16:15+00:00'
format: image
service: instagram
image: https://dentedreality.com.au/wp-content/uploads/2018/03/28765264_117825635667137_3753973580468060160_n.jpg
---

[![Linear](https://dentedreality.com.au/wp-content/uploads/2018/03/28765264_117825635667137_3753973580468060160_n.jpg)](https://dentedreality.com.au/2018/03/14/linear/) 

[![Linear](https://dentedreality.com.au/wp-content/uploads/2018/03/28765264_117825635667137_3753973580468060160_n.jpg)](https://www.instagram.com/p/BgU6bj3jrQH/)

Linear





Posted on [Instagram](https://www.instagram.com/p/BgU6bj3jrQH/) [8:16 pm, March 14, 2018](https://dentedreality.com.au/2018/03/14/linear/ "8:16 pm") 
jQuery(document).ready(function(){
var gmap\_maf6a196b76ae75d12d7aa7a227d28488 = {
positions : {
62 : new google.maps.LatLng( '39.76924', '-104.97717' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maf6a196b76ae75d12d7aa7a227d28488' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maf6a196b76ae75d12d7aa7a227d28488.positions ) {
gmap\_maf6a196b76ae75d12d7aa7a227d28488.bounds.extend( gmap\_maf6a196b76ae75d12d7aa7a227d28488.positions[m] );
}
// Render markers
for ( var m in gmap\_maf6a196b76ae75d12d7aa7a227d28488.positions ) {
gmap\_maf6a196b76ae75d12d7aa7a227d28488.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maf6a196b76ae75d12d7aa7a227d28488.map,
position : gmap\_maf6a196b76ae75d12d7aa7a227d28488.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maf6a196b76ae75d12d7aa7a227d28488.map.setCenter( gmap\_maf6a196b76ae75d12d7aa7a227d28488.positions[62] );
});