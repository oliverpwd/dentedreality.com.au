---
title: Leaving Oslo
date: '2011-10-31T10:20:52+00:00'
format: image
service: flickr
tags:
- norway
- Oslo
- plane
- sky
- wing
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812169806_af5a906664_o.jpg?resize=607%2C452
---

[![Leaving Oslo](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812169806_af5a906664_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/10/31/leaving-oslo/) 
# [Leaving Oslo](http://dentedreality.com.au/2011/10/31/leaving-oslo/)





* #[norway](http://dentedreality.com.au/tags/norway/)
* #[Oslo](http://dentedreality.com.au/tags/oslo/)
* #[plane](http://dentedreality.com.au/tags/plane/)
* #[sky](http://dentedreality.com.au/tags/sky/)
* #[wing](http://dentedreality.com.au/tags/wing/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812169806/) [10:20 am, October 31, 2011](http://dentedreality.com.au/2011/10/31/leaving-oslo/ "10:20 am") 
jQuery(document).ready(function(){
var gmap\_m9330c9a600dbd54727ce23f485c53244 = {
positions : {
843 : new google.maps.LatLng( '59.920166', '10.7685' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9330c9a600dbd54727ce23f485c53244' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9330c9a600dbd54727ce23f485c53244.positions ) {
gmap\_m9330c9a600dbd54727ce23f485c53244.bounds.extend( gmap\_m9330c9a600dbd54727ce23f485c53244.positions[m] );
}
// Render markers
for ( var m in gmap\_m9330c9a600dbd54727ce23f485c53244.positions ) {
gmap\_m9330c9a600dbd54727ce23f485c53244.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9330c9a600dbd54727ce23f485c53244.map,
position : gmap\_m9330c9a600dbd54727ce23f485c53244.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9330c9a600dbd54727ce23f485c53244.map.setCenter( gmap\_m9330c9a600dbd54727ce23f485c53244.positions[843] );
});