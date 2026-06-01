---
title: Oslo
date: '2011-10-29T10:01:51+00:00'
format: image
service: flickr
tags:
- norway
- Oslo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6958278511_e10a97d661_o.jpg?resize=607%2C452
---

[![Oslo](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6958278511_e10a97d661_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/10/29/oslo/) 
# [Oslo](http://dentedreality.com.au/2011/10/29/oslo/)





* #[norway](http://dentedreality.com.au/tags/norway/)
* #[Oslo](http://dentedreality.com.au/tags/oslo/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958278511/) [10:01 am, October 29, 2011](http://dentedreality.com.au/2011/10/29/oslo/ "10:01 am") 
jQuery(document).ready(function(){
var gmap\_m0ab750d565fdc846575c7a526399c3df = {
positions : {
314 : new google.maps.LatLng( '59.964666', '10.667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0ab750d565fdc846575c7a526399c3df' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0ab750d565fdc846575c7a526399c3df.positions ) {
gmap\_m0ab750d565fdc846575c7a526399c3df.bounds.extend( gmap\_m0ab750d565fdc846575c7a526399c3df.positions[m] );
}
// Render markers
for ( var m in gmap\_m0ab750d565fdc846575c7a526399c3df.positions ) {
gmap\_m0ab750d565fdc846575c7a526399c3df.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0ab750d565fdc846575c7a526399c3df.map,
position : gmap\_m0ab750d565fdc846575c7a526399c3df.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0ab750d565fdc846575c7a526399c3df.map.setCenter( gmap\_m0ab750d565fdc846575c7a526399c3df.positions[314] );
});