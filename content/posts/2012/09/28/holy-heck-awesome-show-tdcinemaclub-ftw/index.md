---
title: ''
date: '2012-09-28T21:45:48+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/64d0ef8e09d711e2984822000a1faf28_7.jpg?resize=607%2C607
---

[![Holy heck. Awesome show. @tdcinemaclub FTW.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/64d0ef8e09d711e2984822000a1faf28_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/09/28/holy-heck-awesome-show-tdcinemaclub-ftw/) 

Holy heck. Awesome show. @tdcinemaclub FTW.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/QJCqxFimN3/) [9:45 pm, September 28, 2012](http://dentedreality.com.au/2012/09/28/holy-heck-awesome-show-tdcinemaclub-ftw/ "9:45 pm") 
jQuery(document).ready(function(){
var gmap\_m7160795564cae4258b037c25655ac2d4 = {
positions : {
935 : new google.maps.LatLng( '40.772435241', '-73.970184125' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7160795564cae4258b037c25655ac2d4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7160795564cae4258b037c25655ac2d4.positions ) {
gmap\_m7160795564cae4258b037c25655ac2d4.bounds.extend( gmap\_m7160795564cae4258b037c25655ac2d4.positions[m] );
}
// Render markers
for ( var m in gmap\_m7160795564cae4258b037c25655ac2d4.positions ) {
gmap\_m7160795564cae4258b037c25655ac2d4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7160795564cae4258b037c25655ac2d4.map,
position : gmap\_m7160795564cae4258b037c25655ac2d4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7160795564cae4258b037c25655ac2d4.map.setCenter( gmap\_m7160795564cae4258b037c25655ac2d4.positions[935] );
});