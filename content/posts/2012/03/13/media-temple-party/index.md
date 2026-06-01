---
title: Media Temple Party
date: '2012-03-13T20:25:52+00:00'
format: image
service: flickr
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721697466_47e46ff3da_o.jpg?resize=607%2C452
---

[![Media Temple Party](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721697466_47e46ff3da_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/13/media-temple-party/) 
# [Media Temple Party](http://dentedreality.com.au/2012/03/13/media-temple-party/)





Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7721697466/) [8:25 pm, March 13, 2012](http://dentedreality.com.au/2012/03/13/media-temple-party/ "8:25 pm") 
jQuery(document).ready(function(){
var gmap\_ma63094f0e2993fb8bf54b85b91cf4cb9 = {
positions : {
615 : new google.maps.LatLng( '30.268833', '-97.735834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma63094f0e2993fb8bf54b85b91cf4cb9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma63094f0e2993fb8bf54b85b91cf4cb9.positions ) {
gmap\_ma63094f0e2993fb8bf54b85b91cf4cb9.bounds.extend( gmap\_ma63094f0e2993fb8bf54b85b91cf4cb9.positions[m] );
}
// Render markers
for ( var m in gmap\_ma63094f0e2993fb8bf54b85b91cf4cb9.positions ) {
gmap\_ma63094f0e2993fb8bf54b85b91cf4cb9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma63094f0e2993fb8bf54b85b91cf4cb9.map,
position : gmap\_ma63094f0e2993fb8bf54b85b91cf4cb9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma63094f0e2993fb8bf54b85b91cf4cb9.map.setCenter( gmap\_ma63094f0e2993fb8bf54b85b91cf4cb9.positions[615] );
});