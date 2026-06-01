---
title: Erika
date: '2012-12-27T11:44:02+00:00'
format: image
service: flickr
tags:
- erika
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8460354970_0d7680c0b0_o.jpg?resize=607%2C452
---

[![Erika](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8460354970_0d7680c0b0_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/12/27/erika/) 
# [Erika](http://dentedreality.com.au/2012/12/27/erika/)





* #[erika](http://dentedreality.com.au/tags/erika/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460354970/) [11:44 am, December 27, 2012](http://dentedreality.com.au/2012/12/27/erika/ "11:44 am") 
jQuery(document).ready(function(){
var gmap\_mb92b14824adaa990b7e49161f6eedb91 = {
positions : {
338 : new google.maps.LatLng( '38.888666', '-77.022834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb92b14824adaa990b7e49161f6eedb91' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb92b14824adaa990b7e49161f6eedb91.positions ) {
gmap\_mb92b14824adaa990b7e49161f6eedb91.bounds.extend( gmap\_mb92b14824adaa990b7e49161f6eedb91.positions[m] );
}
// Render markers
for ( var m in gmap\_mb92b14824adaa990b7e49161f6eedb91.positions ) {
gmap\_mb92b14824adaa990b7e49161f6eedb91.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb92b14824adaa990b7e49161f6eedb91.map,
position : gmap\_mb92b14824adaa990b7e49161f6eedb91.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb92b14824adaa990b7e49161f6eedb91.map.setCenter( gmap\_mb92b14824adaa990b7e49161f6eedb91.positions[338] );
});