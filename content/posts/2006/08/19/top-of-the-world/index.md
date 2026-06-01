---
title: Top of the World
date: '2006-08-19T16:41:36+00:00'
format: image
service: flickr
tags:
- mounttam
- mounttamalpais
- mttam
- mttamalpais
- sanfrancisco
- silhouette
- sun
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/08/221185817_f30401eb00_o.jpg?resize=607%2C455
---

[![Top of the World](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/08/221185817_f30401eb00_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/08/19/top-of-the-world/) 
# [Top of the World](http://dentedreality.com.au/2006/08/19/top-of-the-world/)





* #[mounttam](http://dentedreality.com.au/tags/mounttam/)
* #[mounttamalpais](http://dentedreality.com.au/tags/mounttamalpais/)
* #[mttam](http://dentedreality.com.au/tags/mttam/)
* #[mttamalpais](http://dentedreality.com.au/tags/mttamalpais/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[silhouette](http://dentedreality.com.au/tags/silhouette/)
* #[sun](http://dentedreality.com.au/tags/sun/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/221185817/) [4:41 pm, August 19, 2006](http://dentedreality.com.au/2006/08/19/top-of-the-world/ "4:41 pm") 
jQuery(document).ready(function(){
var gmap\_m85f87473f77db795da40208b0b15d2c9 = {
positions : {
378 : new google.maps.LatLng( '37.903574', '-122.591972' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m85f87473f77db795da40208b0b15d2c9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m85f87473f77db795da40208b0b15d2c9.positions ) {
gmap\_m85f87473f77db795da40208b0b15d2c9.bounds.extend( gmap\_m85f87473f77db795da40208b0b15d2c9.positions[m] );
}
// Render markers
for ( var m in gmap\_m85f87473f77db795da40208b0b15d2c9.positions ) {
gmap\_m85f87473f77db795da40208b0b15d2c9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m85f87473f77db795da40208b0b15d2c9.map,
position : gmap\_m85f87473f77db795da40208b0b15d2c9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m85f87473f77db795da40208b0b15d2c9.map.setCenter( gmap\_m85f87473f77db795da40208b0b15d2c9.positions[378] );
});