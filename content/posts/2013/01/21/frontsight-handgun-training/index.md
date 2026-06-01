---
title: Frontsight Handgun Training
date: '2013-01-21T12:40:52+00:00'
format: image
service: flickr
tags:
- frontsight
- gun
- gunrange
- handgun
- pistol
- shooting
- training
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/01/8459085813_02d45f2056_o.jpg?resize=607%2C813
---

[![Frontsight Handgun Training](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/01/8459085813_02d45f2056_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2013/01/21/frontsight-handgun-training/) 
# [Frontsight Handgun Training](http://dentedreality.com.au/2013/01/21/frontsight-handgun-training/)





* #[frontsight](http://dentedreality.com.au/tags/frontsight/)
* #[gun](http://dentedreality.com.au/tags/gun/)
* #[gunrange](http://dentedreality.com.au/tags/gunrange/)
* #[handgun](http://dentedreality.com.au/tags/handgun/)
* #[pistol](http://dentedreality.com.au/tags/pistol/)
* #[shooting](http://dentedreality.com.au/tags/shooting/)
* #[training](http://dentedreality.com.au/tags/training/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8459085813/) [12:40 pm, January 21, 2013](http://dentedreality.com.au/2013/01/21/frontsight-handgun-training/ "12:40 pm") 
jQuery(document).ready(function(){
var gmap\_m5d5db8178dbe67b0ee0adb67e13ad48c = {
positions : {
672 : new google.maps.LatLng( '36.0355', '-115.890167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5d5db8178dbe67b0ee0adb67e13ad48c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5d5db8178dbe67b0ee0adb67e13ad48c.positions ) {
gmap\_m5d5db8178dbe67b0ee0adb67e13ad48c.bounds.extend( gmap\_m5d5db8178dbe67b0ee0adb67e13ad48c.positions[m] );
}
// Render markers
for ( var m in gmap\_m5d5db8178dbe67b0ee0adb67e13ad48c.positions ) {
gmap\_m5d5db8178dbe67b0ee0adb67e13ad48c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5d5db8178dbe67b0ee0adb67e13ad48c.map,
position : gmap\_m5d5db8178dbe67b0ee0adb67e13ad48c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5d5db8178dbe67b0ee0adb67e13ad48c.map.setCenter( gmap\_m5d5db8178dbe67b0ee0adb67e13ad48c.positions[672] );
});