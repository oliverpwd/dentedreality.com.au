---
title: Camping, Sonoma Coast
date: '2010-11-26T11:46:25+00:00'
format: image
service: flickr
tags:
- california
- camping
- sonomacoast
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434637108_2c23eda33b_o.jpg?resize=607%2C452
---

[![Camping, Sonoma Coast](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434637108_2c23eda33b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/11/26/camping-sonoma-coast-11/) 
# [Camping, Sonoma Coast](http://dentedreality.com.au/2010/11/26/camping-sonoma-coast-11/)





* #[california](http://dentedreality.com.au/tags/california/)
* #[camping](http://dentedreality.com.au/tags/camping/)
* #[sonomacoast](http://dentedreality.com.au/tags/sonomacoast/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434637108/) [11:46 am, November 26, 2010](http://dentedreality.com.au/2010/11/26/camping-sonoma-coast-11/ "11:46 am") 
jQuery(document).ready(function(){
var gmap\_m3e0f671cc83949256b21e0111d40b73a = {
positions : {
661 : new google.maps.LatLng( '38.412333', '-123.101334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3e0f671cc83949256b21e0111d40b73a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3e0f671cc83949256b21e0111d40b73a.positions ) {
gmap\_m3e0f671cc83949256b21e0111d40b73a.bounds.extend( gmap\_m3e0f671cc83949256b21e0111d40b73a.positions[m] );
}
// Render markers
for ( var m in gmap\_m3e0f671cc83949256b21e0111d40b73a.positions ) {
gmap\_m3e0f671cc83949256b21e0111d40b73a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3e0f671cc83949256b21e0111d40b73a.map,
position : gmap\_m3e0f671cc83949256b21e0111d40b73a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3e0f671cc83949256b21e0111d40b73a.map.setCenter( gmap\_m3e0f671cc83949256b21e0111d40b73a.positions[661] );
});