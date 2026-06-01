---
title: ''
date: '2016-09-01T15:35:45+00:00'
format: image
service: instagram
tags:
- alpinelake
- backpacking
- colorado
- mountains
- nature
- sabbatical
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/13687170_1086365294750850_749651354_n.jpg?fit=640%2C640
---

[![I was not actually surprised to com across an #alpinelake at his point. #colorado #mountains #nature #backpacking #sabbatical](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/13687170_1086365294750850_749651354_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/09/01/i-was-not-actually-surprised-to-com-across-an-alpinelake-at-his-point-colorado-mountains-nature-backpacking-sabbatical/) 

I was not actually surprised to com across an #alpinelake at his point. #colorado #mountains #nature #backpacking #sabbatical





* #[alpinelake](http://dentedreality.com.au/tags/alpinelake/)
* #[backpacking](http://dentedreality.com.au/tags/backpacking/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[mountains](http://dentedreality.com.au/tags/mountains/)
* #[nature](http://dentedreality.com.au/tags/nature/)
* #[sabbatical](http://dentedreality.com.au/tags/sabbatical/)

Posted on [Instagram](https://www.instagram.com/p/BJ1B-CRA2XS/) [3:35 pm, September 1, 2016](http://dentedreality.com.au/2016/09/01/i-was-not-actually-surprised-to-com-across-an-alpinelake-at-his-point-colorado-mountains-nature-backpacking-sabbatical/ "3:35 pm") 
jQuery(document).ready(function(){
var gmap\_md972fe9940d0dfe78902d857f958eec9 = {
positions : {
93 : new google.maps.LatLng( '39.809279883333', '-106.3025675' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md972fe9940d0dfe78902d857f958eec9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md972fe9940d0dfe78902d857f958eec9.positions ) {
gmap\_md972fe9940d0dfe78902d857f958eec9.bounds.extend( gmap\_md972fe9940d0dfe78902d857f958eec9.positions[m] );
}
// Render markers
for ( var m in gmap\_md972fe9940d0dfe78902d857f958eec9.positions ) {
gmap\_md972fe9940d0dfe78902d857f958eec9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md972fe9940d0dfe78902d857f958eec9.map,
position : gmap\_md972fe9940d0dfe78902d857f958eec9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md972fe9940d0dfe78902d857f958eec9.map.setCenter( gmap\_md972fe9940d0dfe78902d857f958eec9.positions[93] );
});