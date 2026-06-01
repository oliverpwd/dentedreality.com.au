---
title: Sara is Geeky
date: '2011-03-15T19:34:34+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2011
- texas
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802657804_b96bde9e54_o.jpg?resize=607%2C813
---

[![Sara is Geeky](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802657804_b96bde9e54_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/03/15/sara-is-geeky/) 
# [Sara is Geeky](http://dentedreality.com.au/2011/03/15/sara-is-geeky/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2011](http://dentedreality.com.au/tags/sxsw2011/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802657804/) [7:34 pm, March 15, 2011](http://dentedreality.com.au/2011/03/15/sara-is-geeky/ "7:34 pm") 
jQuery(document).ready(function(){
var gmap\_mb11f4edd6a9f8a9f1e231a859a9d4f93 = {
positions : {
122 : new google.maps.LatLng( '30.2675', '-97.7405' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb11f4edd6a9f8a9f1e231a859a9d4f93' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb11f4edd6a9f8a9f1e231a859a9d4f93.positions ) {
gmap\_mb11f4edd6a9f8a9f1e231a859a9d4f93.bounds.extend( gmap\_mb11f4edd6a9f8a9f1e231a859a9d4f93.positions[m] );
}
// Render markers
for ( var m in gmap\_mb11f4edd6a9f8a9f1e231a859a9d4f93.positions ) {
gmap\_mb11f4edd6a9f8a9f1e231a859a9d4f93.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb11f4edd6a9f8a9f1e231a859a9d4f93.map,
position : gmap\_mb11f4edd6a9f8a9f1e231a859a9d4f93.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb11f4edd6a9f8a9f1e231a859a9d4f93.map.setCenter( gmap\_mb11f4edd6a9f8a9f1e231a859a9d4f93.positions[122] );
});