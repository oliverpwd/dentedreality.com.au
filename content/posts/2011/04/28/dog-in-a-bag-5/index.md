---
title: Dog in a Bag
date: '2011-04-28T05:30:04+00:00'
format: image
service: flickr
tags:
- bag
- dog
- muni
- sanfrancisco
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802148177_e18c589545_o.jpg?resize=607%2C813
---

[![Dog in a Bag](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802148177_e18c589545_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/04/28/dog-in-a-bag-5/) 
# [Dog in a Bag](http://dentedreality.com.au/2011/04/28/dog-in-a-bag-5/)

Good old Muni





* #[bag](http://dentedreality.com.au/tags/bag/)
* #[dog](http://dentedreality.com.au/tags/dog/)
* #[muni](http://dentedreality.com.au/tags/muni/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802148177/) [5:30 am, April 28, 2011](http://dentedreality.com.au/2011/04/28/dog-in-a-bag-5/ "5:30 am") 
jQuery(document).ready(function(){
var gmap\_me3e73c73217f7d3a05fdd9b1e79e6897 = {
positions : {
763 : new google.maps.LatLng( '37.793333', '-122.396667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me3e73c73217f7d3a05fdd9b1e79e6897' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me3e73c73217f7d3a05fdd9b1e79e6897.positions ) {
gmap\_me3e73c73217f7d3a05fdd9b1e79e6897.bounds.extend( gmap\_me3e73c73217f7d3a05fdd9b1e79e6897.positions[m] );
}
// Render markers
for ( var m in gmap\_me3e73c73217f7d3a05fdd9b1e79e6897.positions ) {
gmap\_me3e73c73217f7d3a05fdd9b1e79e6897.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me3e73c73217f7d3a05fdd9b1e79e6897.map,
position : gmap\_me3e73c73217f7d3a05fdd9b1e79e6897.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me3e73c73217f7d3a05fdd9b1e79e6897.map.setCenter( gmap\_me3e73c73217f7d3a05fdd9b1e79e6897.positions[763] );
});