---
title: Knives
date: '2011-08-27T09:27:30+00:00'
format: image
service: flickr
tags:
- knives
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6322995099_02df3c958f_o.jpg?resize=607%2C813
---

[![Knives](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6322995099_02df3c958f_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/08/27/knives/) 
# [Knives](http://dentedreality.com.au/2011/08/27/knives/)





* #[knives](http://dentedreality.com.au/tags/knives/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6322995099/) [9:27 am, August 27, 2011](http://dentedreality.com.au/2011/08/27/knives/ "9:27 am") 
jQuery(document).ready(function(){
var gmap\_m35b1dc4d4815728a65260c5fb6167269 = {
positions : {
93 : new google.maps.LatLng( '37.791333', '-122.417667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m35b1dc4d4815728a65260c5fb6167269' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m35b1dc4d4815728a65260c5fb6167269.positions ) {
gmap\_m35b1dc4d4815728a65260c5fb6167269.bounds.extend( gmap\_m35b1dc4d4815728a65260c5fb6167269.positions[m] );
}
// Render markers
for ( var m in gmap\_m35b1dc4d4815728a65260c5fb6167269.positions ) {
gmap\_m35b1dc4d4815728a65260c5fb6167269.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m35b1dc4d4815728a65260c5fb6167269.map,
position : gmap\_m35b1dc4d4815728a65260c5fb6167269.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m35b1dc4d4815728a65260c5fb6167269.map.setCenter( gmap\_m35b1dc4d4815728a65260c5fb6167269.positions[93] );
});