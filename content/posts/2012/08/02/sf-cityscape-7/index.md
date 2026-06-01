---
title: SF Cityscape
date: '2012-08-02T19:38:17+00:00'
format: image
service: flickr
tags:
- cityscape
- sanfrancisco
- sf
- skyline
- view
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8245785388_b4d1a2e265_o.jpg?resize=607%2C452
---

[![SF Cityscape](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8245785388_b4d1a2e265_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/08/02/sf-cityscape-7/) 
# [SF Cityscape](http://dentedreality.com.au/2012/08/02/sf-cityscape-7/)





* #[cityscape](http://dentedreality.com.au/tags/cityscape/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[sf](http://dentedreality.com.au/tags/sf/)
* #[skyline](http://dentedreality.com.au/tags/skyline/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245785388/) [7:38 pm, August 2, 2012](http://dentedreality.com.au/2012/08/02/sf-cityscape-7/ "7:38 pm") 
jQuery(document).ready(function(){
var gmap\_m991bd83cb736b76ce838df2091dffbe6 = {
positions : {
300 : new google.maps.LatLng( '37.787833', '-122.403' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m991bd83cb736b76ce838df2091dffbe6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m991bd83cb736b76ce838df2091dffbe6.positions ) {
gmap\_m991bd83cb736b76ce838df2091dffbe6.bounds.extend( gmap\_m991bd83cb736b76ce838df2091dffbe6.positions[m] );
}
// Render markers
for ( var m in gmap\_m991bd83cb736b76ce838df2091dffbe6.positions ) {
gmap\_m991bd83cb736b76ce838df2091dffbe6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m991bd83cb736b76ce838df2091dffbe6.map,
position : gmap\_m991bd83cb736b76ce838df2091dffbe6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m991bd83cb736b76ce838df2091dffbe6.map.setCenter( gmap\_m991bd83cb736b76ce838df2091dffbe6.positions[300] );
});