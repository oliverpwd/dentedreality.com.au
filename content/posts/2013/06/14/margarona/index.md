---
title: Margarona
date: '2013-06-14T16:41:28-06:00'
format: image
service: flickr
tags:
- corona
- margarita
- margarona
latitude: '45.519833'
longitude: '-122.682'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/06/14190922/9439834300_4ed39d6f88_o.jpg
---

[![Margarona](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/06/14190922/9439834300_4ed39d6f88_o.jpg)](https://dentedreality.com.au/2013/06/14/margarona/) 
# [Margarona](https://dentedreality.com.au/2013/06/14/margarona/)

[![Margarona](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/06/14190922/9439834300_4ed39d6f88_o.jpg)](http://www.flickr.com/photos/borkazoid/9439834300/)

Corona, tipped upside down into a margarita

45.519833-122.682




* #[corona](https://dentedreality.com.au/tags/corona/)
* #[margarita](https://dentedreality.com.au/tags/margarita/)
* #[margarona](https://dentedreality.com.au/tags/margarona/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9439834300/) [4:41 pm, June 14, 2013](https://dentedreality.com.au/2013/06/14/margarona/ "4:41 pm") 
jQuery(document).ready(function(){
var gmap\_mf552e3c8fee61797ae1f9735f6315757 = {
positions : {
679 : new google.maps.LatLng( '45.519833', '-122.682' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf552e3c8fee61797ae1f9735f6315757' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf552e3c8fee61797ae1f9735f6315757.positions ) {
gmap\_mf552e3c8fee61797ae1f9735f6315757.bounds.extend( gmap\_mf552e3c8fee61797ae1f9735f6315757.positions[m] );
}
// Render markers
for ( var m in gmap\_mf552e3c8fee61797ae1f9735f6315757.positions ) {
gmap\_mf552e3c8fee61797ae1f9735f6315757.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf552e3c8fee61797ae1f9735f6315757.map,
position : gmap\_mf552e3c8fee61797ae1f9735f6315757.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf552e3c8fee61797ae1f9735f6315757.map.setCenter( gmap\_mf552e3c8fee61797ae1f9735f6315757.positions[679] );
});