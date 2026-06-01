---
title: Thanksgiving 2012
date: '2012-11-22T11:59:53+00:00'
format: image
service: flickr
tags:
- erika
- food
- thanksgiving
- tray
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8459273093_4b693af2d5_o.jpg?resize=607%2C813
---

[![Thanksgiving 2012](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8459273093_4b693af2d5_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/11/22/thanksgiving-2012-2/) 
# [Thanksgiving 2012](http://dentedreality.com.au/2012/11/22/thanksgiving-2012-2/)





* #[erika](http://dentedreality.com.au/tags/erika/)
* #[food](http://dentedreality.com.au/tags/food/)
* #[thanksgiving](http://dentedreality.com.au/tags/thanksgiving/)
* #[tray](http://dentedreality.com.au/tags/tray/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8459273093/) [11:59 am, November 22, 2012](http://dentedreality.com.au/2012/11/22/thanksgiving-2012-2/ "11:59 am") 
jQuery(document).ready(function(){
var gmap\_ma10099af9bc99db833e3894d9ea1469c = {
positions : {
252 : new google.maps.LatLng( '39.080833', '-77.4725' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma10099af9bc99db833e3894d9ea1469c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma10099af9bc99db833e3894d9ea1469c.positions ) {
gmap\_ma10099af9bc99db833e3894d9ea1469c.bounds.extend( gmap\_ma10099af9bc99db833e3894d9ea1469c.positions[m] );
}
// Render markers
for ( var m in gmap\_ma10099af9bc99db833e3894d9ea1469c.positions ) {
gmap\_ma10099af9bc99db833e3894d9ea1469c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma10099af9bc99db833e3894d9ea1469c.map,
position : gmap\_ma10099af9bc99db833e3894d9ea1469c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma10099af9bc99db833e3894d9ea1469c.map.setCenter( gmap\_ma10099af9bc99db833e3894d9ea1469c.positions[252] );
});