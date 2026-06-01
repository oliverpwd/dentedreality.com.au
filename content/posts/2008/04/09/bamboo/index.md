---
title: Bamboo!
date: '2008-04-09T16:50:43+00:00'
format: image
service: flickr
tags:
- australia
- bamboo
- botanicalgardens
- sydney
- wallpaper
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2437447250_6cdf1f266e_o.jpg?resize=607%2C455
---

[![Bamboo!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2437447250_6cdf1f266e_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2008/04/09/bamboo/) 
# [Bamboo!](http://dentedreality.com.au/2008/04/09/bamboo/)

I <3 Bamboo





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[bamboo](http://dentedreality.com.au/tags/bamboo/)
* #[botanicalgardens](http://dentedreality.com.au/tags/botanicalgardens/)
* #[sydney](http://dentedreality.com.au/tags/sydney/)
* #[wallpaper](http://dentedreality.com.au/tags/wallpaper/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2437447250/) [4:50 pm, April 9, 2008](http://dentedreality.com.au/2008/04/09/bamboo/ "4:50 pm") 
jQuery(document).ready(function(){
var gmap\_m2fb17a1b1930f64446564b67afadf24a = {
positions : {
612 : new google.maps.LatLng( '-33.871555', '151.226291' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2fb17a1b1930f64446564b67afadf24a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2fb17a1b1930f64446564b67afadf24a.positions ) {
gmap\_m2fb17a1b1930f64446564b67afadf24a.bounds.extend( gmap\_m2fb17a1b1930f64446564b67afadf24a.positions[m] );
}
// Render markers
for ( var m in gmap\_m2fb17a1b1930f64446564b67afadf24a.positions ) {
gmap\_m2fb17a1b1930f64446564b67afadf24a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2fb17a1b1930f64446564b67afadf24a.map,
position : gmap\_m2fb17a1b1930f64446564b67afadf24a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2fb17a1b1930f64446564b67afadf24a.map.setCenter( gmap\_m2fb17a1b1930f64446564b67afadf24a.positions[612] );
});