---
title: IMG_0730
date: '2010-12-31T10:16:16+00:00'
format: image
service: flickr
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434096077_75a0fdb47c_o.jpg?resize=607%2C452
---

[![IMG_0730](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434096077_75a0fdb47c_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/12/31/img_0730/) 
# [IMG\_0730](http://dentedreality.com.au/2010/12/31/img_0730/)





Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434096077/) [10:16 am, December 31, 2010](http://dentedreality.com.au/2010/12/31/img_0730/ "10:16 am") 
jQuery(document).ready(function(){
var gmap\_m933efc02b8f34d7b3438fc23316462ae = {
positions : {
482 : new google.maps.LatLng( '-32.053', '115.845999' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m933efc02b8f34d7b3438fc23316462ae' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m933efc02b8f34d7b3438fc23316462ae.positions ) {
gmap\_m933efc02b8f34d7b3438fc23316462ae.bounds.extend( gmap\_m933efc02b8f34d7b3438fc23316462ae.positions[m] );
}
// Render markers
for ( var m in gmap\_m933efc02b8f34d7b3438fc23316462ae.positions ) {
gmap\_m933efc02b8f34d7b3438fc23316462ae.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m933efc02b8f34d7b3438fc23316462ae.map,
position : gmap\_m933efc02b8f34d7b3438fc23316462ae.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m933efc02b8f34d7b3438fc23316462ae.map.setCenter( gmap\_m933efc02b8f34d7b3438fc23316462ae.positions[482] );
});