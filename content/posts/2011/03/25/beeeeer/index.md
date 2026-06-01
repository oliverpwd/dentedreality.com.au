---
title: ''
date: '2011-03-25T16:28:22+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/563aa4c8c46841cdb0eadaa5aa003c4a_7.jpg?resize=607%2C607
---

[![Beeeeer!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/563aa4c8c46841cdb0eadaa5aa003c4a_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/03/25/beeeeer/) 

Beeeeer!





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/Ch_PD/) [4:28 pm, March 25, 2011](http://dentedreality.com.au/2011/03/25/beeeeer/ "4:28 pm") 
jQuery(document).ready(function(){
var gmap\_maf0f998ab2936fbdf36c97373e53e40a = {
positions : {
822 : new google.maps.LatLng( '37.785559798', '-122.399674048' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maf0f998ab2936fbdf36c97373e53e40a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maf0f998ab2936fbdf36c97373e53e40a.positions ) {
gmap\_maf0f998ab2936fbdf36c97373e53e40a.bounds.extend( gmap\_maf0f998ab2936fbdf36c97373e53e40a.positions[m] );
}
// Render markers
for ( var m in gmap\_maf0f998ab2936fbdf36c97373e53e40a.positions ) {
gmap\_maf0f998ab2936fbdf36c97373e53e40a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maf0f998ab2936fbdf36c97373e53e40a.map,
position : gmap\_maf0f998ab2936fbdf36c97373e53e40a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maf0f998ab2936fbdf36c97373e53e40a.map.setCenter( gmap\_maf0f998ab2936fbdf36c97373e53e40a.positions[822] );
});