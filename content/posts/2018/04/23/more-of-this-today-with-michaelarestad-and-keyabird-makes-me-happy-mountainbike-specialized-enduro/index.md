---
title: ''
date: '2018-04-23T19:57:50-06:00'
format: image
service: instagram
tags:
- enduro
- mountainbike
- specialized
latitude: '39.6943776'
longitude: '-105.169851'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/04/14182204/30590028_186709755287122_3083225441180319744_n.jpg?resize=607%2C607&ssl=1
---

[![More of this today with @michaelarestad and @keyabird. Makes me happy. #mountainbike #specialized #enduro](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/04/14182204/30590028_186709755287122_3083225441180319744_n.jpg?resize=607%2C607&ssl=1)](https://dentedreality.com.au/2018/04/23/more-of-this-today-with-michaelarestad-and-keyabird-makes-me-happy-mountainbike-specialized-enduro/) 

[![More of this today with @michaelarestad and @keyabird. Makes me happy. #mountainbike #specialized #enduro](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2018/04/14182204/30590028_186709755287122_3083225441180319744_n.jpg?resize=607%2C607&ssl=1)](https://www.instagram.com/p/Bh74HySFBXG/)

More of this today with @michaelarestad and @keyabird. Makes me happy. #mountainbike #specialized #enduro

39.6943776-105.169851




* #[enduro](https://dentedreality.com.au/tags/enduro/)
* #[mountainbike](https://dentedreality.com.au/tags/mountainbike/)
* #[specialized](https://dentedreality.com.au/tags/specialized/)

Posted on [Instagram](https://www.instagram.com/p/Bh74HySFBXG/) [7:57 pm, April 23, 2018](https://dentedreality.com.au/2018/04/23/more-of-this-today-with-michaelarestad-and-keyabird-makes-me-happy-mountainbike-specialized-enduro/ "7:57 pm") 
jQuery(document).ready(function(){
var gmap\_m79aef3640f845ac778313d1f4b932f0b = {
positions : {
894 : new google.maps.LatLng( '39.694377626329', '-105.16985099772' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m79aef3640f845ac778313d1f4b932f0b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m79aef3640f845ac778313d1f4b932f0b.positions ) {
gmap\_m79aef3640f845ac778313d1f4b932f0b.bounds.extend( gmap\_m79aef3640f845ac778313d1f4b932f0b.positions[m] );
}
// Render markers
for ( var m in gmap\_m79aef3640f845ac778313d1f4b932f0b.positions ) {
gmap\_m79aef3640f845ac778313d1f4b932f0b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m79aef3640f845ac778313d1f4b932f0b.map,
position : gmap\_m79aef3640f845ac778313d1f4b932f0b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m79aef3640f845ac778313d1f4b932f0b.map.setCenter( gmap\_m79aef3640f845ac778313d1f4b932f0b.positions[894] );
});