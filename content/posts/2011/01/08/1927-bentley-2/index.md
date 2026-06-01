---
title: 1927 Bentley
date: '2011-01-08T11:47:12-07:00'
format: image
service: flickr
tags:
- 1927car
- bentley
- vintage
latitude: '-32.053167'
longitude: '115.845999'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/01/14185953/5434720174_e9ddc80d1d_o.jpg
---

[![1927 Bentley](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/01/14185953/5434720174_e9ddc80d1d_o.jpg)](https://dentedreality.com.au/2011/01/08/1927-bentley-2/) 
# [1927 Bentley](https://dentedreality.com.au/2011/01/08/1927-bentley-2/)

[![1927 Bentley](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/01/14185953/5434720174_e9ddc80d1d_o.jpg)](http://www.flickr.com/photos/borkazoid/5434720174/)

-32.053167115.845999




* #[1927car](https://dentedreality.com.au/tags/1927car/)
* #[bentley](https://dentedreality.com.au/tags/bentley/)
* #[vintage](https://dentedreality.com.au/tags/vintage/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434720174/) [11:47 am, January 8, 2011](https://dentedreality.com.au/2011/01/08/1927-bentley-2/ "11:47 am") 
jQuery(document).ready(function(){
var gmap\_m3636e4eff4807fa9f88c4c736e377bc1 = {
positions : {
147 : new google.maps.LatLng( '-32.053167', '115.845999' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3636e4eff4807fa9f88c4c736e377bc1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3636e4eff4807fa9f88c4c736e377bc1.positions ) {
gmap\_m3636e4eff4807fa9f88c4c736e377bc1.bounds.extend( gmap\_m3636e4eff4807fa9f88c4c736e377bc1.positions[m] );
}
// Render markers
for ( var m in gmap\_m3636e4eff4807fa9f88c4c736e377bc1.positions ) {
gmap\_m3636e4eff4807fa9f88c4c736e377bc1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3636e4eff4807fa9f88c4c736e377bc1.map,
position : gmap\_m3636e4eff4807fa9f88c4c736e377bc1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3636e4eff4807fa9f88c4c736e377bc1.map.setCenter( gmap\_m3636e4eff4807fa9f88c4c736e377bc1.positions[147] );
});