---
title: Ermagherd Burzse Crurze with COED.com
date: '2012-08-16T15:49:35+00:00'
format: image
service: flickr
tags:
- boozecruise
- cityscape
- coed
- EastRiver
- newyork
- skyline
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8244766323_7c88f4964f_o.jpg?resize=607%2C452
---

[![Ermagherd Burzse Crurze with COED.com](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8244766323_7c88f4964f_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-9/) 
# [Ermagherd Burzse Crurze with COED.com](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-9/)





* #[boozecruise](http://dentedreality.com.au/tags/boozecruise/)
* #[cityscape](http://dentedreality.com.au/tags/cityscape/)
* #[coed](http://dentedreality.com.au/tags/coed/)
* #[EastRiver](http://dentedreality.com.au/tags/eastriver/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[skyline](http://dentedreality.com.au/tags/skyline/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8244766323/) [3:49 pm, August 16, 2012](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-9/ "3:49 pm") 
jQuery(document).ready(function(){
var gmap\_mad081fd5e9d9004b5a93cd1eda0f6ee2 = {
positions : {
782 : new google.maps.LatLng( '40.727166', '-73.968334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mad081fd5e9d9004b5a93cd1eda0f6ee2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mad081fd5e9d9004b5a93cd1eda0f6ee2.positions ) {
gmap\_mad081fd5e9d9004b5a93cd1eda0f6ee2.bounds.extend( gmap\_mad081fd5e9d9004b5a93cd1eda0f6ee2.positions[m] );
}
// Render markers
for ( var m in gmap\_mad081fd5e9d9004b5a93cd1eda0f6ee2.positions ) {
gmap\_mad081fd5e9d9004b5a93cd1eda0f6ee2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mad081fd5e9d9004b5a93cd1eda0f6ee2.map,
position : gmap\_mad081fd5e9d9004b5a93cd1eda0f6ee2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mad081fd5e9d9004b5a93cd1eda0f6ee2.map.setCenter( gmap\_mad081fd5e9d9004b5a93cd1eda0f6ee2.positions[782] );
});