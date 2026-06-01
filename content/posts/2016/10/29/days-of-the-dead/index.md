---
title: ''
date: '2016-10-29T14:06:43-06:00'
format: image
service: instagram
latitude: '39.7321442'
longitude: '-104.9607721'
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/10/14624218_102871190190858_63316592561225728_n.jpg?fit=640%2C640
---

[![Days of the Dead](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/10/14624218_102871190190858_63316592561225728_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/10/29/days-of-the-dead/) 

[![Days of the Dead](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/10/14624218_102871190190858_63316592561225728_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BMKN4rXjIzW/)

Days of the Dead

39.7321442-104.9607721




Posted on [Instagram](https://www.instagram.com/p/BMKN4rXjIzW/) [2:06 pm, October 29, 2016](https://dentedreality.com.au/2016/10/29/days-of-the-dead/ "2:06 pm") 
jQuery(document).ready(function(){
var gmap\_m9f773bb7151a62929943d7bb3c98aa3d = {
positions : {
510 : new google.maps.LatLng( '39.73214416473', '-104.9607721189' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9f773bb7151a62929943d7bb3c98aa3d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9f773bb7151a62929943d7bb3c98aa3d.positions ) {
gmap\_m9f773bb7151a62929943d7bb3c98aa3d.bounds.extend( gmap\_m9f773bb7151a62929943d7bb3c98aa3d.positions[m] );
}
// Render markers
for ( var m in gmap\_m9f773bb7151a62929943d7bb3c98aa3d.positions ) {
gmap\_m9f773bb7151a62929943d7bb3c98aa3d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9f773bb7151a62929943d7bb3c98aa3d.map,
position : gmap\_m9f773bb7151a62929943d7bb3c98aa3d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9f773bb7151a62929943d7bb3c98aa3d.map.setCenter( gmap\_m9f773bb7151a62929943d7bb3c98aa3d.positions[510] );
});