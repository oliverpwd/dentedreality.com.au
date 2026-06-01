---
title: Distant Bridge
date: '2008-04-10T16:26:07+00:00'
format: image
service: flickr
tags:
- australia
- bridge
- kayaking
- sydney
- sydneybay
- sydneyharbourbridge
- water
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2437459520_2e61038844_o.jpg?resize=607%2C455
---

[![Distant Bridge](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2437459520_2e61038844_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2008/04/10/distant-bridge/) 
# [Distant Bridge](http://dentedreality.com.au/2008/04/10/distant-bridge/)

We rented kayaks at Rose Bay and kayaked around the point to get a snack.





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[bridge](http://dentedreality.com.au/tags/bridge/)
* #[kayaking](http://dentedreality.com.au/tags/kayaking/)
* #[sydney](http://dentedreality.com.au/tags/sydney/)
* #[sydneybay](http://dentedreality.com.au/tags/sydneybay/)
* #[sydneyharbourbridge](http://dentedreality.com.au/tags/sydneyharbourbridge/)
* #[water](http://dentedreality.com.au/tags/water/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2437459520/) [4:26 pm, April 10, 2008](http://dentedreality.com.au/2008/04/10/distant-bridge/ "4:26 pm") 
jQuery(document).ready(function(){
var gmap\_m4bf01a2db3102e2d52a3a0bf53175a2f = {
positions : {
31 : new google.maps.LatLng( '-33.874548', '151.261997' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4bf01a2db3102e2d52a3a0bf53175a2f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4bf01a2db3102e2d52a3a0bf53175a2f.positions ) {
gmap\_m4bf01a2db3102e2d52a3a0bf53175a2f.bounds.extend( gmap\_m4bf01a2db3102e2d52a3a0bf53175a2f.positions[m] );
}
// Render markers
for ( var m in gmap\_m4bf01a2db3102e2d52a3a0bf53175a2f.positions ) {
gmap\_m4bf01a2db3102e2d52a3a0bf53175a2f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4bf01a2db3102e2d52a3a0bf53175a2f.map,
position : gmap\_m4bf01a2db3102e2d52a3a0bf53175a2f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4bf01a2db3102e2d52a3a0bf53175a2f.map.setCenter( gmap\_m4bf01a2db3102e2d52a3a0bf53175a2f.positions[31] );
});