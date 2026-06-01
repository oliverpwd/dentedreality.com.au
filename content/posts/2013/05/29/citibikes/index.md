---
title: Citibikes!
date: '2013-05-29T09:41:47+00:00'
format: image
service: flickr
tags:
- bicycle
- blue
- citibike
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9439715840_dafa7ef040_o.jpg?resize=607%2C452
---

[![Citibikes!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9439715840_dafa7ef040_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/05/29/citibikes/) 
# [Citibikes!](http://dentedreality.com.au/2013/05/29/citibikes/)

In DUMBO





* #[bicycle](http://dentedreality.com.au/tags/bicycle/)
* #[blue](http://dentedreality.com.au/tags/blue/)
* #[citibike](http://dentedreality.com.au/tags/citibike/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9439715840/) [9:41 am, May 29, 2013](http://dentedreality.com.au/2013/05/29/citibikes/ "9:41 am") 
jQuery(document).ready(function(){
var gmap\_m15b5d453f8d741f522407d50b0ac5399 = {
positions : {
197 : new google.maps.LatLng( '40.703', '-73.988' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m15b5d453f8d741f522407d50b0ac5399' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m15b5d453f8d741f522407d50b0ac5399.positions ) {
gmap\_m15b5d453f8d741f522407d50b0ac5399.bounds.extend( gmap\_m15b5d453f8d741f522407d50b0ac5399.positions[m] );
}
// Render markers
for ( var m in gmap\_m15b5d453f8d741f522407d50b0ac5399.positions ) {
gmap\_m15b5d453f8d741f522407d50b0ac5399.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m15b5d453f8d741f522407d50b0ac5399.map,
position : gmap\_m15b5d453f8d741f522407d50b0ac5399.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m15b5d453f8d741f522407d50b0ac5399.map.setCenter( gmap\_m15b5d453f8d741f522407d50b0ac5399.positions[197] );
});