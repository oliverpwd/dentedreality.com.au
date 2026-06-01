---
title: Epic Australian Adventure, 2014
date: '2014-03-21T17:37:02+00:00'
format: image
service: flickr
tags:
- mooloolaba
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904739712_dd4393b0cc_o.jpg?resize=607%2C809
---

[![Epic Australian Adventure, 2014](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904739712_dd4393b0cc_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2014/03/21/epic-australian-adventure-2014-8/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/21/epic-australian-adventure-2014-8/)

Perth, Mooloolaba and Melbourne





* #[mooloolaba](http://dentedreality.com.au/tags/mooloolaba/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904739712/) [5:37 pm, March 21, 2014](http://dentedreality.com.au/2014/03/21/epic-australian-adventure-2014-8/ "5:37 pm") 
jQuery(document).ready(function(){
var gmap\_m7c37e9eb99c791a40b7d1f795790cd9f = {
positions : {
451 : new google.maps.LatLng( '-26.678184', '153.117827' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7c37e9eb99c791a40b7d1f795790cd9f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7c37e9eb99c791a40b7d1f795790cd9f.positions ) {
gmap\_m7c37e9eb99c791a40b7d1f795790cd9f.bounds.extend( gmap\_m7c37e9eb99c791a40b7d1f795790cd9f.positions[m] );
}
// Render markers
for ( var m in gmap\_m7c37e9eb99c791a40b7d1f795790cd9f.positions ) {
gmap\_m7c37e9eb99c791a40b7d1f795790cd9f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7c37e9eb99c791a40b7d1f795790cd9f.map,
position : gmap\_m7c37e9eb99c791a40b7d1f795790cd9f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7c37e9eb99c791a40b7d1f795790cd9f.map.setCenter( gmap\_m7c37e9eb99c791a40b7d1f795790cd9f.positions[451] );
});