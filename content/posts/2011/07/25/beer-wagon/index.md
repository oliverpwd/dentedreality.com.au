---
title: Beer Wagon
date: '2011-07-25T13:46:06+00:00'
format: image
service: flickr
tags:
- beer
- red
- redflyer
- wagon
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6323462300_f2cb4bdf91_o.jpg?resize=607%2C452
---

[![Beer Wagon](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6323462300_f2cb4bdf91_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/07/25/beer-wagon/) 
# [Beer Wagon](http://dentedreality.com.au/2011/07/25/beer-wagon/)





* #[beer](http://dentedreality.com.au/tags/beer/)
* #[red](http://dentedreality.com.au/tags/red/)
* #[redflyer](http://dentedreality.com.au/tags/redflyer/)
* #[wagon](http://dentedreality.com.au/tags/wagon/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6323462300/) [1:46 pm, July 25, 2011](http://dentedreality.com.au/2011/07/25/beer-wagon/ "1:46 pm") 
jQuery(document).ready(function(){
var gmap\_me640d762000cbf27566c717d9cca37cd = {
positions : {
595 : new google.maps.LatLng( '37.782666', '-122.388' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me640d762000cbf27566c717d9cca37cd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me640d762000cbf27566c717d9cca37cd.positions ) {
gmap\_me640d762000cbf27566c717d9cca37cd.bounds.extend( gmap\_me640d762000cbf27566c717d9cca37cd.positions[m] );
}
// Render markers
for ( var m in gmap\_me640d762000cbf27566c717d9cca37cd.positions ) {
gmap\_me640d762000cbf27566c717d9cca37cd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me640d762000cbf27566c717d9cca37cd.map,
position : gmap\_me640d762000cbf27566c717d9cca37cd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me640d762000cbf27566c717d9cca37cd.map.setCenter( gmap\_me640d762000cbf27566c717d9cca37cd.positions[595] );
});