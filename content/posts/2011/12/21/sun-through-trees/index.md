---
title: Sun Through Trees
date: '2011-12-21T09:11:04+00:00'
format: image
service: flickr
tags:
- forest
- sun
- trees
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6959403313_2d9b4d9d2d_o.jpg?resize=607%2C452
---

[![Sun Through Trees](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6959403313_2d9b4d9d2d_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/12/21/sun-through-trees/) 
# [Sun Through Trees](http://dentedreality.com.au/2011/12/21/sun-through-trees/)





* #[forest](http://dentedreality.com.au/tags/forest/)
* #[sun](http://dentedreality.com.au/tags/sun/)
* #[trees](http://dentedreality.com.au/tags/trees/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959403313/) [9:11 am, December 21, 2011](http://dentedreality.com.au/2011/12/21/sun-through-trees/ "9:11 am") 
jQuery(document).ready(function(){
var gmap\_me5966138e1d75d54e04808f6640786b3 = {
positions : {
139 : new google.maps.LatLng( '36.163166', '-121.665501' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me5966138e1d75d54e04808f6640786b3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me5966138e1d75d54e04808f6640786b3.positions ) {
gmap\_me5966138e1d75d54e04808f6640786b3.bounds.extend( gmap\_me5966138e1d75d54e04808f6640786b3.positions[m] );
}
// Render markers
for ( var m in gmap\_me5966138e1d75d54e04808f6640786b3.positions ) {
gmap\_me5966138e1d75d54e04808f6640786b3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me5966138e1d75d54e04808f6640786b3.map,
position : gmap\_me5966138e1d75d54e04808f6640786b3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me5966138e1d75d54e04808f6640786b3.map.setCenter( gmap\_me5966138e1d75d54e04808f6640786b3.positions[139] );
});