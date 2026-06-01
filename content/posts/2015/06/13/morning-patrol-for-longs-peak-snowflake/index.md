---
title: ''
date: '2015-06-13T06:26:44+00:00'
format: image
service: instagram
tags:
- photo
- Snowflake
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/06/11386442_373400982851413_323441731_n.jpg?resize=640%2C640
---

[![Morning Patrol for Long's Peak #Snowflake](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/06/11386442_373400982851413_323441731_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/06/13/morning-patrol-for-longs-peak-snowflake/) 

Morning Patrol for Long’s Peak #Snowflake





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[Snowflake](http://dentedreality.com.au/tags/snowflake/)

Posted on [Instagram](https://instagram.com/p/33omrkimHY/) [6:26 am, June 13, 2015](http://dentedreality.com.au/2015/06/13/morning-patrol-for-longs-peak-snowflake/ "6:26 am") 
jQuery(document).ready(function(){
var gmap\_m944ad68371b427667c35a7d41359b517 = {
positions : {
709 : new google.maps.LatLng( '39.712691', '-104.998779' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m944ad68371b427667c35a7d41359b517' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m944ad68371b427667c35a7d41359b517.positions ) {
gmap\_m944ad68371b427667c35a7d41359b517.bounds.extend( gmap\_m944ad68371b427667c35a7d41359b517.positions[m] );
}
// Render markers
for ( var m in gmap\_m944ad68371b427667c35a7d41359b517.positions ) {
gmap\_m944ad68371b427667c35a7d41359b517.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m944ad68371b427667c35a7d41359b517.map,
position : gmap\_m944ad68371b427667c35a7d41359b517.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m944ad68371b427667c35a7d41359b517.map.setCenter( gmap\_m944ad68371b427667c35a7d41359b517.positions[709] );
});