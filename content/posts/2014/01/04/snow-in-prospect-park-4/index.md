---
title: Snow in Prospect Park
date: '2014-01-04T09:42:44+00:00'
format: image
service: flickr
tags:
- brooklyn
- newyork
- prospectpark
- snow
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901632196_a7a13fb3fc_o.jpg?resize=607%2C455
---

[![Snow in Prospect Park](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901632196_a7a13fb3fc_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/01/04/snow-in-prospect-park-4/) 
# [Snow in Prospect Park](http://dentedreality.com.au/2014/01/04/snow-in-prospect-park-4/)





* #[brooklyn](http://dentedreality.com.au/tags/brooklyn/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[prospectpark](http://dentedreality.com.au/tags/prospectpark/)
* #[snow](http://dentedreality.com.au/tags/snow/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901632196/) [9:42 am, January 4, 2014](http://dentedreality.com.au/2014/01/04/snow-in-prospect-park-4/ "9:42 am") 
jQuery(document).ready(function(){
var gmap\_mef064e172a13d932917118cc46811553 = {
positions : {
776 : new google.maps.LatLng( '40.66788', '-73.971537' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mef064e172a13d932917118cc46811553' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mef064e172a13d932917118cc46811553.positions ) {
gmap\_mef064e172a13d932917118cc46811553.bounds.extend( gmap\_mef064e172a13d932917118cc46811553.positions[m] );
}
// Render markers
for ( var m in gmap\_mef064e172a13d932917118cc46811553.positions ) {
gmap\_mef064e172a13d932917118cc46811553.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mef064e172a13d932917118cc46811553.map,
position : gmap\_mef064e172a13d932917118cc46811553.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mef064e172a13d932917118cc46811553.map.setCenter( gmap\_mef064e172a13d932917118cc46811553.positions[776] );
});