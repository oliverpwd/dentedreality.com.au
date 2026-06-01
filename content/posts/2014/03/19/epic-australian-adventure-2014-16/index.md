---
title: Epic Australian Adventure, 2014
date: '2014-03-19T04:43:54+00:00'
format: image
service: flickr
tags:
- perth
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928287264_c191c2916c_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928287264_c191c2916c_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/19/epic-australian-adventure-2014-16/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/19/epic-australian-adventure-2014-16/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13928287264/) [4:43 am, March 19, 2014](http://dentedreality.com.au/2014/03/19/epic-australian-adventure-2014-16/ "4:43 am") 
jQuery(document).ready(function(){
var gmap\_m2f874459293efce8de21d6d1b6002a26 = {
positions : {
614 : new google.maps.LatLng( '-31.996698', '115.749694' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2f874459293efce8de21d6d1b6002a26' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2f874459293efce8de21d6d1b6002a26.positions ) {
gmap\_m2f874459293efce8de21d6d1b6002a26.bounds.extend( gmap\_m2f874459293efce8de21d6d1b6002a26.positions[m] );
}
// Render markers
for ( var m in gmap\_m2f874459293efce8de21d6d1b6002a26.positions ) {
gmap\_m2f874459293efce8de21d6d1b6002a26.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2f874459293efce8de21d6d1b6002a26.map,
position : gmap\_m2f874459293efce8de21d6d1b6002a26.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2f874459293efce8de21d6d1b6002a26.map.setCenter( gmap\_m2f874459293efce8de21d6d1b6002a26.positions[614] );
});