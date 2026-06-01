---
title: Ermagherd Burzse Crurze with COED.com
date: '2012-08-16T15:49:29+00:00'
format: image
service: flickr
tags:
- boozecruise
- cityscape
- coed
- EastRiver
- newyork
- skyline
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8244766017_627f6bd4b1_o.jpg?resize=607%2C452
---

[![Ermagherd Burzse Crurze with COED.com](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8244766017_627f6bd4b1_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-10/) 
# [Ermagherd Burzse Crurze with COED.com](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-10/)





* #[boozecruise](http://dentedreality.com.au/tags/boozecruise/)
* #[cityscape](http://dentedreality.com.au/tags/cityscape/)
* #[coed](http://dentedreality.com.au/tags/coed/)
* #[EastRiver](http://dentedreality.com.au/tags/eastriver/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[skyline](http://dentedreality.com.au/tags/skyline/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8244766017/) [3:49 pm, August 16, 2012](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-10/ "3:49 pm") 
jQuery(document).ready(function(){
var gmap\_m632e1a2c980cd28bc8875bbc27ffb0cb = {
positions : {
191 : new google.maps.LatLng( '40.727333', '-73.9685' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m632e1a2c980cd28bc8875bbc27ffb0cb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m632e1a2c980cd28bc8875bbc27ffb0cb.positions ) {
gmap\_m632e1a2c980cd28bc8875bbc27ffb0cb.bounds.extend( gmap\_m632e1a2c980cd28bc8875bbc27ffb0cb.positions[m] );
}
// Render markers
for ( var m in gmap\_m632e1a2c980cd28bc8875bbc27ffb0cb.positions ) {
gmap\_m632e1a2c980cd28bc8875bbc27ffb0cb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m632e1a2c980cd28bc8875bbc27ffb0cb.map,
position : gmap\_m632e1a2c980cd28bc8875bbc27ffb0cb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m632e1a2c980cd28bc8875bbc27ffb0cb.map.setCenter( gmap\_m632e1a2c980cd28bc8875bbc27ffb0cb.positions[191] );
});