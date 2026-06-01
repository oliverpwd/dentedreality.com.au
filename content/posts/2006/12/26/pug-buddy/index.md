---
title: Pug Buddy
date: '2006-12-26T19:34:12+00:00'
format: image
service: flickr
tags:
- phuket
- pug
- pugdog
- Sandy
- sleepydog
- thailand
- thailand06
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348103338_1cbfbc0293_o.jpg?resize=607%2C809
---

[![Pug Buddy](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348103338_1cbfbc0293_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2006/12/26/pug-buddy/) 
# [Pug Buddy](http://dentedreality.com.au/2006/12/26/pug-buddy/)

One of our buddies – this is the pug, and there was also a little black sausage-ish dog that hung around the place we stayed all the time.





* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[pug](http://dentedreality.com.au/tags/pug/)
* #[pugdog](http://dentedreality.com.au/tags/pugdog/)
* #[Sandy](http://dentedreality.com.au/tags/sandy/)
* #[sleepydog](http://dentedreality.com.au/tags/sleepydog/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348103338/) [7:34 pm, December 26, 2006](http://dentedreality.com.au/2006/12/26/pug-buddy/ "7:34 pm") 
jQuery(document).ready(function(){
var gmap\_md1ccb65f1a3b7748998815ac1f57a80a = {
positions : {
331 : new google.maps.LatLng( '7.955282', '98.282489' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md1ccb65f1a3b7748998815ac1f57a80a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md1ccb65f1a3b7748998815ac1f57a80a.positions ) {
gmap\_md1ccb65f1a3b7748998815ac1f57a80a.bounds.extend( gmap\_md1ccb65f1a3b7748998815ac1f57a80a.positions[m] );
}
// Render markers
for ( var m in gmap\_md1ccb65f1a3b7748998815ac1f57a80a.positions ) {
gmap\_md1ccb65f1a3b7748998815ac1f57a80a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md1ccb65f1a3b7748998815ac1f57a80a.map,
position : gmap\_md1ccb65f1a3b7748998815ac1f57a80a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md1ccb65f1a3b7748998815ac1f57a80a.map.setCenter( gmap\_md1ccb65f1a3b7748998815ac1f57a80a.positions[331] );
});