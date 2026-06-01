---
title: Me and Kai
date: '2014-03-22T04:51:05+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- kai
- me
- mooloolaba
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927903643_97c0847cef_o.jpg?resize=607%2C455
---

[![Me and Kai](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927903643_97c0847cef_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/22/me-and-kai/) 
# [Me and Kai](http://dentedreality.com.au/2014/03/22/me-and-kai/)

Perth, Mooloolaba and Melbourne





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[kai](http://dentedreality.com.au/tags/kai/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[mooloolaba](http://dentedreality.com.au/tags/mooloolaba/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927903643/) [4:51 am, March 22, 2014](http://dentedreality.com.au/2014/03/22/me-and-kai/ "4:51 am") 
jQuery(document).ready(function(){
var gmap\_m7967673b711a61aa5901261959410089 = {
positions : {
278 : new google.maps.LatLng( '-26.682903', '153.118469' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7967673b711a61aa5901261959410089' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7967673b711a61aa5901261959410089.positions ) {
gmap\_m7967673b711a61aa5901261959410089.bounds.extend( gmap\_m7967673b711a61aa5901261959410089.positions[m] );
}
// Render markers
for ( var m in gmap\_m7967673b711a61aa5901261959410089.positions ) {
gmap\_m7967673b711a61aa5901261959410089.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7967673b711a61aa5901261959410089.map,
position : gmap\_m7967673b711a61aa5901261959410089.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7967673b711a61aa5901261959410089.map.setCenter( gmap\_m7967673b711a61aa5901261959410089.positions[278] );
});