---
title: Testing Flickr’s new auto-Tweet feature
date: '2009-07-01T08:26:12+00:00'
format: image
service: flickr
tags:
- moblog
- treo650
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2009/07/3678671527_38342a0ae8_o.jpg?resize=607%2C455
---

[![Testing Flickr's new auto-Tweet feature](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2009/07/3678671527_38342a0ae8_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2009/07/01/testing-flickrs-new-auto-tweet-feature/) 
# [Testing Flickr’s new auto-Tweet feature](http://dentedreality.com.au/2009/07/01/testing-flickrs-new-auto-tweet-feature/)





* #[moblog](http://dentedreality.com.au/tags/moblog/)
* #[treo650](http://dentedreality.com.au/tags/treo650/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/3678671527/) [8:26 am, July 1, 2009](http://dentedreality.com.au/2009/07/01/testing-flickrs-new-auto-tweet-feature/ "8:26 am") 
jQuery(document).ready(function(){
var gmap\_m13e9534908adf5c9f551ac8e8997d617 = {
positions : {
159 : new google.maps.LatLng( '37.791333', '-122.4175' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m13e9534908adf5c9f551ac8e8997d617' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m13e9534908adf5c9f551ac8e8997d617.positions ) {
gmap\_m13e9534908adf5c9f551ac8e8997d617.bounds.extend( gmap\_m13e9534908adf5c9f551ac8e8997d617.positions[m] );
}
// Render markers
for ( var m in gmap\_m13e9534908adf5c9f551ac8e8997d617.positions ) {
gmap\_m13e9534908adf5c9f551ac8e8997d617.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m13e9534908adf5c9f551ac8e8997d617.map,
position : gmap\_m13e9534908adf5c9f551ac8e8997d617.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m13e9534908adf5c9f551ac8e8997d617.map.setCenter( gmap\_m13e9534908adf5c9f551ac8e8997d617.positions[159] );
});