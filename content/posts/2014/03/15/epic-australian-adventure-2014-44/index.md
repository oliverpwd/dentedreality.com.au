---
title: Epic Australian Adventure, 2014
date: '2014-03-15T09:52:17+00:00'
format: image
service: flickr
tags:
- perth
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904713496_396e854ddf_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904713496_396e854ddf_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/15/epic-australian-adventure-2014-44/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/15/epic-australian-adventure-2014-44/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904713496/) [9:52 am, March 15, 2014](http://dentedreality.com.au/2014/03/15/epic-australian-adventure-2014-44/ "9:52 am") 
jQuery(document).ready(function(){
var gmap\_m78f7c7e034e21b06e422768b3847ce40 = {
positions : {
239 : new google.maps.LatLng( '-32.03437', '115.745697' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m78f7c7e034e21b06e422768b3847ce40' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m78f7c7e034e21b06e422768b3847ce40.positions ) {
gmap\_m78f7c7e034e21b06e422768b3847ce40.bounds.extend( gmap\_m78f7c7e034e21b06e422768b3847ce40.positions[m] );
}
// Render markers
for ( var m in gmap\_m78f7c7e034e21b06e422768b3847ce40.positions ) {
gmap\_m78f7c7e034e21b06e422768b3847ce40.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m78f7c7e034e21b06e422768b3847ce40.map,
position : gmap\_m78f7c7e034e21b06e422768b3847ce40.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m78f7c7e034e21b06e422768b3847ce40.map.setCenter( gmap\_m78f7c7e034e21b06e422768b3847ce40.positions[239] );
});