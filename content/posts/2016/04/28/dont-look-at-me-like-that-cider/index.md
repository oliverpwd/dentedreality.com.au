---
title: ''
date: '2016-04-28T14:31:43+00:00'
format: image
service: instagram
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/04/13102383_1602057873443965_335662820_n.jpg?fit=640%2C640
---

[![Don't look at me like that, cider.](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/04/13102383_1602057873443965_335662820_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/04/28/dont-look-at-me-like-that-cider/) 

Don’t look at me like that, cider.





Posted on [Instagram](https://www.instagram.com/p/BEweexXCmDG/) [2:31 pm, April 28, 2016](http://dentedreality.com.au/2016/04/28/dont-look-at-me-like-that-cider/ "2:31 pm") 
jQuery(document).ready(function(){
var gmap\_mcc4a3fd6df4e5552dd50b74d04691dd2 = {
positions : {
854 : new google.maps.LatLng( '39.76281', '-104.98398' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mcc4a3fd6df4e5552dd50b74d04691dd2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mcc4a3fd6df4e5552dd50b74d04691dd2.positions ) {
gmap\_mcc4a3fd6df4e5552dd50b74d04691dd2.bounds.extend( gmap\_mcc4a3fd6df4e5552dd50b74d04691dd2.positions[m] );
}
// Render markers
for ( var m in gmap\_mcc4a3fd6df4e5552dd50b74d04691dd2.positions ) {
gmap\_mcc4a3fd6df4e5552dd50b74d04691dd2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mcc4a3fd6df4e5552dd50b74d04691dd2.map,
position : gmap\_mcc4a3fd6df4e5552dd50b74d04691dd2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mcc4a3fd6df4e5552dd50b74d04691dd2.map.setCenter( gmap\_mcc4a3fd6df4e5552dd50b74d04691dd2.positions[854] );
});