---
title: Suburban Turban
date: '2012-02-18T12:30:05+00:00'
format: image
service: flickr
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813460766_c86f330acc_o.jpg?resize=607%2C813
---

[![Suburban Turban](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/02/6813460766_c86f330acc_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/02/18/suburban-turban/) 
# [Suburban Turban](http://dentedreality.com.au/2012/02/18/suburban-turban/)





Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813460766/) [12:30 pm, February 18, 2012](http://dentedreality.com.au/2012/02/18/suburban-turban/ "12:30 pm") 
jQuery(document).ready(function(){
var gmap\_m9f100cbd2d9c33285d3bbc5e09ccd101 = {
positions : {
961 : new google.maps.LatLng( '37.741833', '-122.506834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9f100cbd2d9c33285d3bbc5e09ccd101' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9f100cbd2d9c33285d3bbc5e09ccd101.positions ) {
gmap\_m9f100cbd2d9c33285d3bbc5e09ccd101.bounds.extend( gmap\_m9f100cbd2d9c33285d3bbc5e09ccd101.positions[m] );
}
// Render markers
for ( var m in gmap\_m9f100cbd2d9c33285d3bbc5e09ccd101.positions ) {
gmap\_m9f100cbd2d9c33285d3bbc5e09ccd101.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9f100cbd2d9c33285d3bbc5e09ccd101.map,
position : gmap\_m9f100cbd2d9c33285d3bbc5e09ccd101.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9f100cbd2d9c33285d3bbc5e09ccd101.map.setCenter( gmap\_m9f100cbd2d9c33285d3bbc5e09ccd101.positions[961] );
});