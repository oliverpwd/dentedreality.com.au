---
title: ''
date: '2016-08-09T23:19:06+00:00'
format: image
service: instagram
tags:
- fatbike
- mountainbike
- mud
- prospecttrail
- telluride
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13768107_1616428662020827_635023517_n.jpg?fit=640%2C640
---

[![This is what a good ride looks like at the end. #fatbike #mountainbike #telluride #prospecttrail #mud](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13768107_1616428662020827_635023517_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/08/09/this-is-what-a-good-ride-looks-like-at-the-end-fatbike-mountainbike-telluride-prospecttrail-mud/) 

This is what a good ride looks like at the end. #fatbike #mountainbike #telluride #prospecttrail #mud





* #[fatbike](http://dentedreality.com.au/tags/fatbike/)
* #[mountainbike](http://dentedreality.com.au/tags/mountainbike/)
* #[mud](http://dentedreality.com.au/tags/mud/)
* #[prospecttrail](http://dentedreality.com.au/tags/prospecttrail/)
* #[telluride](http://dentedreality.com.au/tags/telluride/)

Posted on [Instagram](https://www.instagram.com/p/BI6otnNgCp4/) [11:19 pm, August 9, 2016](http://dentedreality.com.au/2016/08/09/this-is-what-a-good-ride-looks-like-at-the-end-fatbike-mountainbike-telluride-prospecttrail-mud/ "11:19 pm") 
jQuery(document).ready(function(){
var gmap\_m798bee1c8a978dd11059211b6594f889 = {
positions : {
632 : new google.maps.LatLng( '37.938048566667', '-107.81100471667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m798bee1c8a978dd11059211b6594f889' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m798bee1c8a978dd11059211b6594f889.positions ) {
gmap\_m798bee1c8a978dd11059211b6594f889.bounds.extend( gmap\_m798bee1c8a978dd11059211b6594f889.positions[m] );
}
// Render markers
for ( var m in gmap\_m798bee1c8a978dd11059211b6594f889.positions ) {
gmap\_m798bee1c8a978dd11059211b6594f889.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m798bee1c8a978dd11059211b6594f889.map,
position : gmap\_m798bee1c8a978dd11059211b6594f889.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m798bee1c8a978dd11059211b6594f889.map.setCenter( gmap\_m798bee1c8a978dd11059211b6594f889.positions[632] );
});