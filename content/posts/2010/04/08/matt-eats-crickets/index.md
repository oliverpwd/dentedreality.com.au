---
title: Matt Eats Crickets
date: '2010-04-08T10:10:05+00:00'
format: image
service: flickr
tags:
- crickets
- matt
- photomatt
- tombrown
- trackerschool
- tracking
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4515817077_9ab2399aaf_o.jpg?resize=607%2C455
---

[![Matt Eats Crickets](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4515817077_9ab2399aaf_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/08/matt-eats-crickets/) 
# [Matt Eats Crickets](http://dentedreality.com.au/2010/04/08/matt-eats-crickets/)

Standard class, Tracker School.





* #[crickets](http://dentedreality.com.au/tags/crickets/)
* #[matt](http://dentedreality.com.au/tags/matt/)
* #[photomatt](http://dentedreality.com.au/tags/photomatt/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4515817077/) [10:10 am, April 8, 2010](http://dentedreality.com.au/2010/04/08/matt-eats-crickets/ "10:10 am") 
jQuery(document).ready(function(){
var gmap\_m423c8ebf4720e28e157fcee659471974 = {
positions : {
871 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m423c8ebf4720e28e157fcee659471974' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m423c8ebf4720e28e157fcee659471974.positions ) {
gmap\_m423c8ebf4720e28e157fcee659471974.bounds.extend( gmap\_m423c8ebf4720e28e157fcee659471974.positions[m] );
}
// Render markers
for ( var m in gmap\_m423c8ebf4720e28e157fcee659471974.positions ) {
gmap\_m423c8ebf4720e28e157fcee659471974.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m423c8ebf4720e28e157fcee659471974.map,
position : gmap\_m423c8ebf4720e28e157fcee659471974.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m423c8ebf4720e28e157fcee659471974.map.setCenter( gmap\_m423c8ebf4720e28e157fcee659471974.positions[871] );
});