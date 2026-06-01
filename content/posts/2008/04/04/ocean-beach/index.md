---
title: Ocean Beach
date: '2008-04-04T15:04:53+00:00'
format: image
service: flickr
tags:
- australia
- beach
- ocean
- oceanbeach
- renniewedding
- timswedding
- westernaustraliadenmark
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433422320_0854ba57d9_o.jpg?resize=607%2C455
---

[![Ocean Beach](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433422320_0854ba57d9_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2008/04/04/ocean-beach/) 
# [Ocean Beach](http://dentedreality.com.au/2008/04/04/ocean-beach/)

At Denmark.





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[ocean](http://dentedreality.com.au/tags/ocean/)
* #[oceanbeach](http://dentedreality.com.au/tags/oceanbeach/)
* #[renniewedding](http://dentedreality.com.au/tags/renniewedding/)
* #[timswedding](http://dentedreality.com.au/tags/timswedding/)
* #[westernaustraliadenmark](http://dentedreality.com.au/tags/westernaustraliadenmark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2433422320/) [3:04 pm, April 4, 2008](http://dentedreality.com.au/2008/04/04/ocean-beach/ "3:04 pm") 
jQuery(document).ready(function(){
var gmap\_m10582b1270bdc33a575d7c1ce4d4eaa0 = {
positions : {
863 : new google.maps.LatLng( '-35.03604', '117.329177' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m10582b1270bdc33a575d7c1ce4d4eaa0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m10582b1270bdc33a575d7c1ce4d4eaa0.positions ) {
gmap\_m10582b1270bdc33a575d7c1ce4d4eaa0.bounds.extend( gmap\_m10582b1270bdc33a575d7c1ce4d4eaa0.positions[m] );
}
// Render markers
for ( var m in gmap\_m10582b1270bdc33a575d7c1ce4d4eaa0.positions ) {
gmap\_m10582b1270bdc33a575d7c1ce4d4eaa0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m10582b1270bdc33a575d7c1ce4d4eaa0.map,
position : gmap\_m10582b1270bdc33a575d7c1ce4d4eaa0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m10582b1270bdc33a575d7c1ce4d4eaa0.map.setCenter( gmap\_m10582b1270bdc33a575d7c1ce4d4eaa0.positions[863] );
});