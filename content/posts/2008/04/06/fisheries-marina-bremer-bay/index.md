---
title: Fisheries Marina @ Bremer Bay
date: '2008-04-06T18:04:55-06:00'
format: image
service: flickr
tags:
- australia
- fisheries
- marina
- westernaustraliabremerbay
latitude: '-34.481231'
longitude: '119.373493'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184655/2433442984_44ee6aabf2_o.jpg
---

[![Fisheries Marina @ Bremer Bay](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184655/2433442984_44ee6aabf2_o.jpg)](https://dentedreality.com.au/2008/04/06/fisheries-marina-bremer-bay/) 
# [Fisheries Marina @ Bremer Bay](https://dentedreality.com.au/2008/04/06/fisheries-marina-bremer-bay/)

[![Fisheries Marina @ Bremer Bay](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184655/2433442984_44ee6aabf2_o.jpg)](http://www.flickr.com/photos/borkazoid/2433442984/)

-34.481231119.373493




* #[australia](https://dentedreality.com.au/tags/australia/)
* #[fisheries](https://dentedreality.com.au/tags/fisheries/)
* #[marina](https://dentedreality.com.au/tags/marina/)
* #[westernaustraliabremerbay](https://dentedreality.com.au/tags/westernaustraliabremerbay/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2433442984/) [6:04 pm, April 6, 2008](https://dentedreality.com.au/2008/04/06/fisheries-marina-bremer-bay/ "6:04 pm") 
jQuery(document).ready(function(){
var gmap\_ma45fe32f3a089aab20b7d3a85cb77f2d = {
positions : {
925 : new google.maps.LatLng( '-34.481231', '119.373493' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma45fe32f3a089aab20b7d3a85cb77f2d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma45fe32f3a089aab20b7d3a85cb77f2d.positions ) {
gmap\_ma45fe32f3a089aab20b7d3a85cb77f2d.bounds.extend( gmap\_ma45fe32f3a089aab20b7d3a85cb77f2d.positions[m] );
}
// Render markers
for ( var m in gmap\_ma45fe32f3a089aab20b7d3a85cb77f2d.positions ) {
gmap\_ma45fe32f3a089aab20b7d3a85cb77f2d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma45fe32f3a089aab20b7d3a85cb77f2d.map,
position : gmap\_ma45fe32f3a089aab20b7d3a85cb77f2d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma45fe32f3a089aab20b7d3a85cb77f2d.map.setCenter( gmap\_ma45fe32f3a089aab20b7d3a85cb77f2d.positions[925] );
});