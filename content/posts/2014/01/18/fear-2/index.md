---
title: Fear
date: '2014-01-18T17:23:11+00:00'
format: image
service: flickr
tags:
- erika
- fear
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13926947585_bf904d5153_o.jpg?resize=607%2C455
---

[![Fear](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13926947585_bf904d5153_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/01/18/fear-2/) 
# [Fear](http://dentedreality.com.au/2014/01/18/fear-2/)





* #[erika](http://dentedreality.com.au/tags/erika/)
* #[fear](http://dentedreality.com.au/tags/fear/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13926947585/) [5:23 pm, January 18, 2014](http://dentedreality.com.au/2014/01/18/fear-2/ "5:23 pm") 
jQuery(document).ready(function(){
var gmap\_m0e057e04c9c743b68176243b684ef781 = {
positions : {
510 : new google.maps.LatLng( '40.686977', '-73.977623' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0e057e04c9c743b68176243b684ef781' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0e057e04c9c743b68176243b684ef781.positions ) {
gmap\_m0e057e04c9c743b68176243b684ef781.bounds.extend( gmap\_m0e057e04c9c743b68176243b684ef781.positions[m] );
}
// Render markers
for ( var m in gmap\_m0e057e04c9c743b68176243b684ef781.positions ) {
gmap\_m0e057e04c9c743b68176243b684ef781.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0e057e04c9c743b68176243b684ef781.map,
position : gmap\_m0e057e04c9c743b68176243b684ef781.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0e057e04c9c743b68176243b684ef781.map.setCenter( gmap\_m0e057e04c9c743b68176243b684ef781.positions[510] );
});