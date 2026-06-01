---
title: Camping, Sonoma Coast
date: '2010-11-26T11:46:40+00:00'
format: image
service: flickr
tags:
- california
- camping
- sonomacoast
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434023983_fcac91fd44_o.jpg?resize=607%2C452
---

[![Camping, Sonoma Coast](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434023983_fcac91fd44_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/11/26/camping-sonoma-coast-10/) 
# [Camping, Sonoma Coast](http://dentedreality.com.au/2010/11/26/camping-sonoma-coast-10/)





* #[california](http://dentedreality.com.au/tags/california/)
* #[camping](http://dentedreality.com.au/tags/camping/)
* #[sonomacoast](http://dentedreality.com.au/tags/sonomacoast/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434023983/) [11:46 am, November 26, 2010](http://dentedreality.com.au/2010/11/26/camping-sonoma-coast-10/ "11:46 am") 
jQuery(document).ready(function(){
var gmap\_m8518d3a59a0c3c35616aff1b213b07af = {
positions : {
56 : new google.maps.LatLng( '38.412333', '-123.101334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8518d3a59a0c3c35616aff1b213b07af' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8518d3a59a0c3c35616aff1b213b07af.positions ) {
gmap\_m8518d3a59a0c3c35616aff1b213b07af.bounds.extend( gmap\_m8518d3a59a0c3c35616aff1b213b07af.positions[m] );
}
// Render markers
for ( var m in gmap\_m8518d3a59a0c3c35616aff1b213b07af.positions ) {
gmap\_m8518d3a59a0c3c35616aff1b213b07af.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8518d3a59a0c3c35616aff1b213b07af.map,
position : gmap\_m8518d3a59a0c3c35616aff1b213b07af.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8518d3a59a0c3c35616aff1b213b07af.map.setCenter( gmap\_m8518d3a59a0c3c35616aff1b213b07af.positions[56] );
});