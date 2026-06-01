---
title: Epic Australian Adventure, 2014
date: '2014-03-25T13:50:56+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927919533_b9dee04340_o.jpg?resize=607%2C809
---

[![Epic Australian Adventure, 2014](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13927919533_b9dee04340_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-32/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-32/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927919533/) [1:50 pm, March 25, 2014](http://dentedreality.com.au/2014/03/25/epic-australian-adventure-2014-32/ "1:50 pm") 
jQuery(document).ready(function(){
var gmap\_mf5cd276a23f3c0989f9f0685f3213e25 = {
positions : {
47 : new google.maps.LatLng( '-37.815195', '144.966688' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf5cd276a23f3c0989f9f0685f3213e25' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf5cd276a23f3c0989f9f0685f3213e25.positions ) {
gmap\_mf5cd276a23f3c0989f9f0685f3213e25.bounds.extend( gmap\_mf5cd276a23f3c0989f9f0685f3213e25.positions[m] );
}
// Render markers
for ( var m in gmap\_mf5cd276a23f3c0989f9f0685f3213e25.positions ) {
gmap\_mf5cd276a23f3c0989f9f0685f3213e25.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf5cd276a23f3c0989f9f0685f3213e25.map,
position : gmap\_mf5cd276a23f3c0989f9f0685f3213e25.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf5cd276a23f3c0989f9f0685f3213e25.map.setCenter( gmap\_mf5cd276a23f3c0989f9f0685f3213e25.positions[47] );
});