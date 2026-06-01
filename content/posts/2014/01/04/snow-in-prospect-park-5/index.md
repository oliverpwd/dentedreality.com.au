---
title: Snow in Prospect Park
date: '2014-01-04T09:40:51+00:00'
format: image
service: flickr
tags:
- brooklyn
- newyork
- prospectpark
- snow
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901631406_1da51780b1_o.jpg?resize=607%2C455
---

[![Snow in Prospect Park](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901631406_1da51780b1_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/01/04/snow-in-prospect-park-5/) 
# [Snow in Prospect Park](http://dentedreality.com.au/2014/01/04/snow-in-prospect-park-5/)





* #[brooklyn](http://dentedreality.com.au/tags/brooklyn/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[prospectpark](http://dentedreality.com.au/tags/prospectpark/)
* #[snow](http://dentedreality.com.au/tags/snow/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901631406/) [9:40 am, January 4, 2014](http://dentedreality.com.au/2014/01/04/snow-in-prospect-park-5/ "9:40 am") 
jQuery(document).ready(function(){
var gmap\_mdd37ad016fd37a5176c876e18ea40e42 = {
positions : {
95 : new google.maps.LatLng( '40.668005', '-73.97262' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdd37ad016fd37a5176c876e18ea40e42' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdd37ad016fd37a5176c876e18ea40e42.positions ) {
gmap\_mdd37ad016fd37a5176c876e18ea40e42.bounds.extend( gmap\_mdd37ad016fd37a5176c876e18ea40e42.positions[m] );
}
// Render markers
for ( var m in gmap\_mdd37ad016fd37a5176c876e18ea40e42.positions ) {
gmap\_mdd37ad016fd37a5176c876e18ea40e42.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdd37ad016fd37a5176c876e18ea40e42.map,
position : gmap\_mdd37ad016fd37a5176c876e18ea40e42.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdd37ad016fd37a5176c876e18ea40e42.map.setCenter( gmap\_mdd37ad016fd37a5176c876e18ea40e42.positions[95] );
});