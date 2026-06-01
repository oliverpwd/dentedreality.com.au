---
title: ''
date: '2017-12-16T09:27:01+00:00'
format: image
service: instagram
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/12/25007116_354421928301773_7629202127880978432_n.jpg?fit=640%2C640&ssl=1
---

[![Best elements in the table!](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/12/25007116_354421928301773_7629202127880978432_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/12/16/best-elements-in-the-table/) 

[![Best elements in the table!](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/12/25007116_354421928301773_7629202127880978432_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BcxRC5DB5KU/)

Best elements in the table!





Posted on [Instagram](https://www.instagram.com/p/BcxRC5DB5KU/) [9:27 am, December 16, 2017](https://dentedreality.com.au/2017/12/16/best-elements-in-the-table/ "9:27 am") 
jQuery(document).ready(function(){
var gmap\_m917b5c4c719ab68997513c4b6aaf0670 = {
positions : {
502 : new google.maps.LatLng( '39.760328348259', '-105.02221113277' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m917b5c4c719ab68997513c4b6aaf0670' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m917b5c4c719ab68997513c4b6aaf0670.positions ) {
gmap\_m917b5c4c719ab68997513c4b6aaf0670.bounds.extend( gmap\_m917b5c4c719ab68997513c4b6aaf0670.positions[m] );
}
// Render markers
for ( var m in gmap\_m917b5c4c719ab68997513c4b6aaf0670.positions ) {
gmap\_m917b5c4c719ab68997513c4b6aaf0670.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m917b5c4c719ab68997513c4b6aaf0670.map,
position : gmap\_m917b5c4c719ab68997513c4b6aaf0670.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m917b5c4c719ab68997513c4b6aaf0670.map.setCenter( gmap\_m917b5c4c719ab68997513c4b6aaf0670.positions[502] );
});