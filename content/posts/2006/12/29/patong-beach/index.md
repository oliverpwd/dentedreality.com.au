---
title: Patong Beach
date: '2006-12-29T20:30:45+00:00'
format: image
service: flickr
tags:
- beach
- patong
- patongbeach
- phuket
- thailand
- thailand06
- umbrella
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349563496_435334d630_o.jpg?resize=607%2C455
---

[![Patong Beach](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349563496_435334d630_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/29/patong-beach/) 
# [Patong Beach](http://dentedreality.com.au/2006/12/29/patong-beach/)





* #[beach](http://dentedreality.com.au/tags/beach/)
* #[patong](http://dentedreality.com.au/tags/patong/)
* #[patongbeach](http://dentedreality.com.au/tags/patongbeach/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)
* #[umbrella](http://dentedreality.com.au/tags/umbrella/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349563496/) [8:30 pm, December 29, 2006](http://dentedreality.com.au/2006/12/29/patong-beach/ "8:30 pm") 
jQuery(document).ready(function(){
var gmap\_m6847d4c1d7451acdc16af52e0806f775 = {
positions : {
213 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6847d4c1d7451acdc16af52e0806f775' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6847d4c1d7451acdc16af52e0806f775.positions ) {
gmap\_m6847d4c1d7451acdc16af52e0806f775.bounds.extend( gmap\_m6847d4c1d7451acdc16af52e0806f775.positions[m] );
}
// Render markers
for ( var m in gmap\_m6847d4c1d7451acdc16af52e0806f775.positions ) {
gmap\_m6847d4c1d7451acdc16af52e0806f775.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6847d4c1d7451acdc16af52e0806f775.map,
position : gmap\_m6847d4c1d7451acdc16af52e0806f775.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6847d4c1d7451acdc16af52e0806f775.map.setCenter( gmap\_m6847d4c1d7451acdc16af52e0806f775.positions[213] );
});