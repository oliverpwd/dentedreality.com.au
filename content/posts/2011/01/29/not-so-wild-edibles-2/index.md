---
title: Not-So-Wild Edibles
date: '2011-01-29T08:11:08+00:00'
format: image
service: flickr
tags:
- food
- minerslettuce
- plants
- salad
- sorrel
- wildedibles
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5802608856_36577d10c8_o.jpg?resize=607%2C813
---

[![Not-So-Wild Edibles](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5802608856_36577d10c8_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/01/29/not-so-wild-edibles-2/) 
# [Not-So-Wild Edibles](http://dentedreality.com.au/2011/01/29/not-so-wild-edibles-2/)

I learned about these 2 edible "weeds" during Tracker School… and apparently you can now buy them at the Ferry Building Farmer’s Market





* #[food](http://dentedreality.com.au/tags/food/)
* #[minerslettuce](http://dentedreality.com.au/tags/minerslettuce/)
* #[plants](http://dentedreality.com.au/tags/plants/)
* #[salad](http://dentedreality.com.au/tags/salad/)
* #[sorrel](http://dentedreality.com.au/tags/sorrel/)
* #[wildedibles](http://dentedreality.com.au/tags/wildedibles/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802608856/) [8:11 am, January 29, 2011](http://dentedreality.com.au/2011/01/29/not-so-wild-edibles-2/ "8:11 am") 
jQuery(document).ready(function(){
var gmap\_m0e6810c70f775a577f3a8eddee6d4b0b = {
positions : {
49 : new google.maps.LatLng( '37.795333', '-122.392334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0e6810c70f775a577f3a8eddee6d4b0b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0e6810c70f775a577f3a8eddee6d4b0b.positions ) {
gmap\_m0e6810c70f775a577f3a8eddee6d4b0b.bounds.extend( gmap\_m0e6810c70f775a577f3a8eddee6d4b0b.positions[m] );
}
// Render markers
for ( var m in gmap\_m0e6810c70f775a577f3a8eddee6d4b0b.positions ) {
gmap\_m0e6810c70f775a577f3a8eddee6d4b0b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0e6810c70f775a577f3a8eddee6d4b0b.map,
position : gmap\_m0e6810c70f775a577f3a8eddee6d4b0b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0e6810c70f775a577f3a8eddee6d4b0b.map.setCenter( gmap\_m0e6810c70f775a577f3a8eddee6d4b0b.positions[49] );
});