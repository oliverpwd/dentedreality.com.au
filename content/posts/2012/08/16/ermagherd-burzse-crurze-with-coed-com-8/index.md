---
title: Ermagherd Burzse Crurze with COED.com
date: '2012-08-16T16:00:05+00:00'
format: image
service: flickr
tags:
- boozecruise
- cityscape
- coed
- EastRiver
- newyork
- skyline
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8244766547_4f54069d59_o.jpg?resize=607%2C813
---

[![Ermagherd Burzse Crurze with COED.com](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8244766547_4f54069d59_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-8/) 
# [Ermagherd Burzse Crurze with COED.com](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-8/)





* #[boozecruise](http://dentedreality.com.au/tags/boozecruise/)
* #[cityscape](http://dentedreality.com.au/tags/cityscape/)
* #[coed](http://dentedreality.com.au/tags/coed/)
* #[EastRiver](http://dentedreality.com.au/tags/eastriver/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[skyline](http://dentedreality.com.au/tags/skyline/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8244766547/) [4:00 pm, August 16, 2012](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-8/ "4:00 pm") 
jQuery(document).ready(function(){
var gmap\_mb8a68e19627119ac2c779ffee57b8826 = {
positions : {
710 : new google.maps.LatLng( '40.714166', '-73.9715' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb8a68e19627119ac2c779ffee57b8826' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb8a68e19627119ac2c779ffee57b8826.positions ) {
gmap\_mb8a68e19627119ac2c779ffee57b8826.bounds.extend( gmap\_mb8a68e19627119ac2c779ffee57b8826.positions[m] );
}
// Render markers
for ( var m in gmap\_mb8a68e19627119ac2c779ffee57b8826.positions ) {
gmap\_mb8a68e19627119ac2c779ffee57b8826.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb8a68e19627119ac2c779ffee57b8826.map,
position : gmap\_mb8a68e19627119ac2c779ffee57b8826.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb8a68e19627119ac2c779ffee57b8826.map.setCenter( gmap\_mb8a68e19627119ac2c779ffee57b8826.positions[710] );
});