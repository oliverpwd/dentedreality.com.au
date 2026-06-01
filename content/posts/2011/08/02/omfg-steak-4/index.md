---
title: OMFG Steak
date: '2011-08-02T09:44:03+00:00'
format: image
service: flickr
tags:
- 4505meats
- steak
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6323514774_4e2cdfaf64_o.jpg?resize=607%2C452
---

[![OMFG Steak](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6323514774_4e2cdfaf64_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/08/02/omfg-steak-4/) 
# [OMFG Steak](http://dentedreality.com.au/2011/08/02/omfg-steak-4/)

2.5 lb steaks from 4505 Meats





* #[4505meats](http://dentedreality.com.au/tags/4505meats/)
* #[steak](http://dentedreality.com.au/tags/steak/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6323514774/) [9:44 am, August 2, 2011](http://dentedreality.com.au/2011/08/02/omfg-steak-4/ "9:44 am") 
jQuery(document).ready(function(){
var gmap\_m5166435e17b52f357d89dd6e9c609acf = {
positions : {
872 : new google.maps.LatLng( '37.782666', '-122.388' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5166435e17b52f357d89dd6e9c609acf' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5166435e17b52f357d89dd6e9c609acf.positions ) {
gmap\_m5166435e17b52f357d89dd6e9c609acf.bounds.extend( gmap\_m5166435e17b52f357d89dd6e9c609acf.positions[m] );
}
// Render markers
for ( var m in gmap\_m5166435e17b52f357d89dd6e9c609acf.positions ) {
gmap\_m5166435e17b52f357d89dd6e9c609acf.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5166435e17b52f357d89dd6e9c609acf.map,
position : gmap\_m5166435e17b52f357d89dd6e9c609acf.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5166435e17b52f357d89dd6e9c609acf.map.setCenter( gmap\_m5166435e17b52f357d89dd6e9c609acf.positions[872] );
});