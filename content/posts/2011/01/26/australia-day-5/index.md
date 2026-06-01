---
title: Australia Day
date: '2011-01-26T15:55:58+00:00'
format: image
service: flickr
tags:
- australia
- australiaday
- australiaday2011
- sydney
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434193253_bf4d71521a_o.jpg?resize=607%2C452
---

[![Australia Day](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434193253_bf4d71521a_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/26/australia-day-5/) 
# [Australia Day](http://dentedreality.com.au/2011/01/26/australia-day-5/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[australiaday](http://dentedreality.com.au/tags/australiaday/)
* #[australiaday2011](http://dentedreality.com.au/tags/australiaday2011/)
* #[sydney](http://dentedreality.com.au/tags/sydney/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434193253/) [3:55 pm, January 26, 2011](http://dentedreality.com.au/2011/01/26/australia-day-5/ "3:55 pm") 
jQuery(document).ready(function(){
var gmap\_md922a48306c5e0867aa28e91fe0812ec = {
positions : {
841 : new google.maps.LatLng( '-33.864001', '151.171833' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md922a48306c5e0867aa28e91fe0812ec' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md922a48306c5e0867aa28e91fe0812ec.positions ) {
gmap\_md922a48306c5e0867aa28e91fe0812ec.bounds.extend( gmap\_md922a48306c5e0867aa28e91fe0812ec.positions[m] );
}
// Render markers
for ( var m in gmap\_md922a48306c5e0867aa28e91fe0812ec.positions ) {
gmap\_md922a48306c5e0867aa28e91fe0812ec.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md922a48306c5e0867aa28e91fe0812ec.map,
position : gmap\_md922a48306c5e0867aa28e91fe0812ec.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md922a48306c5e0867aa28e91fe0812ec.map.setCenter( gmap\_md922a48306c5e0867aa28e91fe0812ec.positions[841] );
});