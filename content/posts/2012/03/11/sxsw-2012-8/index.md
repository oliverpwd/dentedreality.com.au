---
title: SXSW 2012
date: '2012-03-11T09:18:45+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2012
- texas
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721573158_da24538cf6_o.jpg?resize=607%2C452
---

[![SXSW 2012](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721573158_da24538cf6_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/11/sxsw-2012-8/) 
# [SXSW 2012](http://dentedreality.com.au/2012/03/11/sxsw-2012-8/)

Random public vegetables





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2012](http://dentedreality.com.au/tags/sxsw2012/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7721573158/) [9:18 am, March 11, 2012](http://dentedreality.com.au/2012/03/11/sxsw-2012-8/ "9:18 am") 
jQuery(document).ready(function(){
var gmap\_m49c694d36df44ccc9c7aceff6abbfd1f = {
positions : {
738 : new google.maps.LatLng( '30.257833', '-97.745167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m49c694d36df44ccc9c7aceff6abbfd1f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m49c694d36df44ccc9c7aceff6abbfd1f.positions ) {
gmap\_m49c694d36df44ccc9c7aceff6abbfd1f.bounds.extend( gmap\_m49c694d36df44ccc9c7aceff6abbfd1f.positions[m] );
}
// Render markers
for ( var m in gmap\_m49c694d36df44ccc9c7aceff6abbfd1f.positions ) {
gmap\_m49c694d36df44ccc9c7aceff6abbfd1f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m49c694d36df44ccc9c7aceff6abbfd1f.map,
position : gmap\_m49c694d36df44ccc9c7aceff6abbfd1f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m49c694d36df44ccc9c7aceff6abbfd1f.map.setCenter( gmap\_m49c694d36df44ccc9c7aceff6abbfd1f.positions[738] );
});