---
title: ''
date: '2014-11-03T17:11:06+00:00'
format: image
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/928059_555047937959823_1738594222_n.jpg?resize=640%2C640
---

[![Sunday's fishing hole.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/928059_555047937959823_1738594222_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/11/03/sundays-fishing-hole/) 

Sunday’s fishing hole.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/u9QvUQimLK/) [5:11 pm, November 3, 2014](http://dentedreality.com.au/2014/11/03/sundays-fishing-hole/ "5:11 pm") 
jQuery(document).ready(function(){
var gmap\_mde0058e5cbbb72385b2d1ae48d936988 = {
positions : {
804 : new google.maps.LatLng( '39.491365801', '-105.093584331' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mde0058e5cbbb72385b2d1ae48d936988' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mde0058e5cbbb72385b2d1ae48d936988.positions ) {
gmap\_mde0058e5cbbb72385b2d1ae48d936988.bounds.extend( gmap\_mde0058e5cbbb72385b2d1ae48d936988.positions[m] );
}
// Render markers
for ( var m in gmap\_mde0058e5cbbb72385b2d1ae48d936988.positions ) {
gmap\_mde0058e5cbbb72385b2d1ae48d936988.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mde0058e5cbbb72385b2d1ae48d936988.map,
position : gmap\_mde0058e5cbbb72385b2d1ae48d936988.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mde0058e5cbbb72385b2d1ae48d936988.map.setCenter( gmap\_mde0058e5cbbb72385b2d1ae48d936988.positions[804] );
});