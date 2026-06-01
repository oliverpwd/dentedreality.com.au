---
title: Denver Meetup
date: '2013-11-17T17:24:02+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291697866_d8feba2031_o.jpg?resize=607%2C455
---

[![Denver Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291697866_d8feba2031_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/17/denver-meetup-14/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/17/denver-meetup-14/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291697866/) [5:24 pm, November 17, 2013](http://dentedreality.com.au/2013/11/17/denver-meetup-14/ "5:24 pm") 
jQuery(document).ready(function(){
var gmap\_m211774feab8721388e231f9e4582850f = {
positions : {
121 : new google.maps.LatLng( '39.695611', '-104.938553' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m211774feab8721388e231f9e4582850f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m211774feab8721388e231f9e4582850f.positions ) {
gmap\_m211774feab8721388e231f9e4582850f.bounds.extend( gmap\_m211774feab8721388e231f9e4582850f.positions[m] );
}
// Render markers
for ( var m in gmap\_m211774feab8721388e231f9e4582850f.positions ) {
gmap\_m211774feab8721388e231f9e4582850f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m211774feab8721388e231f9e4582850f.map,
position : gmap\_m211774feab8721388e231f9e4582850f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m211774feab8721388e231f9e4582850f.map.setCenter( gmap\_m211774feab8721388e231f9e4582850f.positions[121] );
});