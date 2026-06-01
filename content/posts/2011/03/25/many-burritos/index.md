---
title: Many Burritos
date: '2011-03-25T09:26:13+00:00'
format: image
service: flickr
tags:
- burrito
- burritofriday
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802102647_93c4c3b287_o.jpg?resize=607%2C813
---

[![Many Burritos](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802102647_93c4c3b287_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/03/25/many-burritos/) 
# [Many Burritos](http://dentedreality.com.au/2011/03/25/many-burritos/)

Makes me happy





* #[burrito](http://dentedreality.com.au/tags/burrito/)
* #[burritofriday](http://dentedreality.com.au/tags/burritofriday/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802102647/) [9:26 am, March 25, 2011](http://dentedreality.com.au/2011/03/25/many-burritos/ "9:26 am") 
jQuery(document).ready(function(){
var gmap\_m9f986d26c06a228b7b7d43f4613b0150 = {
positions : {
111 : new google.maps.LatLng( '37.782833', '-122.387667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9f986d26c06a228b7b7d43f4613b0150' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9f986d26c06a228b7b7d43f4613b0150.positions ) {
gmap\_m9f986d26c06a228b7b7d43f4613b0150.bounds.extend( gmap\_m9f986d26c06a228b7b7d43f4613b0150.positions[m] );
}
// Render markers
for ( var m in gmap\_m9f986d26c06a228b7b7d43f4613b0150.positions ) {
gmap\_m9f986d26c06a228b7b7d43f4613b0150.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9f986d26c06a228b7b7d43f4613b0150.map,
position : gmap\_m9f986d26c06a228b7b7d43f4613b0150.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9f986d26c06a228b7b7d43f4613b0150.map.setCenter( gmap\_m9f986d26c06a228b7b7d43f4613b0150.positions[111] );
});