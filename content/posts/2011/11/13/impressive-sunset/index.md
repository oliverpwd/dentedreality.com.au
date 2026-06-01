---
title: Impressive Sunset
date: '2011-11-13T13:08:52+00:00'
format: image
service: flickr
tags:
- clouds
- sanfrancisco
- sky
- sunset
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6958311503_d4a2e868ee_o.jpg?resize=607%2C452
---

[![Impressive Sunset](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6958311503_d4a2e868ee_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/11/13/impressive-sunset/) 
# [Impressive Sunset](http://dentedreality.com.au/2011/11/13/impressive-sunset/)





* #[clouds](http://dentedreality.com.au/tags/clouds/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[sky](http://dentedreality.com.au/tags/sky/)
* #[sunset](http://dentedreality.com.au/tags/sunset/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958311503/) [1:08 pm, November 13, 2011](http://dentedreality.com.au/2011/11/13/impressive-sunset/ "1:08 pm") 
jQuery(document).ready(function(){
var gmap\_md9660a2073cdfa8c1f6e5785c9a23e42 = {
positions : {
780 : new google.maps.LatLng( '37.8075', '-122.421' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md9660a2073cdfa8c1f6e5785c9a23e42' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md9660a2073cdfa8c1f6e5785c9a23e42.positions ) {
gmap\_md9660a2073cdfa8c1f6e5785c9a23e42.bounds.extend( gmap\_md9660a2073cdfa8c1f6e5785c9a23e42.positions[m] );
}
// Render markers
for ( var m in gmap\_md9660a2073cdfa8c1f6e5785c9a23e42.positions ) {
gmap\_md9660a2073cdfa8c1f6e5785c9a23e42.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md9660a2073cdfa8c1f6e5785c9a23e42.map,
position : gmap\_md9660a2073cdfa8c1f6e5785c9a23e42.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md9660a2073cdfa8c1f6e5785c9a23e42.map.setCenter( gmap\_md9660a2073cdfa8c1f6e5785c9a23e42.positions[780] );
});