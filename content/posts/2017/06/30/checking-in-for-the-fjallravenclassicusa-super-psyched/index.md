---
title: ''
date: '2017-06-30T22:20:58-06:00'
format: image
service: instagram
tags:
- fjallravenclassicusa
latitude: '39.500861'
longitude: '-106.1535167'
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/06/19367694_428991974166997_8888045016430149632_n.jpg?fit=640%2C640&ssl=1
---

[![Checking in for the #fjallravenclassicusa. Super psyched!](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/06/19367694_428991974166997_8888045016430149632_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/06/30/checking-in-for-the-fjallravenclassicusa-super-psyched/) 

[![Checking in for the #fjallravenclassicusa. Super psyched!](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/06/19367694_428991974166997_8888045016430149632_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BV_YaK4Bkfr/)

Checking in for the #fjallravenclassicusa. Super psyched!

39.500861-106.1535167




* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BV_YaK4Bkfr/) [10:20 pm, June 30, 2017](https://dentedreality.com.au/2017/06/30/checking-in-for-the-fjallravenclassicusa-super-psyched/ "10:20 pm") 
jQuery(document).ready(function(){
var gmap\_mb545b78f538082129ae976cf7631cf77 = {
positions : {
974 : new google.maps.LatLng( '39.500861', '-106.1535167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb545b78f538082129ae976cf7631cf77' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb545b78f538082129ae976cf7631cf77.positions ) {
gmap\_mb545b78f538082129ae976cf7631cf77.bounds.extend( gmap\_mb545b78f538082129ae976cf7631cf77.positions[m] );
}
// Render markers
for ( var m in gmap\_mb545b78f538082129ae976cf7631cf77.positions ) {
gmap\_mb545b78f538082129ae976cf7631cf77.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb545b78f538082129ae976cf7631cf77.map,
position : gmap\_mb545b78f538082129ae976cf7631cf77.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb545b78f538082129ae976cf7631cf77.map.setCenter( gmap\_mb545b78f538082129ae976cf7631cf77.positions[974] );
});