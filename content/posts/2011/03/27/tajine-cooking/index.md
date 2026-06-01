---
title: Tajine Cooking
date: '2011-03-27T16:13:42+00:00'
format: image
service: flickr
tags:
- cooking
- food
- morroccan
- tajine
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802660006_3d58f13046_o.jpg?resize=607%2C452
---

[![Tajine Cooking](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802660006_3d58f13046_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/03/27/tajine-cooking/) 
# [Tajine Cooking](http://dentedreality.com.au/2011/03/27/tajine-cooking/)





* #[cooking](http://dentedreality.com.au/tags/cooking/)
* #[food](http://dentedreality.com.au/tags/food/)
* #[morroccan](http://dentedreality.com.au/tags/morroccan/)
* #[tajine](http://dentedreality.com.au/tags/tajine/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802660006/) [4:13 pm, March 27, 2011](http://dentedreality.com.au/2011/03/27/tajine-cooking/ "4:13 pm") 
jQuery(document).ready(function(){
var gmap\_med9309db4a2e78a321f230f4670b12f2 = {
positions : {
795 : new google.maps.LatLng( '37.791333', '-122.417834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_med9309db4a2e78a321f230f4670b12f2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_med9309db4a2e78a321f230f4670b12f2.positions ) {
gmap\_med9309db4a2e78a321f230f4670b12f2.bounds.extend( gmap\_med9309db4a2e78a321f230f4670b12f2.positions[m] );
}
// Render markers
for ( var m in gmap\_med9309db4a2e78a321f230f4670b12f2.positions ) {
gmap\_med9309db4a2e78a321f230f4670b12f2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_med9309db4a2e78a321f230f4670b12f2.map,
position : gmap\_med9309db4a2e78a321f230f4670b12f2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_med9309db4a2e78a321f230f4670b12f2.map.setCenter( gmap\_med9309db4a2e78a321f230f4670b12f2.positions[795] );
});