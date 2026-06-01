---
title: Automatticians
date: '2011-03-15T20:29:21+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2011
- texas
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802658130_9ea739cc44_o.jpg?resize=607%2C452
---

[![Automatticians](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802658130_9ea739cc44_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/03/15/automatticians-2/) 
# [Automatticians](http://dentedreality.com.au/2011/03/15/automatticians-2/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2011](http://dentedreality.com.au/tags/sxsw2011/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802658130/) [8:29 pm, March 15, 2011](http://dentedreality.com.au/2011/03/15/automatticians-2/ "8:29 pm") 
jQuery(document).ready(function(){
var gmap\_m78855259a47505c730fbb2067449d453 = {
positions : {
900 : new google.maps.LatLng( '30.267833', '-97.740334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m78855259a47505c730fbb2067449d453' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m78855259a47505c730fbb2067449d453.positions ) {
gmap\_m78855259a47505c730fbb2067449d453.bounds.extend( gmap\_m78855259a47505c730fbb2067449d453.positions[m] );
}
// Render markers
for ( var m in gmap\_m78855259a47505c730fbb2067449d453.positions ) {
gmap\_m78855259a47505c730fbb2067449d453.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m78855259a47505c730fbb2067449d453.map,
position : gmap\_m78855259a47505c730fbb2067449d453.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m78855259a47505c730fbb2067449d453.map.setCenter( gmap\_m78855259a47505c730fbb2067449d453.positions[900] );
});