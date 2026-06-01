---
title: ''
date: '2019-08-08T17:37:17-06:00'
format: image
service: instagram
latitude: '38.4547'
longitude: '-107.327'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/08192457/67283265_392100468383495_1092845796509654898_n.jpg?fit=640%2C640&ssl=1
---

[![More crazy views a 5 minute stroll from our campsite.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/08192457/67283265_392100468383495_1092845796509654898_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/08/08/more-crazy-views-a-5-minute-stroll-from-our-campsite/) 

[![More crazy views a 5 minute stroll from our campsite.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/08192457/67283265_392100468383495_1092845796509654898_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/B06_PXjpwSd/)

More crazy views a 5 minute stroll from our campsite.

38.4547-107.327




Posted on [Instagram](https://www.instagram.com/p/B06_PXjpwSd/) [5:37 pm, August 8, 2019](https://dentedreality.com.au/2019/08/08/more-crazy-views-a-5-minute-stroll-from-our-campsite/ "5:37 pm") 
jQuery(document).ready(function(){
var gmap\_m213219871378940aceede8a0daf0bc29 = {
positions : {
746 : new google.maps.LatLng( '38.4547', '-107.327' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m213219871378940aceede8a0daf0bc29' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m213219871378940aceede8a0daf0bc29.positions ) {
gmap\_m213219871378940aceede8a0daf0bc29.bounds.extend( gmap\_m213219871378940aceede8a0daf0bc29.positions[m] );
}
// Render markers
for ( var m in gmap\_m213219871378940aceede8a0daf0bc29.positions ) {
gmap\_m213219871378940aceede8a0daf0bc29.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m213219871378940aceede8a0daf0bc29.map,
position : gmap\_m213219871378940aceede8a0daf0bc29.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m213219871378940aceede8a0daf0bc29.map.setCenter( gmap\_m213219871378940aceede8a0daf0bc29.positions[746] );
});