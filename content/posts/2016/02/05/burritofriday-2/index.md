---
title: ''
date: '2016-02-05T12:31:14+00:00'
format: image
service: instagram
tags:
- burritofriday
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/02/12547378_874859215967665_406921844_n.jpg?fit=640%2C640
---

[![#burritofriday](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/02/12547378_874859215967665_406921844_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/02/05/burritofriday-2/) 

#burritofriday





* #[burritofriday](http://dentedreality.com.au/tags/burritofriday/)

Posted on [Instagram](https://www.instagram.com/p/BBaplISCmEF/) [12:31 pm, February 5, 2016](http://dentedreality.com.au/2016/02/05/burritofriday-2/ "12:31 pm") 
jQuery(document).ready(function(){
var gmap\_mdf4290fd433c4a2c91832350ba322e50 = {
positions : {
613 : new google.maps.LatLng( '17.744183365', '-88.024333805' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdf4290fd433c4a2c91832350ba322e50' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdf4290fd433c4a2c91832350ba322e50.positions ) {
gmap\_mdf4290fd433c4a2c91832350ba322e50.bounds.extend( gmap\_mdf4290fd433c4a2c91832350ba322e50.positions[m] );
}
// Render markers
for ( var m in gmap\_mdf4290fd433c4a2c91832350ba322e50.positions ) {
gmap\_mdf4290fd433c4a2c91832350ba322e50.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdf4290fd433c4a2c91832350ba322e50.map,
position : gmap\_mdf4290fd433c4a2c91832350ba322e50.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdf4290fd433c4a2c91832350ba322e50.map.setCenter( gmap\_mdf4290fd433c4a2c91832350ba322e50.positions[613] );
});