---
title: ''
date: '2015-06-13T10:46:48+00:00'
format: image
service: instagram
tags:
- photo
- Snowflake
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/06/11348377_478240162342633_724617999_n.jpg?resize=640%2C640
---

[![Stranahan's Family Reunion. 2 different #Snowflake batches, Diamond Peak and regular-delicious.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/06/11348377_478240162342633_724617999_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/06/13/stranahans-family-reunion-2-different-snowflake-batches-diamond-peak-and-regular-delicious/) 

Stranahan’s Family Reunion. 2 different #Snowflake batches, Diamond Peak and regular-delicious.





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[Snowflake](http://dentedreality.com.au/tags/snowflake/)

Posted on [Instagram](https://instagram.com/p/34GXf1CmHF/) [10:46 am, June 13, 2015](http://dentedreality.com.au/2015/06/13/stranahans-family-reunion-2-different-snowflake-batches-diamond-peak-and-regular-delicious/ "10:46 am") 
jQuery(document).ready(function(){
var gmap\_m2da36aa431d0d34edafd766f52ea9e1e = {
positions : {
797 : new google.maps.LatLng( '39.759888333', '-104.96955' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2da36aa431d0d34edafd766f52ea9e1e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2da36aa431d0d34edafd766f52ea9e1e.positions ) {
gmap\_m2da36aa431d0d34edafd766f52ea9e1e.bounds.extend( gmap\_m2da36aa431d0d34edafd766f52ea9e1e.positions[m] );
}
// Render markers
for ( var m in gmap\_m2da36aa431d0d34edafd766f52ea9e1e.positions ) {
gmap\_m2da36aa431d0d34edafd766f52ea9e1e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2da36aa431d0d34edafd766f52ea9e1e.map,
position : gmap\_m2da36aa431d0d34edafd766f52ea9e1e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2da36aa431d0d34edafd766f52ea9e1e.map.setCenter( gmap\_m2da36aa431d0d34edafd766f52ea9e1e.positions[797] );
});