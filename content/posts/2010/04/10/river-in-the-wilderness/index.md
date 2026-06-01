---
title: River in the Wilderness
date: '2010-04-10T08:33:42+00:00'
format: image
service: flickr
tags:
- creek
- river
- tombrown
- trackerschool
- tracking
- trees
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516474144_64008ce874_o.jpg?resize=607%2C455
---

[![River in the Wilderness](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516474144_64008ce874_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/10/river-in-the-wilderness/) 
# [River in the Wilderness](http://dentedreality.com.au/2010/04/10/river-in-the-wilderness/)

Standard class, Tracker School.





* #[creek](http://dentedreality.com.au/tags/creek/)
* #[river](http://dentedreality.com.au/tags/river/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)
* #[trees](http://dentedreality.com.au/tags/trees/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516474144/) [8:33 am, April 10, 2010](http://dentedreality.com.au/2010/04/10/river-in-the-wilderness/ "8:33 am") 
jQuery(document).ready(function(){
var gmap\_m6e92e744ef652be4307825ab9649e0f1 = {
positions : {
42 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6e92e744ef652be4307825ab9649e0f1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6e92e744ef652be4307825ab9649e0f1.positions ) {
gmap\_m6e92e744ef652be4307825ab9649e0f1.bounds.extend( gmap\_m6e92e744ef652be4307825ab9649e0f1.positions[m] );
}
// Render markers
for ( var m in gmap\_m6e92e744ef652be4307825ab9649e0f1.positions ) {
gmap\_m6e92e744ef652be4307825ab9649e0f1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6e92e744ef652be4307825ab9649e0f1.map,
position : gmap\_m6e92e744ef652be4307825ab9649e0f1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6e92e744ef652be4307825ab9649e0f1.map.setCenter( gmap\_m6e92e744ef652be4307825ab9649e0f1.positions[42] );
});