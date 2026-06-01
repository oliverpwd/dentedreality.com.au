---
title: ''
date: '2019-12-01T18:35:56-07:00'
format: image
service: instagram
latitude: '39.7391'
longitude: '-104.9836'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/12/01192506/78973601_540718043149377_3370271052354077683_n.jpg
---

[![Denver winter skyline.](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/12/01192506/78973601_540718043149377_3370271052354077683_n.jpg)](https://dentedreality.com.au/2019/12/01/denver-winter-skyline/) 

![Denver winter skyline.](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/12/01192506/78973601_540718043149377_3370271052354077683_n.jpg)

[![Denver winter skyline.](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/78973601_540718043149377_3370271052354077683_n.jpg?_nc_ht=scontent.cdninstagram.com&oh=ad0993b06a884f0ae0fcb47a6cb16bb7&oe=5E671E4C)![Denver winter skyline.](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/78973601_540718043149377_3370271052354077683_n.jpg?_nc_ht=scontent.cdninstagram.com&oh=ad0993b06a884f0ae0fcb47a6cb16bb7&oe=5E671E4C)](https://www.instagram.com/p/B5jUPALJim6/)

Denver winter skyline.

39.7391-104.9836




Posted on [Instagram](https://www.instagram.com/p/B5jUPALJim6/) [6:35 pm, December 1, 2019](https://dentedreality.com.au/2019/12/01/denver-winter-skyline/ "6:35 pm") 
jQuery(document).ready(function(){
var gmap\_mcf5bc8ecf7f83b9095857cbd0aefb491 = {
positions : {
428 : new google.maps.LatLng( '39.7391', '-104.9836' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mcf5bc8ecf7f83b9095857cbd0aefb491' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mcf5bc8ecf7f83b9095857cbd0aefb491.positions ) {
gmap\_mcf5bc8ecf7f83b9095857cbd0aefb491.bounds.extend( gmap\_mcf5bc8ecf7f83b9095857cbd0aefb491.positions[m] );
}
// Render markers
for ( var m in gmap\_mcf5bc8ecf7f83b9095857cbd0aefb491.positions ) {
gmap\_mcf5bc8ecf7f83b9095857cbd0aefb491.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mcf5bc8ecf7f83b9095857cbd0aefb491.map,
position : gmap\_mcf5bc8ecf7f83b9095857cbd0aefb491.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mcf5bc8ecf7f83b9095857cbd0aefb491.map.setCenter( gmap\_mcf5bc8ecf7f83b9095857cbd0aefb491.positions[428] );
});