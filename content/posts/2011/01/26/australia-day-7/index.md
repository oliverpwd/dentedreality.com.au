---
title: Australia Day
date: '2011-01-26T13:59:11+00:00'
format: image
service: flickr
tags:
- australia
- australiaday
- australiaday2011
- sydney
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434806342_992e25569b_o.jpg?resize=607%2C452
---

[![Australia Day](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434806342_992e25569b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/26/australia-day-7/) 
# [Australia Day](http://dentedreality.com.au/2011/01/26/australia-day-7/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[australiaday](http://dentedreality.com.au/tags/australiaday/)
* #[australiaday2011](http://dentedreality.com.au/tags/australiaday2011/)
* #[sydney](http://dentedreality.com.au/tags/sydney/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434806342/) [1:59 pm, January 26, 2011](http://dentedreality.com.au/2011/01/26/australia-day-7/ "1:59 pm") 
jQuery(document).ready(function(){
var gmap\_m3330e829b72b2b8679b265ea4c86e1fa = {
positions : {
15 : new google.maps.LatLng( '-33.8705', '151.1895' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3330e829b72b2b8679b265ea4c86e1fa' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3330e829b72b2b8679b265ea4c86e1fa.positions ) {
gmap\_m3330e829b72b2b8679b265ea4c86e1fa.bounds.extend( gmap\_m3330e829b72b2b8679b265ea4c86e1fa.positions[m] );
}
// Render markers
for ( var m in gmap\_m3330e829b72b2b8679b265ea4c86e1fa.positions ) {
gmap\_m3330e829b72b2b8679b265ea4c86e1fa.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3330e829b72b2b8679b265ea4c86e1fa.map,
position : gmap\_m3330e829b72b2b8679b265ea4c86e1fa.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3330e829b72b2b8679b265ea4c86e1fa.map.setCenter( gmap\_m3330e829b72b2b8679b265ea4c86e1fa.positions[15] );
});