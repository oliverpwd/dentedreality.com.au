---
title: Tech Cleaning
date: '2009-12-13T11:33:18+00:00'
format: image
service: flickr
tags:
- Chile
- cleaning
- Santiago
- vim
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2009/12/4202703745_670c853668_o.jpg?resize=607%2C809
---

[![Tech Cleaning](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2009/12/4202703745_670c853668_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2009/12/13/tech-cleaning/) 
# [Tech Cleaning](http://dentedreality.com.au/2009/12/13/tech-cleaning/)

First there was AJAX, now there is Viim.





* #[Chile](http://dentedreality.com.au/tags/chile/)
* #[cleaning](http://dentedreality.com.au/tags/cleaning/)
* #[Santiago](http://dentedreality.com.au/tags/santiago/)
* #[vim](http://dentedreality.com.au/tags/vim/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4202703745/) [11:33 am, December 13, 2009](http://dentedreality.com.au/2009/12/13/tech-cleaning/ "11:33 am") 
jQuery(document).ready(function(){
var gmap\_m95f0b3c7347ef0370123258730aef2cd = {
positions : {
182 : new google.maps.LatLng( '-33.425667', '-70.618334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m95f0b3c7347ef0370123258730aef2cd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m95f0b3c7347ef0370123258730aef2cd.positions ) {
gmap\_m95f0b3c7347ef0370123258730aef2cd.bounds.extend( gmap\_m95f0b3c7347ef0370123258730aef2cd.positions[m] );
}
// Render markers
for ( var m in gmap\_m95f0b3c7347ef0370123258730aef2cd.positions ) {
gmap\_m95f0b3c7347ef0370123258730aef2cd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m95f0b3c7347ef0370123258730aef2cd.map,
position : gmap\_m95f0b3c7347ef0370123258730aef2cd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m95f0b3c7347ef0370123258730aef2cd.map.setCenter( gmap\_m95f0b3c7347ef0370123258730aef2cd.positions[182] );
});