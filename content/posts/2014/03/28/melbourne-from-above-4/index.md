---
title: Melbourne From Above
date: '2014-03-28T13:38:07+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904764302_2b40411f37_o.jpg?resize=607%2C455
---

[![Melbourne From Above](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904764302_2b40411f37_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/28/melbourne-from-above-4/) 
# [Melbourne From Above](http://dentedreality.com.au/2014/03/28/melbourne-from-above-4/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904764302/) [1:38 pm, March 28, 2014](http://dentedreality.com.au/2014/03/28/melbourne-from-above-4/ "1:38 pm") 
jQuery(document).ready(function(){
var gmap\_m249fff63cdd037145ae2ac4fef33bee4 = {
positions : {
66 : new google.maps.LatLng( '-37.821442', '144.96443' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m249fff63cdd037145ae2ac4fef33bee4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m249fff63cdd037145ae2ac4fef33bee4.positions ) {
gmap\_m249fff63cdd037145ae2ac4fef33bee4.bounds.extend( gmap\_m249fff63cdd037145ae2ac4fef33bee4.positions[m] );
}
// Render markers
for ( var m in gmap\_m249fff63cdd037145ae2ac4fef33bee4.positions ) {
gmap\_m249fff63cdd037145ae2ac4fef33bee4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m249fff63cdd037145ae2ac4fef33bee4.map,
position : gmap\_m249fff63cdd037145ae2ac4fef33bee4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m249fff63cdd037145ae2ac4fef33bee4.map.setCenter( gmap\_m249fff63cdd037145ae2ac4fef33bee4.positions[66] );
});