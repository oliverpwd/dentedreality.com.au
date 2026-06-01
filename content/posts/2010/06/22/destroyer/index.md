---
title: Destroyer
date: '2010-06-22T11:03:43+00:00'
format: image
service: flickr
tags:
- boat
- destroyer
- ship
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/06/4747653185_e86227cec5_o.jpg?resize=607%2C455
---

[![Destroyer](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/06/4747653185_e86227cec5_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/06/22/destroyer/) 
# [Destroyer](http://dentedreality.com.au/2010/06/22/destroyer/)





* #[boat](http://dentedreality.com.au/tags/boat/)
* #[destroyer](http://dentedreality.com.au/tags/destroyer/)
* #[ship](http://dentedreality.com.au/tags/ship/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4747653185/) [11:03 am, June 22, 2010](http://dentedreality.com.au/2010/06/22/destroyer/ "11:03 am") 
jQuery(document).ready(function(){
var gmap\_mf35129d6299fe913a0f7109c51ff71ea = {
positions : {
208 : new google.maps.LatLng( '37.784666', '-122.388167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf35129d6299fe913a0f7109c51ff71ea' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf35129d6299fe913a0f7109c51ff71ea.positions ) {
gmap\_mf35129d6299fe913a0f7109c51ff71ea.bounds.extend( gmap\_mf35129d6299fe913a0f7109c51ff71ea.positions[m] );
}
// Render markers
for ( var m in gmap\_mf35129d6299fe913a0f7109c51ff71ea.positions ) {
gmap\_mf35129d6299fe913a0f7109c51ff71ea.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf35129d6299fe913a0f7109c51ff71ea.map,
position : gmap\_mf35129d6299fe913a0f7109c51ff71ea.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf35129d6299fe913a0f7109c51ff71ea.map.setCenter( gmap\_mf35129d6299fe913a0f7109c51ff71ea.positions[208] );
});