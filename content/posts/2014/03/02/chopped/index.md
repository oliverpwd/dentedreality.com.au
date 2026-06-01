---
title: Chopped
date: '2014-03-02T10:17:09+00:00'
format: image
service: flickr
tags:
- chopped
- hatchet
- log
- wood
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927015963_fb5cfe2e1b_o.jpg?fit=1500%2C1500
---

[![Chopped](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927015963_fb5cfe2e1b_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/03/02/chopped/) 
# [Chopped](http://dentedreality.com.au/2014/03/02/chopped/)

The first thing chopped with my Gransfors Bruk hatchet





* #[chopped](http://dentedreality.com.au/tags/chopped/)
* #[hatchet](http://dentedreality.com.au/tags/hatchet/)
* #[log](http://dentedreality.com.au/tags/log/)
* #[wood](http://dentedreality.com.au/tags/wood/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927015963/) [10:17 am, March 2, 2014](http://dentedreality.com.au/2014/03/02/chopped/ "10:17 am") 
jQuery(document).ready(function(){
var gmap\_me9deb3dd617f5ce7dac72eeff6f6c046 = {
positions : {
533 : new google.maps.LatLng( '40.669247', '-73.984764' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me9deb3dd617f5ce7dac72eeff6f6c046' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me9deb3dd617f5ce7dac72eeff6f6c046.positions ) {
gmap\_me9deb3dd617f5ce7dac72eeff6f6c046.bounds.extend( gmap\_me9deb3dd617f5ce7dac72eeff6f6c046.positions[m] );
}
// Render markers
for ( var m in gmap\_me9deb3dd617f5ce7dac72eeff6f6c046.positions ) {
gmap\_me9deb3dd617f5ce7dac72eeff6f6c046.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me9deb3dd617f5ce7dac72eeff6f6c046.map,
position : gmap\_me9deb3dd617f5ce7dac72eeff6f6c046.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me9deb3dd617f5ce7dac72eeff6f6c046.map.setCenter( gmap\_me9deb3dd617f5ce7dac72eeff6f6c046.positions[533] );
});