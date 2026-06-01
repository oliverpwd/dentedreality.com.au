---
title: Epic Australian Adventure, 2014
date: '2014-03-28T14:01:31+00:00'
format: image
service: flickr
tags:
- Melbourne
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904768482_8d73a9e7f2_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904768482_8d73a9e7f2_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/28/epic-australian-adventure-2014-24/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/28/epic-australian-adventure-2014-24/)

Perth, Mooloolaba and Melbourne





* #[Melbourne](http://dentedreality.com.au/tags/melbourne/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904768482/) [2:01 pm, March 28, 2014](http://dentedreality.com.au/2014/03/28/epic-australian-adventure-2014-24/ "2:01 pm") 
jQuery(document).ready(function(){
var gmap\_m9e87d377cd3905450c72e068e530a7be = {
positions : {
127 : new google.maps.LatLng( '-37.819156', '144.965911' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9e87d377cd3905450c72e068e530a7be' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9e87d377cd3905450c72e068e530a7be.positions ) {
gmap\_m9e87d377cd3905450c72e068e530a7be.bounds.extend( gmap\_m9e87d377cd3905450c72e068e530a7be.positions[m] );
}
// Render markers
for ( var m in gmap\_m9e87d377cd3905450c72e068e530a7be.positions ) {
gmap\_m9e87d377cd3905450c72e068e530a7be.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9e87d377cd3905450c72e068e530a7be.map,
position : gmap\_m9e87d377cd3905450c72e068e530a7be.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9e87d377cd3905450c72e068e530a7be.map.setCenter( gmap\_m9e87d377cd3905450c72e068e530a7be.positions[127] );
});