---
title: Breakfast
date: '2010-12-26T06:42:50+00:00'
format: image
service: flickr
tags:
- bacon
- breakfast
- eggs
- meal
- mushrooms
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434095883_19bd5b4c17_o.jpg?resize=607%2C452
---

[![Breakfast](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434095883_19bd5b4c17_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/12/26/breakfast-5/) 
# [Breakfast](http://dentedreality.com.au/2010/12/26/breakfast-5/)





* #[bacon](http://dentedreality.com.au/tags/bacon/)
* #[breakfast](http://dentedreality.com.au/tags/breakfast/)
* #[eggs](http://dentedreality.com.au/tags/eggs/)
* #[meal](http://dentedreality.com.au/tags/meal/)
* #[mushrooms](http://dentedreality.com.au/tags/mushrooms/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434095883/) [6:42 am, December 26, 2010](http://dentedreality.com.au/2010/12/26/breakfast-5/ "6:42 am") 
jQuery(document).ready(function(){
var gmap\_me780f78c6d2c5cea66524cc22e7ba97d = {
positions : {
921 : new google.maps.LatLng( '-32.053', '115.846499' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me780f78c6d2c5cea66524cc22e7ba97d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me780f78c6d2c5cea66524cc22e7ba97d.positions ) {
gmap\_me780f78c6d2c5cea66524cc22e7ba97d.bounds.extend( gmap\_me780f78c6d2c5cea66524cc22e7ba97d.positions[m] );
}
// Render markers
for ( var m in gmap\_me780f78c6d2c5cea66524cc22e7ba97d.positions ) {
gmap\_me780f78c6d2c5cea66524cc22e7ba97d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me780f78c6d2c5cea66524cc22e7ba97d.map,
position : gmap\_me780f78c6d2c5cea66524cc22e7ba97d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me780f78c6d2c5cea66524cc22e7ba97d.map.setCenter( gmap\_me780f78c6d2c5cea66524cc22e7ba97d.positions[921] );
});