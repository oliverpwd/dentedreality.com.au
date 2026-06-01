---
title: ''
date: '2019-08-08T17:35:34-06:00'
format: image
service: instagram
latitude: '38.4669609'
longitude: '-107.1662674'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/08192459/69183486_132424301323181_1788533836587559832_n.jpg?fit=640%2C640&ssl=1
---

[![Epic views from our campsite this week.](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/08192459/69183486_132424301323181_1788533836587559832_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/08/08/epic-views-from-our-campsite-this-week/) 

[![Epic views from our campsite this week.](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/08192459/69183486_132424301323181_1788533836587559832_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/B06_CrcpweG/)

Epic views from our campsite this week.

38.4669609-107.1662674




Posted on [Instagram](https://www.instagram.com/p/B06_CrcpweG/) [5:35 pm, August 8, 2019](https://dentedreality.com.au/2019/08/08/epic-views-from-our-campsite-this-week/ "5:35 pm") 
jQuery(document).ready(function(){
var gmap\_mf364e2bf9633c0ff560378bf051dd465 = {
positions : {
534 : new google.maps.LatLng( '38.4669609', '-107.1662674' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf364e2bf9633c0ff560378bf051dd465' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf364e2bf9633c0ff560378bf051dd465.positions ) {
gmap\_mf364e2bf9633c0ff560378bf051dd465.bounds.extend( gmap\_mf364e2bf9633c0ff560378bf051dd465.positions[m] );
}
// Render markers
for ( var m in gmap\_mf364e2bf9633c0ff560378bf051dd465.positions ) {
gmap\_mf364e2bf9633c0ff560378bf051dd465.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf364e2bf9633c0ff560378bf051dd465.map,
position : gmap\_mf364e2bf9633c0ff560378bf051dd465.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf364e2bf9633c0ff560378bf051dd465.map.setCenter( gmap\_mf364e2bf9633c0ff560378bf051dd465.positions[534] );
});