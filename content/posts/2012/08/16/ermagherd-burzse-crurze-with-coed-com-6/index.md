---
title: Ermagherd Burzse Crurze with COED.com
date: '2012-08-16T17:03:08+00:00'
format: image
service: flickr
tags:
- boozecruise
- coed
- EastRiver
- newyork
- statueofliberty
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8245834870_1b9dfcb6e9_o.jpg?resize=607%2C813
---

[![Ermagherd Burzse Crurze with COED.com](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/08/8245834870_1b9dfcb6e9_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-6/) 
# [Ermagherd Burzse Crurze with COED.com](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-6/)





* #[boozecruise](http://dentedreality.com.au/tags/boozecruise/)
* #[coed](http://dentedreality.com.au/tags/coed/)
* #[EastRiver](http://dentedreality.com.au/tags/eastriver/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[statueofliberty](http://dentedreality.com.au/tags/statueofliberty/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245834870/) [5:03 pm, August 16, 2012](http://dentedreality.com.au/2012/08/16/ermagherd-burzse-crurze-with-coed-com-6/ "5:03 pm") 
jQuery(document).ready(function(){
var gmap\_ma0b49de04cd88055ead04907b03bbc19 = {
positions : {
237 : new google.maps.LatLng( '40.687999', '-74.042334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma0b49de04cd88055ead04907b03bbc19' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma0b49de04cd88055ead04907b03bbc19.positions ) {
gmap\_ma0b49de04cd88055ead04907b03bbc19.bounds.extend( gmap\_ma0b49de04cd88055ead04907b03bbc19.positions[m] );
}
// Render markers
for ( var m in gmap\_ma0b49de04cd88055ead04907b03bbc19.positions ) {
gmap\_ma0b49de04cd88055ead04907b03bbc19.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma0b49de04cd88055ead04907b03bbc19.map,
position : gmap\_ma0b49de04cd88055ead04907b03bbc19.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma0b49de04cd88055ead04907b03bbc19.map.setCenter( gmap\_ma0b49de04cd88055ead04907b03bbc19.positions[237] );
});