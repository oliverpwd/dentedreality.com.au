---
title: Camping, Sonoma Coast
date: '2010-11-27T09:51:06+00:00'
format: image
service: flickr
tags:
- california
- camping
- sonomacoast
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434639694_75cee153b1_o.jpg?resize=607%2C452
---

[![Camping, Sonoma Coast](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434639694_75cee153b1_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/11/27/camping-sonoma-coast/) 
# [Camping, Sonoma Coast](http://dentedreality.com.au/2010/11/27/camping-sonoma-coast/)





* #[california](http://dentedreality.com.au/tags/california/)
* #[camping](http://dentedreality.com.au/tags/camping/)
* #[sonomacoast](http://dentedreality.com.au/tags/sonomacoast/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434639694/) [9:51 am, November 27, 2010](http://dentedreality.com.au/2010/11/27/camping-sonoma-coast/ "9:51 am") 
jQuery(document).ready(function(){
var gmap\_mf1d25dcf7bf77e8b63ff6b7ad203d2a8 = {
positions : {
59 : new google.maps.LatLng( '37.822833', '-122.479167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf1d25dcf7bf77e8b63ff6b7ad203d2a8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf1d25dcf7bf77e8b63ff6b7ad203d2a8.positions ) {
gmap\_mf1d25dcf7bf77e8b63ff6b7ad203d2a8.bounds.extend( gmap\_mf1d25dcf7bf77e8b63ff6b7ad203d2a8.positions[m] );
}
// Render markers
for ( var m in gmap\_mf1d25dcf7bf77e8b63ff6b7ad203d2a8.positions ) {
gmap\_mf1d25dcf7bf77e8b63ff6b7ad203d2a8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf1d25dcf7bf77e8b63ff6b7ad203d2a8.map,
position : gmap\_mf1d25dcf7bf77e8b63ff6b7ad203d2a8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf1d25dcf7bf77e8b63ff6b7ad203d2a8.map.setCenter( gmap\_mf1d25dcf7bf77e8b63ff6b7ad203d2a8.positions[59] );
});