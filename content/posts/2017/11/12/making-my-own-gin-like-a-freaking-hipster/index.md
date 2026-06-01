---
title: ''
date: '2017-11-12T15:10:45+00:00'
format: image
service: instagram
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/11/23594289_126658251336001_730116531622510592_n.jpg?fit=640%2C640&ssl=1
---

[![Making my own gin, like a freaking hipster.](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/11/23594289_126658251336001_730116531622510592_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/11/12/making-my-own-gin-like-a-freaking-hipster/) 

[![Making my own gin, like a freaking hipster.](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2017/11/23594289_126658251336001_730116531622510592_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BbaVWwUBpIn/)

Making my own gin, like a freaking hipster.





Posted on [Instagram](https://www.instagram.com/p/BbaVWwUBpIn/) [3:10 pm, November 12, 2017](https://dentedreality.com.au/2017/11/12/making-my-own-gin-like-a-freaking-hipster/ "3:10 pm") 
jQuery(document).ready(function(){
var gmap\_mc4e98cbb2210acb8f3379be705b51806 = {
positions : {
840 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc4e98cbb2210acb8f3379be705b51806' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc4e98cbb2210acb8f3379be705b51806.positions ) {
gmap\_mc4e98cbb2210acb8f3379be705b51806.bounds.extend( gmap\_mc4e98cbb2210acb8f3379be705b51806.positions[m] );
}
// Render markers
for ( var m in gmap\_mc4e98cbb2210acb8f3379be705b51806.positions ) {
gmap\_mc4e98cbb2210acb8f3379be705b51806.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc4e98cbb2210acb8f3379be705b51806.map,
position : gmap\_mc4e98cbb2210acb8f3379be705b51806.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc4e98cbb2210acb8f3379be705b51806.map.setCenter( gmap\_mc4e98cbb2210acb8f3379be705b51806.positions[840] );
});