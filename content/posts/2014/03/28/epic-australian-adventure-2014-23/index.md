---
title: Epic Australian Adventure, 2014
date: '2014-03-28T16:34:47+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904760141_77619194a6_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904760141_77619194a6_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/28/epic-australian-adventure-2014-23/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/28/epic-australian-adventure-2014-23/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904760141/) [4:34 pm, March 28, 2014](http://dentedreality.com.au/2014/03/28/epic-australian-adventure-2014-23/ "4:34 pm") 
jQuery(document).ready(function(){
var gmap\_me86bd980062159154b73184d5aef4b37 = {
positions : {
858 : new google.maps.LatLng( '-37.818356', '144.968186' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me86bd980062159154b73184d5aef4b37' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me86bd980062159154b73184d5aef4b37.positions ) {
gmap\_me86bd980062159154b73184d5aef4b37.bounds.extend( gmap\_me86bd980062159154b73184d5aef4b37.positions[m] );
}
// Render markers
for ( var m in gmap\_me86bd980062159154b73184d5aef4b37.positions ) {
gmap\_me86bd980062159154b73184d5aef4b37.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me86bd980062159154b73184d5aef4b37.map,
position : gmap\_me86bd980062159154b73184d5aef4b37.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me86bd980062159154b73184d5aef4b37.map.setCenter( gmap\_me86bd980062159154b73184d5aef4b37.positions[858] );
});