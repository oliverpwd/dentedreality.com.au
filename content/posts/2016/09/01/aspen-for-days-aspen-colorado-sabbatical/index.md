---
title: ''
date: '2016-09-01T15:13:51+00:00'
format: image
service: instagram
tags:
- aspen
- colorado
- sabbatical
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14134972_1745754302342950_978559756_n.jpg?fit=640%2C640
---

[![Aspen for days. #aspen #colorado #sabbatical](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14134972_1745754302342950_978559756_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/09/01/aspen-for-days-aspen-colorado-sabbatical/) 

Aspen for days. #aspen #colorado #sabbatical





* #[aspen](http://dentedreality.com.au/tags/aspen/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[sabbatical](http://dentedreality.com.au/tags/sabbatical/)

Posted on [Instagram](https://www.instagram.com/p/BJ0_dmxgWl9/) [3:13 pm, September 1, 2016](http://dentedreality.com.au/2016/09/01/aspen-for-days-aspen-colorado-sabbatical/ "3:13 pm") 
jQuery(document).ready(function(){
var gmap\_m41075f180d26a004dd69595fbe4338a0 = {
positions : {
743 : new google.maps.LatLng( '39.83561857', '-106.31805081' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m41075f180d26a004dd69595fbe4338a0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m41075f180d26a004dd69595fbe4338a0.positions ) {
gmap\_m41075f180d26a004dd69595fbe4338a0.bounds.extend( gmap\_m41075f180d26a004dd69595fbe4338a0.positions[m] );
}
// Render markers
for ( var m in gmap\_m41075f180d26a004dd69595fbe4338a0.positions ) {
gmap\_m41075f180d26a004dd69595fbe4338a0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m41075f180d26a004dd69595fbe4338a0.map,
position : gmap\_m41075f180d26a004dd69595fbe4338a0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m41075f180d26a004dd69595fbe4338a0.map.setCenter( gmap\_m41075f180d26a004dd69595fbe4338a0.positions[743] );
});