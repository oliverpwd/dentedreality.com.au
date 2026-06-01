---
title: The Acropolis, from The Agora
date: '2010-11-09T10:04:41-06:00'
format: image
service: flickr
tags:
- acropolis
- agora
- Athens
- automattic
- greece
- teamsocial
latitude: '37.975'
longitude: '23.7215'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14185852/5183192317_3b8a4c0885_o.jpg
---

[![The Acropolis, from The Agora](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14185852/5183192317_3b8a4c0885_o.jpg)](https://dentedreality.com.au/2010/11/09/the-acropolis-from-the-agora/) 
# [The Acropolis, from The Agora](https://dentedreality.com.au/2010/11/09/the-acropolis-from-the-agora/)

[![The Acropolis, from The Agora](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14185852/5183192317_3b8a4c0885_o.jpg)](http://www.flickr.com/photos/borkazoid/5183192317/)

37.97523.7215




* #[acropolis](https://dentedreality.com.au/tags/acropolis/)
* #[agora](https://dentedreality.com.au/tags/agora/)
* #[Athens](https://dentedreality.com.au/tags/athens/)
* #[automattic](https://dentedreality.com.au/tags/automattic/)
* #[greece](https://dentedreality.com.au/tags/greece/)
* #[teamsocial](https://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183192317/) [10:04 am, November 9, 2010](https://dentedreality.com.au/2010/11/09/the-acropolis-from-the-agora/ "10:04 am") 
jQuery(document).ready(function(){
var gmap\_m64562463e4b703f1760d6712e371a242 = {
positions : {
661 : new google.maps.LatLng( '37.975', '23.7215' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m64562463e4b703f1760d6712e371a242' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m64562463e4b703f1760d6712e371a242.positions ) {
gmap\_m64562463e4b703f1760d6712e371a242.bounds.extend( gmap\_m64562463e4b703f1760d6712e371a242.positions[m] );
}
// Render markers
for ( var m in gmap\_m64562463e4b703f1760d6712e371a242.positions ) {
gmap\_m64562463e4b703f1760d6712e371a242.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m64562463e4b703f1760d6712e371a242.map,
position : gmap\_m64562463e4b703f1760d6712e371a242.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m64562463e4b703f1760d6712e371a242.map.setCenter( gmap\_m64562463e4b703f1760d6712e371a242.positions[661] );
});