---
title: ''
date: '2018-07-21T03:37:32-06:00'
format: image
service: instagram
tags:
- shrine
- temple
latitude: '34.967222'
longitude: '135.772778'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2018/07/14182123/36794004_1780392968715351_8080594553511346176_n.jpg
---

[![If you get there early, it's relatively empty. #temple #shrine](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2018/07/14182123/36794004_1780392968715351_8080594553511346176_n.jpg)](https://dentedreality.com.au/2018/07/21/if-you-get-there-early-its-relatively-empty-temple-shrine/) 

[![If you get there early, it's relatively empty. #temple #shrine](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2018/07/14182123/36794004_1780392968715351_8080594553511346176_n.jpg)](https://www.instagram.com/p/BlfSrpOlSGC/)

If you get there early, it’s relatively empty. #temple #shrine

34.967222135.772778




* #[shrine](https://dentedreality.com.au/tags/shrine/)
* #[temple](https://dentedreality.com.au/tags/temple/)

Posted on [Instagram](https://www.instagram.com/p/BlfSrpOlSGC/) [3:37 am, July 21, 2018](https://dentedreality.com.au/2018/07/21/if-you-get-there-early-its-relatively-empty-temple-shrine/ "3:37 am") 
jQuery(document).ready(function(){
var gmap\_mc228ece0a389d09499f56dda0c064a88 = {
positions : {
321 : new google.maps.LatLng( '34.967222', '135.772778' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc228ece0a389d09499f56dda0c064a88' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc228ece0a389d09499f56dda0c064a88.positions ) {
gmap\_mc228ece0a389d09499f56dda0c064a88.bounds.extend( gmap\_mc228ece0a389d09499f56dda0c064a88.positions[m] );
}
// Render markers
for ( var m in gmap\_mc228ece0a389d09499f56dda0c064a88.positions ) {
gmap\_mc228ece0a389d09499f56dda0c064a88.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc228ece0a389d09499f56dda0c064a88.map,
position : gmap\_mc228ece0a389d09499f56dda0c064a88.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc228ece0a389d09499f56dda0c064a88.map.setCenter( gmap\_mc228ece0a389d09499f56dda0c064a88.positions[321] );
});