---
title: Frankenthumb
date: '2014-01-26T08:29:25+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13924867273_f3009ae493_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13924867273_f3009ae493_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/01/26/frankenthumb-6/) 
# [Frankenthumb](http://dentedreality.com.au/2014/01/26/frankenthumb-6/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924867273/) [8:29 am, January 26, 2014](http://dentedreality.com.au/2014/01/26/frankenthumb-6/ "8:29 am") 
jQuery(document).ready(function(){
var gmap\_m03b7ea4737c17091f79d170860c8dd88 = {
positions : {
662 : new google.maps.LatLng( '40.669413', '-73.984992' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m03b7ea4737c17091f79d170860c8dd88' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m03b7ea4737c17091f79d170860c8dd88.positions ) {
gmap\_m03b7ea4737c17091f79d170860c8dd88.bounds.extend( gmap\_m03b7ea4737c17091f79d170860c8dd88.positions[m] );
}
// Render markers
for ( var m in gmap\_m03b7ea4737c17091f79d170860c8dd88.positions ) {
gmap\_m03b7ea4737c17091f79d170860c8dd88.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m03b7ea4737c17091f79d170860c8dd88.map,
position : gmap\_m03b7ea4737c17091f79d170860c8dd88.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m03b7ea4737c17091f79d170860c8dd88.map.setCenter( gmap\_m03b7ea4737c17091f79d170860c8dd88.positions[662] );
});