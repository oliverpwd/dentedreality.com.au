---
title: Pink Sky
date: '2010-11-23T13:00:15+00:00'
format: image
service: flickr
tags:
- clouds
- color
- light
- pink
- sky
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434636048_6d4ec419fc_o.jpg?resize=607%2C452
---

[![Pink Sky](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434636048_6d4ec419fc_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/11/23/pink-sky/) 
# [Pink Sky](http://dentedreality.com.au/2010/11/23/pink-sky/)





* #[clouds](http://dentedreality.com.au/tags/clouds/)
* #[color](http://dentedreality.com.au/tags/color/)
* #[light](http://dentedreality.com.au/tags/light/)
* #[pink](http://dentedreality.com.au/tags/pink/)
* #[sky](http://dentedreality.com.au/tags/sky/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434636048/) [1:00 pm, November 23, 2010](http://dentedreality.com.au/2010/11/23/pink-sky/ "1:00 pm") 
jQuery(document).ready(function(){
var gmap\_me854eb4fd79046223559d8fb13dde206 = {
positions : {
63 : new google.maps.LatLng( '37.782833', '-122.388334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me854eb4fd79046223559d8fb13dde206' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me854eb4fd79046223559d8fb13dde206.positions ) {
gmap\_me854eb4fd79046223559d8fb13dde206.bounds.extend( gmap\_me854eb4fd79046223559d8fb13dde206.positions[m] );
}
// Render markers
for ( var m in gmap\_me854eb4fd79046223559d8fb13dde206.positions ) {
gmap\_me854eb4fd79046223559d8fb13dde206.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me854eb4fd79046223559d8fb13dde206.map,
position : gmap\_me854eb4fd79046223559d8fb13dde206.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me854eb4fd79046223559d8fb13dde206.map.setCenter( gmap\_me854eb4fd79046223559d8fb13dde206.positions[63] );
});