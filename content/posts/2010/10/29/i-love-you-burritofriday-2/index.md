---
title: ''
date: '2010-10-29T18:29:34+00:00'
format: image
service: instagram
tags:
- burritofriday
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/3e7fc802fa134265936be095a75430f6_7.jpg?resize=607%2C607
---

[![I love you #burritofriday ](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/3e7fc802fa134265936be095a75430f6_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2010/10/29/i-love-you-burritofriday-2/) 

I love you #burritofriday





* #[burritofriday](http://dentedreality.com.au/tags/burritofriday/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/GXcv/) [6:29 pm, October 29, 2010](http://dentedreality.com.au/2010/10/29/i-love-you-burritofriday-2/ "6:29 pm") 
jQuery(document).ready(function(){
var gmap\_m1154b155f4997eda7dc47173c3916a21 = {
positions : {
662 : new google.maps.LatLng( '37.792031', '-122.421053' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1154b155f4997eda7dc47173c3916a21' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1154b155f4997eda7dc47173c3916a21.positions ) {
gmap\_m1154b155f4997eda7dc47173c3916a21.bounds.extend( gmap\_m1154b155f4997eda7dc47173c3916a21.positions[m] );
}
// Render markers
for ( var m in gmap\_m1154b155f4997eda7dc47173c3916a21.positions ) {
gmap\_m1154b155f4997eda7dc47173c3916a21.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1154b155f4997eda7dc47173c3916a21.map,
position : gmap\_m1154b155f4997eda7dc47173c3916a21.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1154b155f4997eda7dc47173c3916a21.map.setCenter( gmap\_m1154b155f4997eda7dc47173c3916a21.positions[662] );
});