---
title: Hazelnut/Philbert
date: '2010-04-09T11:49:55+00:00'
format: image
service: flickr
tags:
- hazelnut
- philbert
- plantwalk
- tombrown
- trackerschool
- tracking
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516469838_d26b960557_o.jpg?resize=607%2C809
---

[![Hazelnut/Philbert](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516469838_d26b960557_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2010/04/09/hazelnutphilbert/) 
# [Hazelnut/Philbert](http://dentedreality.com.au/2010/04/09/hazelnutphilbert/)

As seen during our edible/medicinal plant walk.





* #[hazelnut](http://dentedreality.com.au/tags/hazelnut/)
* #[philbert](http://dentedreality.com.au/tags/philbert/)
* #[plantwalk](http://dentedreality.com.au/tags/plantwalk/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516469838/) [11:49 am, April 9, 2010](http://dentedreality.com.au/2010/04/09/hazelnutphilbert/ "11:49 am") 
jQuery(document).ready(function(){
var gmap\_md9a164ee44cc31c5a01622fec0c95f28 = {
positions : {
129 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md9a164ee44cc31c5a01622fec0c95f28' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md9a164ee44cc31c5a01622fec0c95f28.positions ) {
gmap\_md9a164ee44cc31c5a01622fec0c95f28.bounds.extend( gmap\_md9a164ee44cc31c5a01622fec0c95f28.positions[m] );
}
// Render markers
for ( var m in gmap\_md9a164ee44cc31c5a01622fec0c95f28.positions ) {
gmap\_md9a164ee44cc31c5a01622fec0c95f28.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md9a164ee44cc31c5a01622fec0c95f28.map,
position : gmap\_md9a164ee44cc31c5a01622fec0c95f28.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md9a164ee44cc31c5a01622fec0c95f28.map.setCenter( gmap\_md9a164ee44cc31c5a01622fec0c95f28.positions[129] );
});