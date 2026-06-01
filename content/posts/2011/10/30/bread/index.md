---
title: Bread
date: '2011-10-30T07:52:02+00:00'
format: image
service: flickr
tags:
- bread
- norway
- Oslo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812169402_665ddaca93_o.jpg?resize=607%2C452
---

[![Bread](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812169402_665ddaca93_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/10/30/bread/) 
# [Bread](http://dentedreality.com.au/2011/10/30/bread/)





* #[bread](http://dentedreality.com.au/tags/bread/)
* #[norway](http://dentedreality.com.au/tags/norway/)
* #[Oslo](http://dentedreality.com.au/tags/oslo/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812169402/) [7:52 am, October 30, 2011](http://dentedreality.com.au/2011/10/30/bread/ "7:52 am") 
jQuery(document).ready(function(){
var gmap\_m80d3b92cbe635fc30b63714d4723985e = {
positions : {
715 : new google.maps.LatLng( '59.913833', '10.735999' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m80d3b92cbe635fc30b63714d4723985e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m80d3b92cbe635fc30b63714d4723985e.positions ) {
gmap\_m80d3b92cbe635fc30b63714d4723985e.bounds.extend( gmap\_m80d3b92cbe635fc30b63714d4723985e.positions[m] );
}
// Render markers
for ( var m in gmap\_m80d3b92cbe635fc30b63714d4723985e.positions ) {
gmap\_m80d3b92cbe635fc30b63714d4723985e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m80d3b92cbe635fc30b63714d4723985e.map,
position : gmap\_m80d3b92cbe635fc30b63714d4723985e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m80d3b92cbe635fc30b63714d4723985e.map.setCenter( gmap\_m80d3b92cbe635fc30b63714d4723985e.positions[715] );
});