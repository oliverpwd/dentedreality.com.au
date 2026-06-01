---
title: Central Park
date: '2012-07-29T08:35:57+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- centralpark
- me
- newyork
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/07/8245784440_7217b8d4cd_o.jpg?resize=607%2C455
---

[![Central Park](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/07/8245784440_7217b8d4cd_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2012/07/29/central-park/) 
# [Central Park](http://dentedreality.com.au/2012/07/29/central-park/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[centralpark](http://dentedreality.com.au/tags/centralpark/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245784440/) [8:35 am, July 29, 2012](http://dentedreality.com.au/2012/07/29/central-park/ "8:35 am") 
jQuery(document).ready(function(){
var gmap\_mfda9aebc64d28f13f72d21f7974697dc = {
positions : {
905 : new google.maps.LatLng( '40.774194', '-73.970648' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mfda9aebc64d28f13f72d21f7974697dc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mfda9aebc64d28f13f72d21f7974697dc.positions ) {
gmap\_mfda9aebc64d28f13f72d21f7974697dc.bounds.extend( gmap\_mfda9aebc64d28f13f72d21f7974697dc.positions[m] );
}
// Render markers
for ( var m in gmap\_mfda9aebc64d28f13f72d21f7974697dc.positions ) {
gmap\_mfda9aebc64d28f13f72d21f7974697dc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mfda9aebc64d28f13f72d21f7974697dc.map,
position : gmap\_mfda9aebc64d28f13f72d21f7974697dc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mfda9aebc64d28f13f72d21f7974697dc.map.setCenter( gmap\_mfda9aebc64d28f13f72d21f7974697dc.positions[905] );
});