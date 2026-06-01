---
title: River Gorge
date: '2008-04-07T15:52:30+00:00'
format: image
service: flickr
tags:
- australia
- gorge
- panorama
- panoramic
- river
- westernaustraliabremerbay
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433448426_18b54c0517_o.jpg?resize=607%2C165
---

[![River Gorge](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433448426_18b54c0517_o.jpg?resize=607%2C165)](http://dentedreality.com.au/2008/04/07/river-gorge/) 
# [River Gorge](http://dentedreality.com.au/2008/04/07/river-gorge/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[gorge](http://dentedreality.com.au/tags/gorge/)
* #[panorama](http://dentedreality.com.au/tags/panorama/)
* #[panoramic](http://dentedreality.com.au/tags/panoramic/)
* #[river](http://dentedreality.com.au/tags/river/)
* #[westernaustraliabremerbay](http://dentedreality.com.au/tags/westernaustraliabremerbay/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2433448426/) [3:52 pm, April 7, 2008](http://dentedreality.com.au/2008/04/07/river-gorge/ "3:52 pm") 
jQuery(document).ready(function(){
var gmap\_ma1543f249ffad38a00cc7f68ed9b8bf5 = {
positions : {
173 : new google.maps.LatLng( '-34.36859', '119.322681' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma1543f249ffad38a00cc7f68ed9b8bf5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma1543f249ffad38a00cc7f68ed9b8bf5.positions ) {
gmap\_ma1543f249ffad38a00cc7f68ed9b8bf5.bounds.extend( gmap\_ma1543f249ffad38a00cc7f68ed9b8bf5.positions[m] );
}
// Render markers
for ( var m in gmap\_ma1543f249ffad38a00cc7f68ed9b8bf5.positions ) {
gmap\_ma1543f249ffad38a00cc7f68ed9b8bf5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma1543f249ffad38a00cc7f68ed9b8bf5.map,
position : gmap\_ma1543f249ffad38a00cc7f68ed9b8bf5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma1543f249ffad38a00cc7f68ed9b8bf5.map.setCenter( gmap\_ma1543f249ffad38a00cc7f68ed9b8bf5.positions[173] );
});