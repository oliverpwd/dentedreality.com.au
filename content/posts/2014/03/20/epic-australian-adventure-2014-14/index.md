---
title: Epic Australian Adventure, 2014
date: '2014-03-20T05:25:27+00:00'
format: image
service: flickr
tags:
- mooloolaba
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904732292_25fd02b594_o.jpg?resize=607%2C182
---

[![Epic Australian Adventure, 2014](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904732292_25fd02b594_o.jpg?resize=607%2C182)](http://dentedreality.com.au/2014/03/20/epic-australian-adventure-2014-14/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/20/epic-australian-adventure-2014-14/)

Perth, Mooloolaba and Melbourne





* #[mooloolaba](http://dentedreality.com.au/tags/mooloolaba/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904732292/) [5:25 am, March 20, 2014](http://dentedreality.com.au/2014/03/20/epic-australian-adventure-2014-14/ "5:25 am") 
jQuery(document).ready(function(){
var gmap\_mbe4966c8dc80a474f358720d0264b51f = {
positions : {
59 : new google.maps.LatLng( '-26.678684', '153.119522' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbe4966c8dc80a474f358720d0264b51f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbe4966c8dc80a474f358720d0264b51f.positions ) {
gmap\_mbe4966c8dc80a474f358720d0264b51f.bounds.extend( gmap\_mbe4966c8dc80a474f358720d0264b51f.positions[m] );
}
// Render markers
for ( var m in gmap\_mbe4966c8dc80a474f358720d0264b51f.positions ) {
gmap\_mbe4966c8dc80a474f358720d0264b51f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbe4966c8dc80a474f358720d0264b51f.map,
position : gmap\_mbe4966c8dc80a474f358720d0264b51f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbe4966c8dc80a474f358720d0264b51f.map.setCenter( gmap\_mbe4966c8dc80a474f358720d0264b51f.positions[59] );
});