---
title: Frankenthumb
date: '2014-01-05T08:31:08+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901682036_fbdf472948_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901682036_fbdf472948_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/01/05/frankenthumb-22/) 
# [Frankenthumb](http://dentedreality.com.au/2014/01/05/frankenthumb-22/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901682036/) [8:31 am, January 5, 2014](http://dentedreality.com.au/2014/01/05/frankenthumb-22/ "8:31 am") 
jQuery(document).ready(function(){
var gmap\_m89a9a520362414200155f4162b107ed7 = {
positions : {
815 : new google.maps.LatLng( '40.670138', '-73.985603' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m89a9a520362414200155f4162b107ed7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m89a9a520362414200155f4162b107ed7.positions ) {
gmap\_m89a9a520362414200155f4162b107ed7.bounds.extend( gmap\_m89a9a520362414200155f4162b107ed7.positions[m] );
}
// Render markers
for ( var m in gmap\_m89a9a520362414200155f4162b107ed7.positions ) {
gmap\_m89a9a520362414200155f4162b107ed7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m89a9a520362414200155f4162b107ed7.map,
position : gmap\_m89a9a520362414200155f4162b107ed7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m89a9a520362414200155f4162b107ed7.map.setCenter( gmap\_m89a9a520362414200155f4162b107ed7.positions[815] );
});