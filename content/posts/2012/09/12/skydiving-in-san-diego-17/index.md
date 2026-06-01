---
title: Skydiving in San Diego
date: '2012-09-12T12:41:11-06:00'
format: image
service: flickr
tags:
- andrewspittle
- automattic
- skydiving
- wordpress
latitude: '32.571'
longitude: '-116.993334'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/09/14190718/8244794231_e5998979e9_o.jpg
---

[![Skydiving in San Diego](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/09/14190718/8244794231_e5998979e9_o.jpg)](https://dentedreality.com.au/2012/09/12/skydiving-in-san-diego-17/) 
# [Skydiving in San Diego](https://dentedreality.com.au/2012/09/12/skydiving-in-san-diego-17/)

[![Skydiving in San Diego](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/09/14190718/8244794231_e5998979e9_o.jpg)](http://www.flickr.com/photos/borkazoid/8244794231/)

At the Automattic Grand Meetup, 2012

32.571-116.993334




* #[andrewspittle](https://dentedreality.com.au/tags/andrewspittle/)
* #[automattic](https://dentedreality.com.au/tags/automattic/)
* #[skydiving](https://dentedreality.com.au/tags/skydiving/)
* #[wordpress](https://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8244794231/) [12:41 pm, September 12, 2012](https://dentedreality.com.au/2012/09/12/skydiving-in-san-diego-17/ "12:41 pm") 
jQuery(document).ready(function(){
var gmap\_m33aabba2183211a7dcbfbc925f0009e7 = {
positions : {
48 : new google.maps.LatLng( '32.571', '-116.993334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m33aabba2183211a7dcbfbc925f0009e7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m33aabba2183211a7dcbfbc925f0009e7.positions ) {
gmap\_m33aabba2183211a7dcbfbc925f0009e7.bounds.extend( gmap\_m33aabba2183211a7dcbfbc925f0009e7.positions[m] );
}
// Render markers
for ( var m in gmap\_m33aabba2183211a7dcbfbc925f0009e7.positions ) {
gmap\_m33aabba2183211a7dcbfbc925f0009e7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m33aabba2183211a7dcbfbc925f0009e7.map,
position : gmap\_m33aabba2183211a7dcbfbc925f0009e7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m33aabba2183211a7dcbfbc925f0009e7.map.setCenter( gmap\_m33aabba2183211a7dcbfbc925f0009e7.positions[48] );
});