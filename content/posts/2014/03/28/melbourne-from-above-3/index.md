---
title: Melbourne From Above
date: '2014-03-28T13:45:54+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904759386_03a465256a_o.jpg?resize=607%2C455
---

[![Melbourne From Above](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904759386_03a465256a_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/28/melbourne-from-above-3/) 
# [Melbourne From Above](http://dentedreality.com.au/2014/03/28/melbourne-from-above-3/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904759386/) [1:45 pm, March 28, 2014](http://dentedreality.com.au/2014/03/28/melbourne-from-above-3/ "1:45 pm") 
jQuery(document).ready(function(){
var gmap\_m4e88abc9cd85cf0ff0ba25ffac6e29d4 = {
positions : {
189 : new google.maps.LatLng( '-37.823939', '144.962752' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4e88abc9cd85cf0ff0ba25ffac6e29d4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4e88abc9cd85cf0ff0ba25ffac6e29d4.positions ) {
gmap\_m4e88abc9cd85cf0ff0ba25ffac6e29d4.bounds.extend( gmap\_m4e88abc9cd85cf0ff0ba25ffac6e29d4.positions[m] );
}
// Render markers
for ( var m in gmap\_m4e88abc9cd85cf0ff0ba25ffac6e29d4.positions ) {
gmap\_m4e88abc9cd85cf0ff0ba25ffac6e29d4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4e88abc9cd85cf0ff0ba25ffac6e29d4.map,
position : gmap\_m4e88abc9cd85cf0ff0ba25ffac6e29d4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4e88abc9cd85cf0ff0ba25ffac6e29d4.map.setCenter( gmap\_m4e88abc9cd85cf0ff0ba25ffac6e29d4.positions[189] );
});