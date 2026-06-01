---
title: Automatticians on a Boat
date: '2011-05-05T12:20:26+00:00'
format: image
service: flickr
tags:
- boat
- francisco
- sailing
- SAN
- sanfranciscobay
- sheri
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802149163_7266b5a245_o.jpg?resize=607%2C452
---

[![Automatticians on a Boat](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802149163_7266b5a245_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/05/automatticians-on-a-boat-5/) 
# [Automatticians on a Boat](http://dentedreality.com.au/2011/05/05/automatticians-on-a-boat-5/)

Pete took us out sailing on the Bay. It was most awesome.





* #[boat](http://dentedreality.com.au/tags/boat/)
* #[francisco](http://dentedreality.com.au/tags/francisco/)
* #[sailing](http://dentedreality.com.au/tags/sailing/)
* #[SAN](http://dentedreality.com.au/tags/san/)
* #[sanfranciscobay](http://dentedreality.com.au/tags/sanfranciscobay/)
* #[sheri](http://dentedreality.com.au/tags/sheri/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802149163/) [12:20 pm, May 5, 2011](http://dentedreality.com.au/2011/05/05/automatticians-on-a-boat-5/ "12:20 pm") 
jQuery(document).ready(function(){
var gmap\_m5d73db920f30a60414915160325b3b24 = {
positions : {
489 : new google.maps.LatLng( '37.863833', '-122.485834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5d73db920f30a60414915160325b3b24' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5d73db920f30a60414915160325b3b24.positions ) {
gmap\_m5d73db920f30a60414915160325b3b24.bounds.extend( gmap\_m5d73db920f30a60414915160325b3b24.positions[m] );
}
// Render markers
for ( var m in gmap\_m5d73db920f30a60414915160325b3b24.positions ) {
gmap\_m5d73db920f30a60414915160325b3b24.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5d73db920f30a60414915160325b3b24.map,
position : gmap\_m5d73db920f30a60414915160325b3b24.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5d73db920f30a60414915160325b3b24.map.setCenter( gmap\_m5d73db920f30a60414915160325b3b24.positions[489] );
});