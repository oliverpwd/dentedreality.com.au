---
title: Cott Sunset
date: '2011-01-22T15:19:27+00:00'
format: image
service: flickr
tags:
- australia
- beach
- cottesloe
- sunset
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434790146_051e010910_o.jpg?resize=607%2C452
---

[![Cott Sunset](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434790146_051e010910_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/22/cott-sunset-3/) 
# [Cott Sunset](http://dentedreality.com.au/2011/01/22/cott-sunset-3/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[cottesloe](http://dentedreality.com.au/tags/cottesloe/)
* #[sunset](http://dentedreality.com.au/tags/sunset/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434790146/) [3:19 pm, January 22, 2011](http://dentedreality.com.au/2011/01/22/cott-sunset-3/ "3:19 pm") 
jQuery(document).ready(function(){
var gmap\_m0741d56ac023d768f366a39a4d0e0044 = {
positions : {
257 : new google.maps.LatLng( '-31.994501', '115.751333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0741d56ac023d768f366a39a4d0e0044' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0741d56ac023d768f366a39a4d0e0044.positions ) {
gmap\_m0741d56ac023d768f366a39a4d0e0044.bounds.extend( gmap\_m0741d56ac023d768f366a39a4d0e0044.positions[m] );
}
// Render markers
for ( var m in gmap\_m0741d56ac023d768f366a39a4d0e0044.positions ) {
gmap\_m0741d56ac023d768f366a39a4d0e0044.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0741d56ac023d768f366a39a4d0e0044.map,
position : gmap\_m0741d56ac023d768f366a39a4d0e0044.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0741d56ac023d768f366a39a4d0e0044.map.setCenter( gmap\_m0741d56ac023d768f366a39a4d0e0044.positions[257] );
});