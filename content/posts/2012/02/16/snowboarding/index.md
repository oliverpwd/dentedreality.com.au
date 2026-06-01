---
title: Snowboarding
date: '2012-02-16T10:06:08+00:00'
format: image
service: flickr
tags:
- emmi
- erika
- nelson
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813460464_bfc05d3459_o.jpg?resize=607%2C813
---

[![Snowboarding](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813460464_bfc05d3459_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/02/16/snowboarding/) 
# [Snowboarding](http://dentedreality.com.au/2012/02/16/snowboarding/)





* #[emmi](http://dentedreality.com.au/tags/emmi/)
* #[erika](http://dentedreality.com.au/tags/erika/)
* #[nelson](http://dentedreality.com.au/tags/nelson/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813460464/) [10:06 am, February 16, 2012](http://dentedreality.com.au/2012/02/16/snowboarding/ "10:06 am") 
jQuery(document).ready(function(){
var gmap\_m69988a7e5c8c16ef9f318ad8027a1ab2 = {
positions : {
235 : new google.maps.LatLng( '38.9345', '-119.940334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m69988a7e5c8c16ef9f318ad8027a1ab2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m69988a7e5c8c16ef9f318ad8027a1ab2.positions ) {
gmap\_m69988a7e5c8c16ef9f318ad8027a1ab2.bounds.extend( gmap\_m69988a7e5c8c16ef9f318ad8027a1ab2.positions[m] );
}
// Render markers
for ( var m in gmap\_m69988a7e5c8c16ef9f318ad8027a1ab2.positions ) {
gmap\_m69988a7e5c8c16ef9f318ad8027a1ab2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m69988a7e5c8c16ef9f318ad8027a1ab2.map,
position : gmap\_m69988a7e5c8c16ef9f318ad8027a1ab2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m69988a7e5c8c16ef9f318ad8027a1ab2.map.setCenter( gmap\_m69988a7e5c8c16ef9f318ad8027a1ab2.positions[235] );
});