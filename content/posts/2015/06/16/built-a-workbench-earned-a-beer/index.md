---
title: ''
date: '2015-06-16T17:04:17+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/06/11333364_497365787087553_1051130327_n.jpg?resize=640%2C640
---

[![Built a workbench. Earned a beer.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/06/11333364_497365787087553_1051130327_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/06/16/built-a-workbench-earned-a-beer/) 

Built a workbench. Earned a beer.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/4Af83XCmJc/) [5:04 pm, June 16, 2015](http://dentedreality.com.au/2015/06/16/built-a-workbench-earned-a-beer/ "5:04 pm") 
jQuery(document).ready(function(){
var gmap\_m0cc791f633e6f0934c642afcb792f306 = {
positions : {
633 : new google.maps.LatLng( '39.759913333', '-104.969528333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0cc791f633e6f0934c642afcb792f306' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0cc791f633e6f0934c642afcb792f306.positions ) {
gmap\_m0cc791f633e6f0934c642afcb792f306.bounds.extend( gmap\_m0cc791f633e6f0934c642afcb792f306.positions[m] );
}
// Render markers
for ( var m in gmap\_m0cc791f633e6f0934c642afcb792f306.positions ) {
gmap\_m0cc791f633e6f0934c642afcb792f306.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0cc791f633e6f0934c642afcb792f306.map,
position : gmap\_m0cc791f633e6f0934c642afcb792f306.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0cc791f633e6f0934c642afcb792f306.map.setCenter( gmap\_m0cc791f633e6f0934c642afcb792f306.positions[633] );
});