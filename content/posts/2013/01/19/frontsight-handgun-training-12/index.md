---
title: Frontsight Handgun Training
date: '2013-01-19T09:27:13+00:00'
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
image: http://dentedreality.com.au/wp-content/uploads/2013/01/8460186044_8afb3e2832_o-1024x764.jpg
---

[![Frontsight Handgun Training](http://dentedreality.com.au/wp-content/uploads/2013/01/8460186044_8afb3e2832_o-1024x764.jpg)](https://dentedreality.com.au/2013/01/19/frontsight-handgun-training-12/) 
# [Frontsight Handgun Training](https://dentedreality.com.au/2013/01/19/frontsight-handgun-training-12/)

[![Frontsight Handgun Training](http://dentedreality.com.au/wp-content/uploads/2013/01/8460186044_8afb3e2832_o-1024x764.jpg)](http://www.flickr.com/photos/borkazoid/8460186044/)





* #[frontsight](https://dentedreality.com.au/tags/frontsight/)
* #[gun](https://dentedreality.com.au/tags/gun/)
* #[gunrange](https://dentedreality.com.au/tags/gunrange/)
* #[handgun](https://dentedreality.com.au/tags/handgun/)
* #[pistol](https://dentedreality.com.au/tags/pistol/)
* #[shooting](https://dentedreality.com.au/tags/shooting/)
* #[training](https://dentedreality.com.au/tags/training/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460186044/) [9:27 am, January 19, 2013](https://dentedreality.com.au/2013/01/19/frontsight-handgun-training-12/ "9:27 am") 
jQuery(document).ready(function(){
var gmap\_m833b16102f69eb18571e77d7e5093ca9 = {
positions : {
320 : new google.maps.LatLng( '36.031333', '-115.883334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m833b16102f69eb18571e77d7e5093ca9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m833b16102f69eb18571e77d7e5093ca9.positions ) {
gmap\_m833b16102f69eb18571e77d7e5093ca9.bounds.extend( gmap\_m833b16102f69eb18571e77d7e5093ca9.positions[m] );
}
// Render markers
for ( var m in gmap\_m833b16102f69eb18571e77d7e5093ca9.positions ) {
gmap\_m833b16102f69eb18571e77d7e5093ca9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m833b16102f69eb18571e77d7e5093ca9.map,
position : gmap\_m833b16102f69eb18571e77d7e5093ca9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m833b16102f69eb18571e77d7e5093ca9.map.setCenter( gmap\_m833b16102f69eb18571e77d7e5093ca9.positions[320] );
});