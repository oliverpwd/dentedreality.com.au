---
title: Costa Rica, 2013
date: '2013-07-14T06:41:02+00:00'
format: image
service: flickr
tags:
- costarica
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440183810_481e0fb853_o.jpg?resize=607%2C455
---

[![Costa Rica, 2013](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440183810_481e0fb853_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/07/14/costa-rica-2013-11/) 
# [Costa Rica, 2013](http://dentedreality.com.au/2013/07/14/costa-rica-2013-11/)





* #[costarica](http://dentedreality.com.au/tags/costarica/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9440183810/) [6:41 am, July 14, 2013](http://dentedreality.com.au/2013/07/14/costa-rica-2013-11/ "6:41 am") 
jQuery(document).ready(function(){
var gmap\_m3c2fe1898982ff323861997b6629734a = {
positions : {
971 : new google.maps.LatLng( '9.881733', '-85.527995' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3c2fe1898982ff323861997b6629734a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3c2fe1898982ff323861997b6629734a.positions ) {
gmap\_m3c2fe1898982ff323861997b6629734a.bounds.extend( gmap\_m3c2fe1898982ff323861997b6629734a.positions[m] );
}
// Render markers
for ( var m in gmap\_m3c2fe1898982ff323861997b6629734a.positions ) {
gmap\_m3c2fe1898982ff323861997b6629734a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3c2fe1898982ff323861997b6629734a.map,
position : gmap\_m3c2fe1898982ff323861997b6629734a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3c2fe1898982ff323861997b6629734a.map.setCenter( gmap\_m3c2fe1898982ff323861997b6629734a.positions[971] );
});