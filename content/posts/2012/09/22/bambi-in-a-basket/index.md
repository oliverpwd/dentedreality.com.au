---
title: Bambi in a Basket
date: '2012-09-22T09:27:15-06:00'
format: image
service: flickr
tags:
- bambi
- basket
- dog
- laundry
latitude: '40.667666'
longitude: '-73.984334'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/09/14190721/8245862564_ce3d88916e_o.jpg
---

[![Bambi in a Basket](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/09/14190721/8245862564_ce3d88916e_o.jpg)](https://dentedreality.com.au/2012/09/22/bambi-in-a-basket/) 
# [Bambi in a Basket](https://dentedreality.com.au/2012/09/22/bambi-in-a-basket/)

[![Bambi in a Basket](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2012/09/14190721/8245862564_ce3d88916e_o.jpg)](http://www.flickr.com/photos/borkazoid/8245862564/)

40.667666-73.984334




* #[bambi](https://dentedreality.com.au/tags/bambi/)
* #[basket](https://dentedreality.com.au/tags/basket/)
* #[dog](https://dentedreality.com.au/tags/dog/)
* #[laundry](https://dentedreality.com.au/tags/laundry/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245862564/) [9:27 am, September 22, 2012](https://dentedreality.com.au/2012/09/22/bambi-in-a-basket/ "9:27 am") 
jQuery(document).ready(function(){
var gmap\_m309b2be8136a0e55d4c5d9210dc62ef5 = {
positions : {
209 : new google.maps.LatLng( '40.667666', '-73.984334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m309b2be8136a0e55d4c5d9210dc62ef5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m309b2be8136a0e55d4c5d9210dc62ef5.positions ) {
gmap\_m309b2be8136a0e55d4c5d9210dc62ef5.bounds.extend( gmap\_m309b2be8136a0e55d4c5d9210dc62ef5.positions[m] );
}
// Render markers
for ( var m in gmap\_m309b2be8136a0e55d4c5d9210dc62ef5.positions ) {
gmap\_m309b2be8136a0e55d4c5d9210dc62ef5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m309b2be8136a0e55d4c5d9210dc62ef5.map,
position : gmap\_m309b2be8136a0e55d4c5d9210dc62ef5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m309b2be8136a0e55d4c5d9210dc62ef5.map.setCenter( gmap\_m309b2be8136a0e55d4c5d9210dc62ef5.positions[209] );
});