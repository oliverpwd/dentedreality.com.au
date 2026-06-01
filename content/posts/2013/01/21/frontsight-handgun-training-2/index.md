---
title: Frontsight Handgun Training
date: '2013-01-21T07:37:05+00:00'
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
image: http://dentedreality.com.au/wp-content/uploads/2013/01/8459085609_cc55e13d60_o-1024x764.jpg
---

[![Frontsight Handgun Training](http://dentedreality.com.au/wp-content/uploads/2013/01/8459085609_cc55e13d60_o-1024x764.jpg)](https://dentedreality.com.au/2013/01/21/frontsight-handgun-training-2/) 
# [Frontsight Handgun Training](https://dentedreality.com.au/2013/01/21/frontsight-handgun-training-2/)

[![Frontsight Handgun Training](http://dentedreality.com.au/wp-content/uploads/2013/01/8459085609_cc55e13d60_o-1024x764.jpg)](http://www.flickr.com/photos/borkazoid/8459085609/)





* #[frontsight](https://dentedreality.com.au/tags/frontsight/)
* #[gun](https://dentedreality.com.au/tags/gun/)
* #[gunrange](https://dentedreality.com.au/tags/gunrange/)
* #[handgun](https://dentedreality.com.au/tags/handgun/)
* #[pistol](https://dentedreality.com.au/tags/pistol/)
* #[shooting](https://dentedreality.com.au/tags/shooting/)
* #[training](https://dentedreality.com.au/tags/training/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8459085609/) [7:37 am, January 21, 2013](https://dentedreality.com.au/2013/01/21/frontsight-handgun-training-2/ "7:37 am") 
jQuery(document).ready(function(){
var gmap\_mfce672ccfa0438e09b5b093c5b1931a7 = {
positions : {
322 : new google.maps.LatLng( '36.0355', '-115.890167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mfce672ccfa0438e09b5b093c5b1931a7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mfce672ccfa0438e09b5b093c5b1931a7.positions ) {
gmap\_mfce672ccfa0438e09b5b093c5b1931a7.bounds.extend( gmap\_mfce672ccfa0438e09b5b093c5b1931a7.positions[m] );
}
// Render markers
for ( var m in gmap\_mfce672ccfa0438e09b5b093c5b1931a7.positions ) {
gmap\_mfce672ccfa0438e09b5b093c5b1931a7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mfce672ccfa0438e09b5b093c5b1931a7.map,
position : gmap\_mfce672ccfa0438e09b5b093c5b1931a7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mfce672ccfa0438e09b5b093c5b1931a7.map.setCenter( gmap\_mfce672ccfa0438e09b5b093c5b1931a7.positions[322] );
});