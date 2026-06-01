---
title: I Sea Food
date: '2006-12-30T02:37:02+00:00'
format: image
service: flickr
tags:
- fresh
- ice
- lobster
- phuket
- seafood
- thailand
- thailand06
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349561790_037b426db6_o.jpg?resize=607%2C455
---

[![I Sea Food](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349561790_037b426db6_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/30/i-sea-food/) 
# [I Sea Food](http://dentedreality.com.au/2006/12/30/i-sea-food/)





* #[fresh](http://dentedreality.com.au/tags/fresh/)
* #[ice](http://dentedreality.com.au/tags/ice/)
* #[lobster](http://dentedreality.com.au/tags/lobster/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[seafood](http://dentedreality.com.au/tags/seafood/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349561790/) [2:37 am, December 30, 2006](http://dentedreality.com.au/2006/12/30/i-sea-food/ "2:37 am") 
jQuery(document).ready(function(){
var gmap\_me8b6831d8a5e8893cc4f1a38e86b10a1 = {
positions : {
767 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me8b6831d8a5e8893cc4f1a38e86b10a1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me8b6831d8a5e8893cc4f1a38e86b10a1.positions ) {
gmap\_me8b6831d8a5e8893cc4f1a38e86b10a1.bounds.extend( gmap\_me8b6831d8a5e8893cc4f1a38e86b10a1.positions[m] );
}
// Render markers
for ( var m in gmap\_me8b6831d8a5e8893cc4f1a38e86b10a1.positions ) {
gmap\_me8b6831d8a5e8893cc4f1a38e86b10a1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me8b6831d8a5e8893cc4f1a38e86b10a1.map,
position : gmap\_me8b6831d8a5e8893cc4f1a38e86b10a1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me8b6831d8a5e8893cc4f1a38e86b10a1.map.setCenter( gmap\_me8b6831d8a5e8893cc4f1a38e86b10a1.positions[767] );
});