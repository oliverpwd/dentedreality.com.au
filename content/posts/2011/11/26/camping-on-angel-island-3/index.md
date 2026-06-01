---
title: Camping on Angel Island
date: '2011-11-26T05:12:50+00:00'
format: image
service: flickr
tags:
- angelisland
- california
- camping
- outdoors
- sanfrancisco
- tony
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6812210158_0201a8d22b_o.jpg?resize=607%2C452
---

[![Camping on Angel Island](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6812210158_0201a8d22b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/11/26/camping-on-angel-island-3/) 
# [Camping on Angel Island](http://dentedreality.com.au/2011/11/26/camping-on-angel-island-3/)





* #[angelisland](http://dentedreality.com.au/tags/angelisland/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[camping](http://dentedreality.com.au/tags/camping/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[tony](http://dentedreality.com.au/tags/tony/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812210158/) [5:12 am, November 26, 2011](http://dentedreality.com.au/2011/11/26/camping-on-angel-island-3/ "5:12 am") 
jQuery(document).ready(function(){
var gmap\_m846748b13a04c7d65788c47361ea7e9a = {
positions : {
374 : new google.maps.LatLng( '37.865', '-122.425001' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m846748b13a04c7d65788c47361ea7e9a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m846748b13a04c7d65788c47361ea7e9a.positions ) {
gmap\_m846748b13a04c7d65788c47361ea7e9a.bounds.extend( gmap\_m846748b13a04c7d65788c47361ea7e9a.positions[m] );
}
// Render markers
for ( var m in gmap\_m846748b13a04c7d65788c47361ea7e9a.positions ) {
gmap\_m846748b13a04c7d65788c47361ea7e9a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m846748b13a04c7d65788c47361ea7e9a.map,
position : gmap\_m846748b13a04c7d65788c47361ea7e9a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m846748b13a04c7d65788c47361ea7e9a.map.setCenter( gmap\_m846748b13a04c7d65788c47361ea7e9a.positions[374] );
});