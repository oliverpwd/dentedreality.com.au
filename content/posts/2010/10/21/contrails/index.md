---
title: Contrails
date: '2010-10-21T05:33:00+00:00'
format: image
service: flickr
tags:
- clouds
- contrail
- sky
- sun
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/5183168515_5d3db34988_o.jpg?resize=607%2C813
---

[![Contrails](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/5183168515_5d3db34988_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2010/10/21/contrails/) 
# [Contrails](http://dentedreality.com.au/2010/10/21/contrails/)





* #[clouds](http://dentedreality.com.au/tags/clouds/)
* #[contrail](http://dentedreality.com.au/tags/contrail/)
* #[sky](http://dentedreality.com.au/tags/sky/)
* #[sun](http://dentedreality.com.au/tags/sun/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183168515/) [5:33 am, October 21, 2010](http://dentedreality.com.au/2010/10/21/contrails/ "5:33 am") 
jQuery(document).ready(function(){
var gmap\_mac5fc628854f19b77ec9fe63ce71c48f = {
positions : {
782 : new google.maps.LatLng( '37.791', '-122.417334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mac5fc628854f19b77ec9fe63ce71c48f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mac5fc628854f19b77ec9fe63ce71c48f.positions ) {
gmap\_mac5fc628854f19b77ec9fe63ce71c48f.bounds.extend( gmap\_mac5fc628854f19b77ec9fe63ce71c48f.positions[m] );
}
// Render markers
for ( var m in gmap\_mac5fc628854f19b77ec9fe63ce71c48f.positions ) {
gmap\_mac5fc628854f19b77ec9fe63ce71c48f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mac5fc628854f19b77ec9fe63ce71c48f.map,
position : gmap\_mac5fc628854f19b77ec9fe63ce71c48f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mac5fc628854f19b77ec9fe63ce71c48f.map.setCenter( gmap\_mac5fc628854f19b77ec9fe63ce71c48f.positions[782] );
});