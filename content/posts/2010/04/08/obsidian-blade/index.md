---
title: Obsidian Blade
date: '2010-04-08T12:34:52+00:00'
format: image
service: flickr
tags:
- blade
- flintknapping
- obsidian
- stone
- tombrown
- trackerschool
- tracking
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4515818879_ba1bc63e38_o.jpg?resize=607%2C455
---

[![Obsidian Blade](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4515818879_ba1bc63e38_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/08/obsidian-blade/) 
# [Obsidian Blade](http://dentedreality.com.au/2010/04/08/obsidian-blade/)

One of the blades that one of the instructors was working on at Tracker School.





* #[blade](http://dentedreality.com.au/tags/blade/)
* #[flintknapping](http://dentedreality.com.au/tags/flintknapping/)
* #[obsidian](http://dentedreality.com.au/tags/obsidian/)
* #[stone](http://dentedreality.com.au/tags/stone/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4515818879/) [12:34 pm, April 8, 2010](http://dentedreality.com.au/2010/04/08/obsidian-blade/ "12:34 pm") 
jQuery(document).ready(function(){
var gmap\_mc9979ac6d28f5922ce3158e541df2b96 = {
positions : {
330 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc9979ac6d28f5922ce3158e541df2b96' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc9979ac6d28f5922ce3158e541df2b96.positions ) {
gmap\_mc9979ac6d28f5922ce3158e541df2b96.bounds.extend( gmap\_mc9979ac6d28f5922ce3158e541df2b96.positions[m] );
}
// Render markers
for ( var m in gmap\_mc9979ac6d28f5922ce3158e541df2b96.positions ) {
gmap\_mc9979ac6d28f5922ce3158e541df2b96.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc9979ac6d28f5922ce3158e541df2b96.map,
position : gmap\_mc9979ac6d28f5922ce3158e541df2b96.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc9979ac6d28f5922ce3158e541df2b96.map.setCenter( gmap\_mc9979ac6d28f5922ce3158e541df2b96.positions[330] );
});