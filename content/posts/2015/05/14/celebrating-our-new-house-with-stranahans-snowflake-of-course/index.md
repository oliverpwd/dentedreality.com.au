---
title: ''
date: '2015-05-14T18:28:05+00:00'
format: image
service: instagram
tags:
- photo
- Snowflake
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/11245637_752725234848389_1879422047_n.jpg?resize=640%2C640
---

[![Celebrating our new house with @stranahans #snowflake, of course.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/11245637_752725234848389_1879422047_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/05/14/celebrating-our-new-house-with-stranahans-snowflake-of-course/) 

Celebrating our new house with @stranahans #snowflake, of course.





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[Snowflake](http://dentedreality.com.au/tags/snowflake/)

Posted on [Instagram](https://instagram.com/p/2rrTyeCmEX/) [6:28 pm, May 14, 2015](http://dentedreality.com.au/2015/05/14/celebrating-our-new-house-with-stranahans-snowflake-of-course/ "6:28 pm") 
jQuery(document).ready(function(){
var gmap\_m17acee1d93c3d503f08cc184393bd259 = {
positions : {
784 : new google.maps.LatLng( '39.759913333', '-104.969528333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m17acee1d93c3d503f08cc184393bd259' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m17acee1d93c3d503f08cc184393bd259.positions ) {
gmap\_m17acee1d93c3d503f08cc184393bd259.bounds.extend( gmap\_m17acee1d93c3d503f08cc184393bd259.positions[m] );
}
// Render markers
for ( var m in gmap\_m17acee1d93c3d503f08cc184393bd259.positions ) {
gmap\_m17acee1d93c3d503f08cc184393bd259.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m17acee1d93c3d503f08cc184393bd259.map,
position : gmap\_m17acee1d93c3d503f08cc184393bd259.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m17acee1d93c3d503f08cc184393bd259.map.setCenter( gmap\_m17acee1d93c3d503f08cc184393bd259.positions[784] );
});