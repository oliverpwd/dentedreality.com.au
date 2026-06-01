---
title: Automatticians on a Boat
date: '2011-05-05T12:31:10+00:00'
format: image
service: flickr
tags:
- boat
- francisco
- sailing
- SAN
- sanfranciscobay
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802149899_e1dfa33e5e_o.jpg?resize=607%2C813
---

[![Automatticians on a Boat](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802149899_e1dfa33e5e_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/05/automatticians-on-a-boat-3/) 
# [Automatticians on a Boat](http://dentedreality.com.au/2011/05/05/automatticians-on-a-boat-3/)

Pete took us out sailing on the Bay. It was most awesome.





* #[boat](http://dentedreality.com.au/tags/boat/)
* #[francisco](http://dentedreality.com.au/tags/francisco/)
* #[sailing](http://dentedreality.com.au/tags/sailing/)
* #[SAN](http://dentedreality.com.au/tags/san/)
* #[sanfranciscobay](http://dentedreality.com.au/tags/sanfranciscobay/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802149899/) [12:31 pm, May 5, 2011](http://dentedreality.com.au/2011/05/05/automatticians-on-a-boat-3/ "12:31 pm") 
jQuery(document).ready(function(){
var gmap\_m77ddf529890ac70f9583e35688f02142 = {
positions : {
765 : new google.maps.LatLng( '37.856333', '-122.4725' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m77ddf529890ac70f9583e35688f02142' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m77ddf529890ac70f9583e35688f02142.positions ) {
gmap\_m77ddf529890ac70f9583e35688f02142.bounds.extend( gmap\_m77ddf529890ac70f9583e35688f02142.positions[m] );
}
// Render markers
for ( var m in gmap\_m77ddf529890ac70f9583e35688f02142.positions ) {
gmap\_m77ddf529890ac70f9583e35688f02142.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m77ddf529890ac70f9583e35688f02142.map,
position : gmap\_m77ddf529890ac70f9583e35688f02142.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m77ddf529890ac70f9583e35688f02142.map.setCenter( gmap\_m77ddf529890ac70f9583e35688f02142.positions[765] );
});