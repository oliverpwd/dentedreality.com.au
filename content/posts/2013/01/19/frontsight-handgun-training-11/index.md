---
title: Frontsight Handgun Training
date: '2013-01-19T10:32:41+00:00'
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
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/01/8460186202_740b106d99_o.jpg?resize=607%2C813
---

[![Frontsight Handgun Training](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/01/8460186202_740b106d99_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2013/01/19/frontsight-handgun-training-11/) 
# [Frontsight Handgun Training](http://dentedreality.com.au/2013/01/19/frontsight-handgun-training-11/)





* #[frontsight](http://dentedreality.com.au/tags/frontsight/)
* #[gun](http://dentedreality.com.au/tags/gun/)
* #[gunrange](http://dentedreality.com.au/tags/gunrange/)
* #[handgun](http://dentedreality.com.au/tags/handgun/)
* #[pistol](http://dentedreality.com.au/tags/pistol/)
* #[shooting](http://dentedreality.com.au/tags/shooting/)
* #[training](http://dentedreality.com.au/tags/training/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460186202/) [10:32 am, January 19, 2013](http://dentedreality.com.au/2013/01/19/frontsight-handgun-training-11/ "10:32 am") 
jQuery(document).ready(function(){
var gmap\_m336fb9a58c6dd03ef2e966c3ae6f7240 = {
positions : {
337 : new google.maps.LatLng( '36.031333', '-115.883334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m336fb9a58c6dd03ef2e966c3ae6f7240' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m336fb9a58c6dd03ef2e966c3ae6f7240.positions ) {
gmap\_m336fb9a58c6dd03ef2e966c3ae6f7240.bounds.extend( gmap\_m336fb9a58c6dd03ef2e966c3ae6f7240.positions[m] );
}
// Render markers
for ( var m in gmap\_m336fb9a58c6dd03ef2e966c3ae6f7240.positions ) {
gmap\_m336fb9a58c6dd03ef2e966c3ae6f7240.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m336fb9a58c6dd03ef2e966c3ae6f7240.map,
position : gmap\_m336fb9a58c6dd03ef2e966c3ae6f7240.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m336fb9a58c6dd03ef2e966c3ae6f7240.map.setCenter( gmap\_m336fb9a58c6dd03ef2e966c3ae6f7240.positions[337] );
});