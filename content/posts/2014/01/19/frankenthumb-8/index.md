---
title: Frankenthumb
date: '2014-01-19T08:38:24+00:00'
format: image
service: flickr
tags:
- Frankenthumb
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901693896_60e60f5a82_o.jpg?fit=1500%2C1500
---

[![Frankenthumb](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13901693896_60e60f5a82_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2014/01/19/frankenthumb-8/) 
# [Frankenthumb](http://dentedreality.com.au/2014/01/19/frankenthumb-8/)





* #[Frankenthumb](http://dentedreality.com.au/tags/frankenthumb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901693896/) [8:38 am, January 19, 2014](http://dentedreality.com.au/2014/01/19/frankenthumb-8/ "8:38 am") 
jQuery(document).ready(function(){
var gmap\_ma4e23c564edd5125737b75969295176c = {
positions : {
18 : new google.maps.LatLng( '40.669405', '-73.984978' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma4e23c564edd5125737b75969295176c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma4e23c564edd5125737b75969295176c.positions ) {
gmap\_ma4e23c564edd5125737b75969295176c.bounds.extend( gmap\_ma4e23c564edd5125737b75969295176c.positions[m] );
}
// Render markers
for ( var m in gmap\_ma4e23c564edd5125737b75969295176c.positions ) {
gmap\_ma4e23c564edd5125737b75969295176c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma4e23c564edd5125737b75969295176c.map,
position : gmap\_ma4e23c564edd5125737b75969295176c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma4e23c564edd5125737b75969295176c.map.setCenter( gmap\_ma4e23c564edd5125737b75969295176c.positions[18] );
});