---
title: Australia Day
date: '2011-01-26T17:07:30+00:00'
format: image
service: flickr
tags:
- australia
- australiaday
- australiaday2011
- sydney
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434807516_06004454a2_o.jpg?resize=607%2C452
---

[![Australia Day](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434807516_06004454a2_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/26/australia-day-2/) 
# [Australia Day](http://dentedreality.com.au/2011/01/26/australia-day-2/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[australiaday](http://dentedreality.com.au/tags/australiaday/)
* #[australiaday2011](http://dentedreality.com.au/tags/australiaday2011/)
* #[sydney](http://dentedreality.com.au/tags/sydney/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434807516/) [5:07 pm, January 26, 2011](http://dentedreality.com.au/2011/01/26/australia-day-2/ "5:07 pm") 
jQuery(document).ready(function(){
var gmap\_m42bcb76c24035470709a591b9f3a5459 = {
positions : {
539 : new google.maps.LatLng( '-33.864001', '151.172' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m42bcb76c24035470709a591b9f3a5459' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m42bcb76c24035470709a591b9f3a5459.positions ) {
gmap\_m42bcb76c24035470709a591b9f3a5459.bounds.extend( gmap\_m42bcb76c24035470709a591b9f3a5459.positions[m] );
}
// Render markers
for ( var m in gmap\_m42bcb76c24035470709a591b9f3a5459.positions ) {
gmap\_m42bcb76c24035470709a591b9f3a5459.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m42bcb76c24035470709a591b9f3a5459.map,
position : gmap\_m42bcb76c24035470709a591b9f3a5459.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m42bcb76c24035470709a591b9f3a5459.map.setCenter( gmap\_m42bcb76c24035470709a591b9f3a5459.positions[539] );
});