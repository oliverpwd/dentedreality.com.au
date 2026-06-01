---
title: ''
date: '2016-08-25T09:02:03-06:00'
format: image
service: instagram
tags:
- fjallclassic16
- fjallclassic2016
- fjallravenclassicusa
latitude: '40.5113831'
longitude: '-106.0084839'
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/14033468_1063313203721921_1505140805_n.jpg?fit=640%2C640
---

[![Gorgeous Aspen grove near the end of the #fjallclassic2016. Such a great trip. Thanks @fjallravenusa! #fjallclassic16](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/14033468_1063313203721921_1505140805_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/08/25/gorgeous-aspen-grove-near-the-end-of-the-fjallclassic2016-such-a-great-trip-thanks-fjallravenusa-fjallclassic16/) 

[![Gorgeous Aspen grove near the end of the #fjallclassic2016. Such a great trip. Thanks @fjallravenusa! #fjallclassic16](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/14033468_1063313203721921_1505140805_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BJiTWV0gnYE/)

Gorgeous Aspen grove near the end of the #fjallclassic2016. Such a great trip. Thanks @fjallravenusa! #fjallclassic16

40.5113831-106.0084839




* #[fjallclassic16](https://dentedreality.com.au/tags/fjallclassic16/)
* #[fjallclassic2016](https://dentedreality.com.au/tags/fjallclassic2016/)
* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BJiTWV0gnYE/) [9:02 am, August 25, 2016](https://dentedreality.com.au/2016/08/25/gorgeous-aspen-grove-near-the-end-of-the-fjallclassic2016-such-a-great-trip-thanks-fjallravenusa-fjallclassic16/ "9:02 am") 
jQuery(document).ready(function(){
var gmap\_m5bd1473a82ceebbe928f0ff48ea62ffe = {
positions : {
478 : new google.maps.LatLng( '40.5113831', '-106.0084839' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5bd1473a82ceebbe928f0ff48ea62ffe' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5bd1473a82ceebbe928f0ff48ea62ffe.positions ) {
gmap\_m5bd1473a82ceebbe928f0ff48ea62ffe.bounds.extend( gmap\_m5bd1473a82ceebbe928f0ff48ea62ffe.positions[m] );
}
// Render markers
for ( var m in gmap\_m5bd1473a82ceebbe928f0ff48ea62ffe.positions ) {
gmap\_m5bd1473a82ceebbe928f0ff48ea62ffe.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5bd1473a82ceebbe928f0ff48ea62ffe.map,
position : gmap\_m5bd1473a82ceebbe928f0ff48ea62ffe.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5bd1473a82ceebbe928f0ff48ea62ffe.map.setCenter( gmap\_m5bd1473a82ceebbe928f0ff48ea62ffe.positions[478] );
});