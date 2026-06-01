---
title: Hotel
date: '2013-11-29T05:01:09+00:00'
format: image
service: flickr
tags:
- france
- paris
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900365472_9d6e31406c_o.jpg?resize=607%2C455
---

[![Hotel](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900365472_9d6e31406c_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/29/hotel/) 
# [Hotel](http://dentedreality.com.au/2013/11/29/hotel/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900365472/) [5:01 am, November 29, 2013](http://dentedreality.com.au/2013/11/29/hotel/ "5:01 am") 
jQuery(document).ready(function(){
var gmap\_m2dcca79725bcb43e6ec8abb78c7969f3 = {
positions : {
791 : new google.maps.LatLng( '48.870852', '2.330355' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2dcca79725bcb43e6ec8abb78c7969f3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2dcca79725bcb43e6ec8abb78c7969f3.positions ) {
gmap\_m2dcca79725bcb43e6ec8abb78c7969f3.bounds.extend( gmap\_m2dcca79725bcb43e6ec8abb78c7969f3.positions[m] );
}
// Render markers
for ( var m in gmap\_m2dcca79725bcb43e6ec8abb78c7969f3.positions ) {
gmap\_m2dcca79725bcb43e6ec8abb78c7969f3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2dcca79725bcb43e6ec8abb78c7969f3.map,
position : gmap\_m2dcca79725bcb43e6ec8abb78c7969f3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2dcca79725bcb43e6ec8abb78c7969f3.map.setCenter( gmap\_m2dcca79725bcb43e6ec8abb78c7969f3.positions[791] );
});