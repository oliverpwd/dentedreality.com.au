---
title: Camping on Angel Island
date: '2011-11-26T05:49:41+00:00'
format: image
service: flickr
tags:
- angelisland
- california
- camping
- outdoors
- sanfrancisco
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6958319377_d276a97362_o.jpg?resize=607%2C452
---

[![Camping on Angel Island](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6958319377_d276a97362_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/11/26/camping-on-angel-island-2/) 
# [Camping on Angel Island](http://dentedreality.com.au/2011/11/26/camping-on-angel-island-2/)





* #[angelisland](http://dentedreality.com.au/tags/angelisland/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[camping](http://dentedreality.com.au/tags/camping/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958319377/) [5:49 am, November 26, 2011](http://dentedreality.com.au/2011/11/26/camping-on-angel-island-2/ "5:49 am") 
jQuery(document).ready(function(){
var gmap\_m0e9eff3d3be3284da6eb516249a910e8 = {
positions : {
764 : new google.maps.LatLng( '37.864833', '-122.424334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0e9eff3d3be3284da6eb516249a910e8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0e9eff3d3be3284da6eb516249a910e8.positions ) {
gmap\_m0e9eff3d3be3284da6eb516249a910e8.bounds.extend( gmap\_m0e9eff3d3be3284da6eb516249a910e8.positions[m] );
}
// Render markers
for ( var m in gmap\_m0e9eff3d3be3284da6eb516249a910e8.positions ) {
gmap\_m0e9eff3d3be3284da6eb516249a910e8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0e9eff3d3be3284da6eb516249a910e8.map,
position : gmap\_m0e9eff3d3be3284da6eb516249a910e8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0e9eff3d3be3284da6eb516249a910e8.map.setCenter( gmap\_m0e9eff3d3be3284da6eb516249a910e8.positions[764] );
});