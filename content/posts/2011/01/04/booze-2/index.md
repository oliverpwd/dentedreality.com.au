---
title: Booze!
date: '2011-01-04T04:56:53+00:00'
format: image
service: flickr
tags:
- alcohol
- beer
- booze
- party
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434712510_4e8b0d4010_o.jpg?resize=607%2C452
---

[![Booze!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434712510_4e8b0d4010_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/04/booze-2/) 
# [Booze!](http://dentedreality.com.au/2011/01/04/booze-2/)





* #[alcohol](http://dentedreality.com.au/tags/alcohol/)
* #[beer](http://dentedreality.com.au/tags/beer/)
* #[booze](http://dentedreality.com.au/tags/booze/)
* #[party](http://dentedreality.com.au/tags/party/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434712510/) [4:56 am, January 4, 2011](http://dentedreality.com.au/2011/01/04/booze-2/ "4:56 am") 
jQuery(document).ready(function(){
var gmap\_m611b71464eeb955f6bcd8a7d615102ed = {
positions : {
785 : new google.maps.LatLng( '-32.053', '115.846499' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m611b71464eeb955f6bcd8a7d615102ed' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m611b71464eeb955f6bcd8a7d615102ed.positions ) {
gmap\_m611b71464eeb955f6bcd8a7d615102ed.bounds.extend( gmap\_m611b71464eeb955f6bcd8a7d615102ed.positions[m] );
}
// Render markers
for ( var m in gmap\_m611b71464eeb955f6bcd8a7d615102ed.positions ) {
gmap\_m611b71464eeb955f6bcd8a7d615102ed.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m611b71464eeb955f6bcd8a7d615102ed.map,
position : gmap\_m611b71464eeb955f6bcd8a7d615102ed.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m611b71464eeb955f6bcd8a7d615102ed.map.setCenter( gmap\_m611b71464eeb955f6bcd8a7d615102ed.positions[785] );
});