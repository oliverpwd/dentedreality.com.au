---
title: ''
date: '2016-01-07T19:53:29+00:00'
format: image
service: instagram
tags:
- sushi
- winning
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/01/12519266_1693134587575099_689082342_n.jpg?fit=640%2C640
---

[![#winning at #sushi](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/01/12519266_1693134587575099_689082342_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/01/07/winning-at-sushi/) 

#winning at #sushi





* #[sushi](http://dentedreality.com.au/tags/sushi/)
* #[winning](http://dentedreality.com.au/tags/winning/)

Posted on [Instagram](https://www.instagram.com/p/BAQxI8wCmLv/) [7:53 pm, January 7, 2016](http://dentedreality.com.au/2016/01/07/winning-at-sushi/ "7:53 pm") 
jQuery(document).ready(function(){
var gmap\_mc20ad2e19b2f3288d612e8150ecce3f1 = {
positions : {
649 : new google.maps.LatLng( '39.7588997', '-104.9851456' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc20ad2e19b2f3288d612e8150ecce3f1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc20ad2e19b2f3288d612e8150ecce3f1.positions ) {
gmap\_mc20ad2e19b2f3288d612e8150ecce3f1.bounds.extend( gmap\_mc20ad2e19b2f3288d612e8150ecce3f1.positions[m] );
}
// Render markers
for ( var m in gmap\_mc20ad2e19b2f3288d612e8150ecce3f1.positions ) {
gmap\_mc20ad2e19b2f3288d612e8150ecce3f1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc20ad2e19b2f3288d612e8150ecce3f1.map,
position : gmap\_mc20ad2e19b2f3288d612e8150ecce3f1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc20ad2e19b2f3288d612e8150ecce3f1.map.setCenter( gmap\_mc20ad2e19b2f3288d612e8150ecce3f1.positions[649] );
});