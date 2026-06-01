---
title: BBQ!
date: '2013-07-22T17:35:33+00:00'
format: image
service: flickr
tags:
- bbq
- delicious
- dino
- meat
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440398512_0f7af37667_o.jpg?resize=607%2C452
---

[![BBQ!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440398512_0f7af37667_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/07/22/bbq/) 
# [BBQ!](http://dentedreality.com.au/2013/07/22/bbq/)

Dino BBQ in Brooklyn





* #[bbq](http://dentedreality.com.au/tags/bbq/)
* #[delicious](http://dentedreality.com.au/tags/delicious-2/)
* #[dino](http://dentedreality.com.au/tags/dino/)
* #[meat](http://dentedreality.com.au/tags/meat/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9440398512/) [5:35 pm, July 22, 2013](http://dentedreality.com.au/2013/07/22/bbq/ "5:35 pm") 
jQuery(document).ready(function(){
var gmap\_m7c96dd702b2af05e4f0b647ad9f40e4e = {
positions : {
157 : new google.maps.LatLng( '40.677666', '-73.984' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7c96dd702b2af05e4f0b647ad9f40e4e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7c96dd702b2af05e4f0b647ad9f40e4e.positions ) {
gmap\_m7c96dd702b2af05e4f0b647ad9f40e4e.bounds.extend( gmap\_m7c96dd702b2af05e4f0b647ad9f40e4e.positions[m] );
}
// Render markers
for ( var m in gmap\_m7c96dd702b2af05e4f0b647ad9f40e4e.positions ) {
gmap\_m7c96dd702b2af05e4f0b647ad9f40e4e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7c96dd702b2af05e4f0b647ad9f40e4e.map,
position : gmap\_m7c96dd702b2af05e4f0b647ad9f40e4e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7c96dd702b2af05e4f0b647ad9f40e4e.map.setCenter( gmap\_m7c96dd702b2af05e4f0b647ad9f40e4e.positions[157] );
});