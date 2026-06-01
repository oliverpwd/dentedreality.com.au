---
title: IMG_0731
date: '2010-12-31T10:29:50+00:00'
format: image
service: flickr
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434709712_cb073bf4cd_o.jpg?resize=607%2C452
---

[![IMG_0731](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434709712_cb073bf4cd_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/12/31/img_0731/) 
# [IMG\_0731](http://dentedreality.com.au/2010/12/31/img_0731/)





Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434709712/) [10:29 am, December 31, 2010](http://dentedreality.com.au/2010/12/31/img_0731/ "10:29 am") 
jQuery(document).ready(function(){
var gmap\_m3fee87c22e758af8a07716a9a4333836 = {
positions : {
910 : new google.maps.LatLng( '-32.053', '115.845999' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3fee87c22e758af8a07716a9a4333836' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3fee87c22e758af8a07716a9a4333836.positions ) {
gmap\_m3fee87c22e758af8a07716a9a4333836.bounds.extend( gmap\_m3fee87c22e758af8a07716a9a4333836.positions[m] );
}
// Render markers
for ( var m in gmap\_m3fee87c22e758af8a07716a9a4333836.positions ) {
gmap\_m3fee87c22e758af8a07716a9a4333836.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3fee87c22e758af8a07716a9a4333836.map,
position : gmap\_m3fee87c22e758af8a07716a9a4333836.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3fee87c22e758af8a07716a9a4333836.map.setCenter( gmap\_m3fee87c22e758af8a07716a9a4333836.positions[910] );
});