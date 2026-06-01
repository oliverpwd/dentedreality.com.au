---
title: ''
date: '2014-12-14T01:13:47+00:00'
format: image
service: instagram
tags:
- nofilter
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/928865_1577658792465624_1660938997_n.jpg?resize=640%2C640
---

[![The Colosseum is pretty impressive #nofilter](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/12/928865_1577658792465624_1660938997_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/12/14/the-colosseum-is-pretty-impressive-nofilter/) 

The Colosseum is pretty impressive #nofilter





* #[nofilter](http://dentedreality.com.au/tags/nofilter/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/wlHxq6imIF/) [1:13 am, December 14, 2014](http://dentedreality.com.au/2014/12/14/the-colosseum-is-pretty-impressive-nofilter/ "1:13 am") 
jQuery(document).ready(function(){
var gmap\_maac13c94de232ba3ace7ba16e9c08914 = {
positions : {
48 : new google.maps.LatLng( '41.890169444', '12.492269444' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maac13c94de232ba3ace7ba16e9c08914' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maac13c94de232ba3ace7ba16e9c08914.positions ) {
gmap\_maac13c94de232ba3ace7ba16e9c08914.bounds.extend( gmap\_maac13c94de232ba3ace7ba16e9c08914.positions[m] );
}
// Render markers
for ( var m in gmap\_maac13c94de232ba3ace7ba16e9c08914.positions ) {
gmap\_maac13c94de232ba3ace7ba16e9c08914.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maac13c94de232ba3ace7ba16e9c08914.map,
position : gmap\_maac13c94de232ba3ace7ba16e9c08914.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maac13c94de232ba3ace7ba16e9c08914.map.setCenter( gmap\_maac13c94de232ba3ace7ba16e9c08914.positions[48] );
});