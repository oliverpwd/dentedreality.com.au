---
title: Dinner
date: '2010-11-21T15:28:23+00:00'
format: image
service: flickr
tags:
- cooking
- food
- lamb
- shank
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434635660_2ce77d6a90_o.jpg?resize=607%2C452
---

[![Dinner](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/11/5434635660_2ce77d6a90_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/11/21/dinner/) 
# [Dinner](http://dentedreality.com.au/2010/11/21/dinner/)





* #[cooking](http://dentedreality.com.au/tags/cooking/)
* #[food](http://dentedreality.com.au/tags/food/)
* #[lamb](http://dentedreality.com.au/tags/lamb/)
* #[shank](http://dentedreality.com.au/tags/shank/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434635660/) [3:28 pm, November 21, 2010](http://dentedreality.com.au/2010/11/21/dinner/ "3:28 pm") 
jQuery(document).ready(function(){
var gmap\_m260232939d6838d8443c17df7657fe7d = {
positions : {
423 : new google.maps.LatLng( '37.791333', '-122.417834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m260232939d6838d8443c17df7657fe7d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m260232939d6838d8443c17df7657fe7d.positions ) {
gmap\_m260232939d6838d8443c17df7657fe7d.bounds.extend( gmap\_m260232939d6838d8443c17df7657fe7d.positions[m] );
}
// Render markers
for ( var m in gmap\_m260232939d6838d8443c17df7657fe7d.positions ) {
gmap\_m260232939d6838d8443c17df7657fe7d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m260232939d6838d8443c17df7657fe7d.map,
position : gmap\_m260232939d6838d8443c17df7657fe7d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m260232939d6838d8443c17df7657fe7d.map.setCenter( gmap\_m260232939d6838d8443c17df7657fe7d.positions[423] );
});