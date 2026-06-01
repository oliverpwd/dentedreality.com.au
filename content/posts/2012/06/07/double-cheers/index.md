---
title: Double Cheers!
date: '2012-06-07T19:06:35+00:00'
format: image
service: flickr
tags:
- chexee
- jaquith
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7911182104_78f518ef23_o.jpg?resize=607%2C452
---

[![Double Cheers!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7911182104_78f518ef23_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/06/07/double-cheers/) 
# [Double Cheers!](http://dentedreality.com.au/2012/06/07/double-cheers/)

At McSorley’s Ale House





* #[chexee](http://dentedreality.com.au/tags/chexee/)
* #[jaquith](http://dentedreality.com.au/tags/jaquith/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7911182104/) [7:06 pm, June 7, 2012](http://dentedreality.com.au/2012/06/07/double-cheers/ "7:06 pm") 
jQuery(document).ready(function(){
var gmap\_ma36138f1ed71bc6dd1f86ef1c85148a0 = {
positions : {
734 : new google.maps.LatLng( '40.7285', '-73.99' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma36138f1ed71bc6dd1f86ef1c85148a0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma36138f1ed71bc6dd1f86ef1c85148a0.positions ) {
gmap\_ma36138f1ed71bc6dd1f86ef1c85148a0.bounds.extend( gmap\_ma36138f1ed71bc6dd1f86ef1c85148a0.positions[m] );
}
// Render markers
for ( var m in gmap\_ma36138f1ed71bc6dd1f86ef1c85148a0.positions ) {
gmap\_ma36138f1ed71bc6dd1f86ef1c85148a0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma36138f1ed71bc6dd1f86ef1c85148a0.map,
position : gmap\_ma36138f1ed71bc6dd1f86ef1c85148a0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma36138f1ed71bc6dd1f86ef1c85148a0.map.setCenter( gmap\_ma36138f1ed71bc6dd1f86ef1c85148a0.positions[734] );
});