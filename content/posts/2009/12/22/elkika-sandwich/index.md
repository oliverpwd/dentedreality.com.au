---
title: Elkika Sandwich
date: '2009-12-22T09:33:40+00:00'
format: image
service: flickr
tags:
- Chile
- elkika
- sandwich
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2009/12/4248113312_335ac731f4_o.jpg?resize=607%2C455
---

[![Elkika Sandwich](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2009/12/4248113312_335ac731f4_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2009/12/22/elkika-sandwich/) 
# [Elkika Sandwich](http://dentedreality.com.au/2009/12/22/elkika-sandwich/)





* #[Chile](http://dentedreality.com.au/tags/chile/)
* #[elkika](http://dentedreality.com.au/tags/elkika/)
* #[sandwich](http://dentedreality.com.au/tags/sandwich/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4248113312/) [9:33 am, December 22, 2009](http://dentedreality.com.au/2009/12/22/elkika-sandwich/ "9:33 am") 
jQuery(document).ready(function(){
var gmap\_m5c3598290b10daeadf80f6326fea38e4 = {
positions : {
279 : new google.maps.LatLng( '-33.425834', '-70.6125' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5c3598290b10daeadf80f6326fea38e4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5c3598290b10daeadf80f6326fea38e4.positions ) {
gmap\_m5c3598290b10daeadf80f6326fea38e4.bounds.extend( gmap\_m5c3598290b10daeadf80f6326fea38e4.positions[m] );
}
// Render markers
for ( var m in gmap\_m5c3598290b10daeadf80f6326fea38e4.positions ) {
gmap\_m5c3598290b10daeadf80f6326fea38e4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5c3598290b10daeadf80f6326fea38e4.map,
position : gmap\_m5c3598290b10daeadf80f6326fea38e4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5c3598290b10daeadf80f6326fea38e4.map.setCenter( gmap\_m5c3598290b10daeadf80f6326fea38e4.positions[279] );
});