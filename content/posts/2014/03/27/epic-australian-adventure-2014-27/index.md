---
title: Epic Australian Adventure, 2014
date: '2014-03-27T17:52:02+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927879805_f2fa47ffd0_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927879805_f2fa47ffd0_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/27/epic-australian-adventure-2014-27/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/27/epic-australian-adventure-2014-27/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927879805/) [5:52 pm, March 27, 2014](http://dentedreality.com.au/2014/03/27/epic-australian-adventure-2014-27/ "5:52 pm") 
jQuery(document).ready(function(){
var gmap\_m858da01afaa5ab3688bf60f94215c0a1 = {
positions : {
233 : new google.maps.LatLng( '-37.824939', '144.992888' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m858da01afaa5ab3688bf60f94215c0a1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m858da01afaa5ab3688bf60f94215c0a1.positions ) {
gmap\_m858da01afaa5ab3688bf60f94215c0a1.bounds.extend( gmap\_m858da01afaa5ab3688bf60f94215c0a1.positions[m] );
}
// Render markers
for ( var m in gmap\_m858da01afaa5ab3688bf60f94215c0a1.positions ) {
gmap\_m858da01afaa5ab3688bf60f94215c0a1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m858da01afaa5ab3688bf60f94215c0a1.map,
position : gmap\_m858da01afaa5ab3688bf60f94215c0a1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m858da01afaa5ab3688bf60f94215c0a1.map.setCenter( gmap\_m858da01afaa5ab3688bf60f94215c0a1.positions[233] );
});