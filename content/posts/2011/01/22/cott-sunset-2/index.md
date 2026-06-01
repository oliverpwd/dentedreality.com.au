---
title: Cott Sunset
date: '2011-01-22T15:21:31+00:00'
format: image
service: flickr
tags:
- australia
- beach
- cottesloe
- sunset
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434790272_22557e0e23_o.jpg?resize=607%2C452
---

[![Cott Sunset](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434790272_22557e0e23_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/22/cott-sunset-2/) 
# [Cott Sunset](http://dentedreality.com.au/2011/01/22/cott-sunset-2/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[cottesloe](http://dentedreality.com.au/tags/cottesloe/)
* #[sunset](http://dentedreality.com.au/tags/sunset/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434790272/) [3:21 pm, January 22, 2011](http://dentedreality.com.au/2011/01/22/cott-sunset-2/ "3:21 pm") 
jQuery(document).ready(function(){
var gmap\_m7d6b5c773f65eed10f6846887f629f0b = {
positions : {
189 : new google.maps.LatLng( '-31.994667', '115.7515' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7d6b5c773f65eed10f6846887f629f0b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7d6b5c773f65eed10f6846887f629f0b.positions ) {
gmap\_m7d6b5c773f65eed10f6846887f629f0b.bounds.extend( gmap\_m7d6b5c773f65eed10f6846887f629f0b.positions[m] );
}
// Render markers
for ( var m in gmap\_m7d6b5c773f65eed10f6846887f629f0b.positions ) {
gmap\_m7d6b5c773f65eed10f6846887f629f0b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7d6b5c773f65eed10f6846887f629f0b.map,
position : gmap\_m7d6b5c773f65eed10f6846887f629f0b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7d6b5c773f65eed10f6846887f629f0b.map.setCenter( gmap\_m7d6b5c773f65eed10f6846887f629f0b.positions[189] );
});