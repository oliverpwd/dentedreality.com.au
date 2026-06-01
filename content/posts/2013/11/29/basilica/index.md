---
title: Basilica
date: '2013-11-29T03:10:43+00:00'
format: image
service: flickr
tags:
- france
- paris
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13923464795_45affd674a_o.jpg?resize=607%2C809
---

[![Basilica](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13923464795_45affd674a_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2013/11/29/basilica/) 
# [Basilica](http://dentedreality.com.au/2013/11/29/basilica/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13923464795/) [3:10 am, November 29, 2013](http://dentedreality.com.au/2013/11/29/basilica/ "3:10 am") 
jQuery(document).ready(function(){
var gmap\_mdfe644c9a851dfb560bd2a179576237a = {
positions : {
488 : new google.maps.LatLng( '48.886383', '2.343033' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdfe644c9a851dfb560bd2a179576237a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdfe644c9a851dfb560bd2a179576237a.positions ) {
gmap\_mdfe644c9a851dfb560bd2a179576237a.bounds.extend( gmap\_mdfe644c9a851dfb560bd2a179576237a.positions[m] );
}
// Render markers
for ( var m in gmap\_mdfe644c9a851dfb560bd2a179576237a.positions ) {
gmap\_mdfe644c9a851dfb560bd2a179576237a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdfe644c9a851dfb560bd2a179576237a.map,
position : gmap\_mdfe644c9a851dfb560bd2a179576237a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdfe644c9a851dfb560bd2a179576237a.map.setCenter( gmap\_mdfe644c9a851dfb560bd2a179576237a.positions[488] );
});