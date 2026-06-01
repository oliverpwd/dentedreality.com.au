---
title: ''
date: '2017-03-02T19:57:23-07:00'
format: image
service: instagram
tags:
- meetup
latitude: '39.7638893'
longitude: '-104.9813919'
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/03/17076299_178391955992964_7012924284259532800_n.jpg?fit=640%2C640
---

[![Final night #meetup dinner.](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/03/17076299_178391955992964_7012924284259532800_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2017/03/02/final-night-meetup-dinner/) 

[![Final night #meetup dinner.](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/03/17076299_178391955992964_7012924284259532800_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BRKPdC3B0Yz/)

Final night #meetup dinner.

39.7638893-104.9813919




* #[meetup](https://dentedreality.com.au/tags/meetup/)

Posted on [Instagram](https://www.instagram.com/p/BRKPdC3B0Yz/) [7:57 pm, March 2, 2017](https://dentedreality.com.au/2017/03/02/final-night-meetup-dinner/ "7:57 pm") 
jQuery(document).ready(function(){
var gmap\_ma7f2dd4044a9e807a31528c911c3f4e8 = {
positions : {
914 : new google.maps.LatLng( '39.7638893', '-104.9813919' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma7f2dd4044a9e807a31528c911c3f4e8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma7f2dd4044a9e807a31528c911c3f4e8.positions ) {
gmap\_ma7f2dd4044a9e807a31528c911c3f4e8.bounds.extend( gmap\_ma7f2dd4044a9e807a31528c911c3f4e8.positions[m] );
}
// Render markers
for ( var m in gmap\_ma7f2dd4044a9e807a31528c911c3f4e8.positions ) {
gmap\_ma7f2dd4044a9e807a31528c911c3f4e8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma7f2dd4044a9e807a31528c911c3f4e8.map,
position : gmap\_ma7f2dd4044a9e807a31528c911c3f4e8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma7f2dd4044a9e807a31528c911c3f4e8.map.setCenter( gmap\_ma7f2dd4044a9e807a31528c911c3f4e8.positions[914] );
});