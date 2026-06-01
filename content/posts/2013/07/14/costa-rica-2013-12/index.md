---
title: Costa Rica, 2013
date: '2013-07-14T06:40:54+00:00'
format: image
service: flickr
tags:
- costarica
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440183260_82f876da72_o.jpg?resize=607%2C455
---

[![Costa Rica, 2013](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440183260_82f876da72_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/07/14/costa-rica-2013-12/) 
# [Costa Rica, 2013](http://dentedreality.com.au/2013/07/14/costa-rica-2013-12/)





* #[costarica](http://dentedreality.com.au/tags/costarica/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9440183260/) [6:40 am, July 14, 2013](http://dentedreality.com.au/2013/07/14/costa-rica-2013-12/ "6:40 am") 
jQuery(document).ready(function(){
var gmap\_mced93eb8e053f9d7b6493beba6e27f0b = {
positions : {
746 : new google.maps.LatLng( '9.88178', '-85.527959' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mced93eb8e053f9d7b6493beba6e27f0b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mced93eb8e053f9d7b6493beba6e27f0b.positions ) {
gmap\_mced93eb8e053f9d7b6493beba6e27f0b.bounds.extend( gmap\_mced93eb8e053f9d7b6493beba6e27f0b.positions[m] );
}
// Render markers
for ( var m in gmap\_mced93eb8e053f9d7b6493beba6e27f0b.positions ) {
gmap\_mced93eb8e053f9d7b6493beba6e27f0b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mced93eb8e053f9d7b6493beba6e27f0b.map,
position : gmap\_mced93eb8e053f9d7b6493beba6e27f0b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mced93eb8e053f9d7b6493beba6e27f0b.map.setCenter( gmap\_mced93eb8e053f9d7b6493beba6e27f0b.positions[746] );
});