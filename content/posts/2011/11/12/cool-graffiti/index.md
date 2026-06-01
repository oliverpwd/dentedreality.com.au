---
title: Cool Graffiti
date: '2011-11-12T11:58:02+00:00'
format: image
service: flickr
tags:
- graffiti
- sanfrancisco
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6958310489_5034324fd0_o.jpg?resize=607%2C452
---

[![Cool Graffiti](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6958310489_5034324fd0_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/11/12/cool-graffiti/) 
# [Cool Graffiti](http://dentedreality.com.au/2011/11/12/cool-graffiti/)





* #[graffiti](http://dentedreality.com.au/tags/graffiti/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958310489/) [11:58 am, November 12, 2011](http://dentedreality.com.au/2011/11/12/cool-graffiti/ "11:58 am") 
jQuery(document).ready(function(){
var gmap\_mbd1fe8b1641fdf6c5dd5f1d5e96c8942 = {
positions : {
298 : new google.maps.LatLng( '37.788833', '-122.4195' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbd1fe8b1641fdf6c5dd5f1d5e96c8942' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbd1fe8b1641fdf6c5dd5f1d5e96c8942.positions ) {
gmap\_mbd1fe8b1641fdf6c5dd5f1d5e96c8942.bounds.extend( gmap\_mbd1fe8b1641fdf6c5dd5f1d5e96c8942.positions[m] );
}
// Render markers
for ( var m in gmap\_mbd1fe8b1641fdf6c5dd5f1d5e96c8942.positions ) {
gmap\_mbd1fe8b1641fdf6c5dd5f1d5e96c8942.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbd1fe8b1641fdf6c5dd5f1d5e96c8942.map,
position : gmap\_mbd1fe8b1641fdf6c5dd5f1d5e96c8942.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbd1fe8b1641fdf6c5dd5f1d5e96c8942.map.setCenter( gmap\_mbd1fe8b1641fdf6c5dd5f1d5e96c8942.positions[298] );
});