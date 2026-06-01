---
title: ''
date: '2016-09-06T23:00:49+00:00'
format: image
service: instagram
tags:
- mtbierstadt
- Snowflake
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14280388_591770380948225_625659807_n.jpg?fit=640%2C640
---

[![Drinking @stranahans #mtbierstadt #snowflake at the summit of Mt. Bierstadt. Like a boss.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14280388_591770380948225_625659807_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/09/06/drinking-stranahans-mtbierstadt-snowflake-at-the-summit-of-mt-bierstadt-like-a-boss/) 

Drinking @stranahans #mtbierstadt #snowflake at the summit of Mt. Bierstadt. Like a boss.





* #[mtbierstadt](http://dentedreality.com.au/tags/mtbierstadt/)
* #[Snowflake](http://dentedreality.com.au/tags/snowflake/)

Posted on [Instagram](https://www.instagram.com/p/BKCs4JLAl-r/) [11:00 pm, September 6, 2016](http://dentedreality.com.au/2016/09/06/drinking-stranahans-mtbierstadt-snowflake-at-the-summit-of-mt-bierstadt-like-a-boss/ "11:00 pm") 
jQuery(document).ready(function(){
var gmap\_md0c1db5e3b7e2cdd2fd69fc30584cd41 = {
positions : {
940 : new google.maps.LatLng( '39.582462310791', '-105.66902160645' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md0c1db5e3b7e2cdd2fd69fc30584cd41' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md0c1db5e3b7e2cdd2fd69fc30584cd41.positions ) {
gmap\_md0c1db5e3b7e2cdd2fd69fc30584cd41.bounds.extend( gmap\_md0c1db5e3b7e2cdd2fd69fc30584cd41.positions[m] );
}
// Render markers
for ( var m in gmap\_md0c1db5e3b7e2cdd2fd69fc30584cd41.positions ) {
gmap\_md0c1db5e3b7e2cdd2fd69fc30584cd41.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md0c1db5e3b7e2cdd2fd69fc30584cd41.map,
position : gmap\_md0c1db5e3b7e2cdd2fd69fc30584cd41.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md0c1db5e3b7e2cdd2fd69fc30584cd41.map.setCenter( gmap\_md0c1db5e3b7e2cdd2fd69fc30584cd41.positions[940] );
});