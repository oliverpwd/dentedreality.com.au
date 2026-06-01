---
title: Portable Office
date: '2011-03-05T09:59:29+00:00'
format: image
service: flickr
tags:
- cafe
- computer
- desktop
- office
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802061737_4bcda812b2_o.jpg?resize=607%2C813
---

[![Portable Office](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802061737_4bcda812b2_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/03/05/portable-office/) 
# [Portable Office](http://dentedreality.com.au/2011/03/05/portable-office/)

This guy turned up with everything on that table in a massive backpack. Seriously.





* #[cafe](http://dentedreality.com.au/tags/cafe/)
* #[computer](http://dentedreality.com.au/tags/computer/)
* #[desktop](http://dentedreality.com.au/tags/desktop/)
* #[office](http://dentedreality.com.au/tags/office/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802061737/) [9:59 am, March 5, 2011](http://dentedreality.com.au/2011/03/05/portable-office/ "9:59 am") 
jQuery(document).ready(function(){
var gmap\_ma0b7c5185fb7f810b5c302dd3caa225d = {
positions : {
829 : new google.maps.LatLng( '37.788333', '-122.433834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma0b7c5185fb7f810b5c302dd3caa225d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma0b7c5185fb7f810b5c302dd3caa225d.positions ) {
gmap\_ma0b7c5185fb7f810b5c302dd3caa225d.bounds.extend( gmap\_ma0b7c5185fb7f810b5c302dd3caa225d.positions[m] );
}
// Render markers
for ( var m in gmap\_ma0b7c5185fb7f810b5c302dd3caa225d.positions ) {
gmap\_ma0b7c5185fb7f810b5c302dd3caa225d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma0b7c5185fb7f810b5c302dd3caa225d.map,
position : gmap\_ma0b7c5185fb7f810b5c302dd3caa225d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma0b7c5185fb7f810b5c302dd3caa225d.map.setCenter( gmap\_ma0b7c5185fb7f810b5c302dd3caa225d.positions[829] );
});