---
title: Cool Graffiti
date: '2011-11-12T11:57:46+00:00'
format: image
service: flickr
tags:
- graffiti
- sanfrancisco
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6958310367_6612b715ae_o.jpg?resize=607%2C452
---

[![Cool Graffiti](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6958310367_6612b715ae_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/11/12/cool-graffiti-2/) 
# [Cool Graffiti](http://dentedreality.com.au/2011/11/12/cool-graffiti-2/)





* #[graffiti](http://dentedreality.com.au/tags/graffiti/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958310367/) [11:57 am, November 12, 2011](http://dentedreality.com.au/2011/11/12/cool-graffiti-2/ "11:57 am") 
jQuery(document).ready(function(){
var gmap\_me07d7b81958f2da5cdbf457211c3e8cc = {
positions : {
624 : new google.maps.LatLng( '37.7905', '-122.419834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me07d7b81958f2da5cdbf457211c3e8cc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me07d7b81958f2da5cdbf457211c3e8cc.positions ) {
gmap\_me07d7b81958f2da5cdbf457211c3e8cc.bounds.extend( gmap\_me07d7b81958f2da5cdbf457211c3e8cc.positions[m] );
}
// Render markers
for ( var m in gmap\_me07d7b81958f2da5cdbf457211c3e8cc.positions ) {
gmap\_me07d7b81958f2da5cdbf457211c3e8cc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me07d7b81958f2da5cdbf457211c3e8cc.map,
position : gmap\_me07d7b81958f2da5cdbf457211c3e8cc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me07d7b81958f2da5cdbf457211c3e8cc.map.setCenter( gmap\_me07d7b81958f2da5cdbf457211c3e8cc.positions[624] );
});