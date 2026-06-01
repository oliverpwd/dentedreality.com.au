---
title: Anthony’s Nose
date: '2013-08-24T10:04:51+00:00'
format: image
tags:
- anthony's nose
- bear mountain
- hiking
- new york
- sky
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767967475_743a4331a3_o.jpg?resize=607%2C452
---

[![IMG_5512](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767967475_743a4331a3_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/08/24/img_5512/) 
# [Anthony’s Nose](http://dentedreality.com.au/2013/08/24/img_5512/)





* #[anthony's nose](http://dentedreality.com.au/tags/anthonys-nose/)
* #[bear mountain](http://dentedreality.com.au/tags/bear-mountain/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[new york](http://dentedreality.com.au/tags/new-york/)
* #[sky](http://dentedreality.com.au/tags/sky/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9767967475/) [10:04 am, August 24, 2013](http://dentedreality.com.au/2013/08/24/img_5512/ "10:04 am") 
jQuery(document).ready(function(){
var gmap\_m8410ad6a610723ade4def6c3943866d7 = {
positions : {
40 : new google.maps.LatLng( '41.320166', '-73.974334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8410ad6a610723ade4def6c3943866d7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8410ad6a610723ade4def6c3943866d7.positions ) {
gmap\_m8410ad6a610723ade4def6c3943866d7.bounds.extend( gmap\_m8410ad6a610723ade4def6c3943866d7.positions[m] );
}
// Render markers
for ( var m in gmap\_m8410ad6a610723ade4def6c3943866d7.positions ) {
gmap\_m8410ad6a610723ade4def6c3943866d7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8410ad6a610723ade4def6c3943866d7.map,
position : gmap\_m8410ad6a610723ade4def6c3943866d7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8410ad6a610723ade4def6c3943866d7.map.setCenter( gmap\_m8410ad6a610723ade4def6c3943866d7.positions[40] );
});