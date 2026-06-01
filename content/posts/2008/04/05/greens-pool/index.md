---
title: Green’s Pool
date: '2008-04-05T17:52:28+00:00'
format: image
service: flickr
tags:
- australia
- beach
- greenspool
- ocean
- renniewedding
- timswedding
- westernaustraliadenmark
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433435850_5ca8d89bb7_o.jpg?resize=607%2C455
---

[![Green's Pool](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433435850_5ca8d89bb7_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2008/04/05/greens-pool/) 
# [Green’s Pool](http://dentedreality.com.au/2008/04/05/greens-pool/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[greenspool](http://dentedreality.com.au/tags/greenspool/)
* #[ocean](http://dentedreality.com.au/tags/ocean/)
* #[renniewedding](http://dentedreality.com.au/tags/renniewedding/)
* #[timswedding](http://dentedreality.com.au/tags/timswedding/)
* #[westernaustraliadenmark](http://dentedreality.com.au/tags/westernaustraliadenmark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2433435850/) [5:52 pm, April 5, 2008](http://dentedreality.com.au/2008/04/05/greens-pool/ "5:52 pm") 
jQuery(document).ready(function(){
var gmap\_m9a8ee6934536fb70af1d03180dcf5975 = {
positions : {
831 : new google.maps.LatLng( '-34.983877', '117.298278' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9a8ee6934536fb70af1d03180dcf5975' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9a8ee6934536fb70af1d03180dcf5975.positions ) {
gmap\_m9a8ee6934536fb70af1d03180dcf5975.bounds.extend( gmap\_m9a8ee6934536fb70af1d03180dcf5975.positions[m] );
}
// Render markers
for ( var m in gmap\_m9a8ee6934536fb70af1d03180dcf5975.positions ) {
gmap\_m9a8ee6934536fb70af1d03180dcf5975.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9a8ee6934536fb70af1d03180dcf5975.map,
position : gmap\_m9a8ee6934536fb70af1d03180dcf5975.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9a8ee6934536fb70af1d03180dcf5975.map.setCenter( gmap\_m9a8ee6934536fb70af1d03180dcf5975.positions[831] );
});