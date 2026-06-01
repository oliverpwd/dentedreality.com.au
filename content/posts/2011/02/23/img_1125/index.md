---
title: IMG_1125
date: '2011-02-23T09:10:58+00:00'
format: image
service: flickr
tags:
- newyork
- newyorkcity
- NYC
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802058605_c797f55abe_o.jpg?resize=607%2C813
---

[![IMG_1125](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802058605_c797f55abe_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/02/23/img_1125/) 
# [IMG\_1125](http://dentedreality.com.au/2011/02/23/img_1125/)





* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[newyorkcity](http://dentedreality.com.au/tags/newyorkcity/)
* #[NYC](http://dentedreality.com.au/tags/nyc/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802058605/) [9:10 am, February 23, 2011](http://dentedreality.com.au/2011/02/23/img_1125/ "9:10 am") 
jQuery(document).ready(function(){
var gmap\_ma7fe8ea5106caa626f2eabcad281d79d = {
positions : {
247 : new google.maps.LatLng( '40.701666', '-74.0065' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma7fe8ea5106caa626f2eabcad281d79d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma7fe8ea5106caa626f2eabcad281d79d.positions ) {
gmap\_ma7fe8ea5106caa626f2eabcad281d79d.bounds.extend( gmap\_ma7fe8ea5106caa626f2eabcad281d79d.positions[m] );
}
// Render markers
for ( var m in gmap\_ma7fe8ea5106caa626f2eabcad281d79d.positions ) {
gmap\_ma7fe8ea5106caa626f2eabcad281d79d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma7fe8ea5106caa626f2eabcad281d79d.map,
position : gmap\_ma7fe8ea5106caa626f2eabcad281d79d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma7fe8ea5106caa626f2eabcad281d79d.map.setCenter( gmap\_ma7fe8ea5106caa626f2eabcad281d79d.positions[247] );
});