---
title: Tarmac Boarding, LHR
date: '2010-11-10T11:45:19+00:00'
format: image
service: flickr
tags:
- Athens
- automattic
- greece
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5183791122_b3c33fe8e1_o.jpg?resize=607%2C452
---

[![Tarmac Boarding, LHR](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5183791122_b3c33fe8e1_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/11/10/tarmac-boarding-lhr/) 
# [Tarmac Boarding, LHR](http://dentedreality.com.au/2010/11/10/tarmac-boarding-lhr/)





* #[Athens](http://dentedreality.com.au/tags/athens/)
* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[greece](http://dentedreality.com.au/tags/greece/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183791122/) [11:45 am, November 10, 2010](http://dentedreality.com.au/2010/11/10/tarmac-boarding-lhr/ "11:45 am") 
jQuery(document).ready(function(){
var gmap\_m8e0ba9595ee1f812eb9f18494b6e947b = {
positions : {
815 : new google.maps.LatLng( '51.469666', '-0.475167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8e0ba9595ee1f812eb9f18494b6e947b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8e0ba9595ee1f812eb9f18494b6e947b.positions ) {
gmap\_m8e0ba9595ee1f812eb9f18494b6e947b.bounds.extend( gmap\_m8e0ba9595ee1f812eb9f18494b6e947b.positions[m] );
}
// Render markers
for ( var m in gmap\_m8e0ba9595ee1f812eb9f18494b6e947b.positions ) {
gmap\_m8e0ba9595ee1f812eb9f18494b6e947b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8e0ba9595ee1f812eb9f18494b6e947b.map,
position : gmap\_m8e0ba9595ee1f812eb9f18494b6e947b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8e0ba9595ee1f812eb9f18494b6e947b.map.setCenter( gmap\_m8e0ba9595ee1f812eb9f18494b6e947b.positions[815] );
});