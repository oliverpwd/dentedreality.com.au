---
title: ''
date: '2014-12-06T19:46:10+00:00'
format: image
service: instagram
tags:
- mtbierstadt
- photo
- Snowflake
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10838798_707056016057447_840534686_n.jpg?resize=640%2C640
---

[![Time to try some @stranahans #snowflake #mtbierstadt](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/10838798_707056016057447_840534686_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/12/06/time-to-try-some-stranahans-snowflake-mtbierstadt/) 

Time to try some @stranahans #snowflake #mtbierstadt





* #[mtbierstadt](http://dentedreality.com.au/tags/mtbierstadt/)
* #[photo](http://dentedreality.com.au/tags/photo/)
* #[Snowflake](http://dentedreality.com.au/tags/snowflake/)

Posted on [Instagram](http://instagram.com/p/wSgt7bCmMI/) [7:46 pm, December 6, 2014](http://dentedreality.com.au/2014/12/06/time-to-try-some-stranahans-snowflake-mtbierstadt/ "7:46 pm") 
jQuery(document).ready(function(){
var gmap\_m902a4c8ac6842acb1bff1fe4842a8197 = {
positions : {
801 : new google.maps.LatLng( '39.734736667', '-104.978455' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m902a4c8ac6842acb1bff1fe4842a8197' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m902a4c8ac6842acb1bff1fe4842a8197.positions ) {
gmap\_m902a4c8ac6842acb1bff1fe4842a8197.bounds.extend( gmap\_m902a4c8ac6842acb1bff1fe4842a8197.positions[m] );
}
// Render markers
for ( var m in gmap\_m902a4c8ac6842acb1bff1fe4842a8197.positions ) {
gmap\_m902a4c8ac6842acb1bff1fe4842a8197.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m902a4c8ac6842acb1bff1fe4842a8197.map,
position : gmap\_m902a4c8ac6842acb1bff1fe4842a8197.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m902a4c8ac6842acb1bff1fe4842a8197.map.setCenter( gmap\_m902a4c8ac6842acb1bff1fe4842a8197.positions[801] );
});