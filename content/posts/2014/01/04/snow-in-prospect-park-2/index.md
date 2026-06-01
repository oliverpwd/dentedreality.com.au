---
title: Snow in Prospect Park
date: '2014-01-04T09:47:40+00:00'
format: image
service: flickr
tags:
- brooklyn
- newyork
- prospectpark
- snow
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13925196774_1e21997101_o.jpg?resize=607%2C809
---

[![Snow in Prospect Park](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13925196774_1e21997101_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2014/01/04/snow-in-prospect-park-2/) 
# [Snow in Prospect Park](http://dentedreality.com.au/2014/01/04/snow-in-prospect-park-2/)





* #[brooklyn](http://dentedreality.com.au/tags/brooklyn/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[prospectpark](http://dentedreality.com.au/tags/prospectpark/)
* #[snow](http://dentedreality.com.au/tags/snow/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13925196774/) [9:47 am, January 4, 2014](http://dentedreality.com.au/2014/01/04/snow-in-prospect-park-2/ "9:47 am") 
jQuery(document).ready(function(){
var gmap\_mba936a1510489c89cd36f029ae69c75a = {
positions : {
523 : new google.maps.LatLng( '40.66848', '-73.970803' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mba936a1510489c89cd36f029ae69c75a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mba936a1510489c89cd36f029ae69c75a.positions ) {
gmap\_mba936a1510489c89cd36f029ae69c75a.bounds.extend( gmap\_mba936a1510489c89cd36f029ae69c75a.positions[m] );
}
// Render markers
for ( var m in gmap\_mba936a1510489c89cd36f029ae69c75a.positions ) {
gmap\_mba936a1510489c89cd36f029ae69c75a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mba936a1510489c89cd36f029ae69c75a.map,
position : gmap\_mba936a1510489c89cd36f029ae69c75a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mba936a1510489c89cd36f029ae69c75a.map.setCenter( gmap\_mba936a1510489c89cd36f029ae69c75a.positions[523] );
});