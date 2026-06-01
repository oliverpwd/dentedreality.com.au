---
title: ''
date: '2015-02-15T17:20:43+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/11008280_1049655208381771_1853809762_n.jpg?resize=640%2C640
---

[![Little people, doing things in the snow.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/02/11008280_1049655208381771_1853809762_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/02/15/little-people-doing-things-in-the-snow/) 

Little people, doing things in the snow.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/zJEgvdCmMV/) [5:20 pm, February 15, 2015](http://dentedreality.com.au/2015/02/15/little-people-doing-things-in-the-snow/ "5:20 pm") 
jQuery(document).ready(function(){
var gmap\_mfde072be064cce98b866fc2bf2f71684 = {
positions : {
33 : new google.maps.LatLng( '39.491488212', '-106.045679496' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mfde072be064cce98b866fc2bf2f71684' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mfde072be064cce98b866fc2bf2f71684.positions ) {
gmap\_mfde072be064cce98b866fc2bf2f71684.bounds.extend( gmap\_mfde072be064cce98b866fc2bf2f71684.positions[m] );
}
// Render markers
for ( var m in gmap\_mfde072be064cce98b866fc2bf2f71684.positions ) {
gmap\_mfde072be064cce98b866fc2bf2f71684.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mfde072be064cce98b866fc2bf2f71684.map,
position : gmap\_mfde072be064cce98b866fc2bf2f71684.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mfde072be064cce98b866fc2bf2f71684.map.setCenter( gmap\_mfde072be064cce98b866fc2bf2f71684.positions[33] );
});