---
title: ''
date: '2018-05-13T21:48:06-06:00'
format: image
service: instagram
tags:
- fjallravenclassic
latitude: '39.6678136'
longitude: '-105.2578443'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2018/05/14182157/31489548_623167098019116_6884978213534040064_n.jpg
---

[![Another 10 mile training hike for #fjallravenclassic. This time with @akires](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2018/05/14182157/31489548_623167098019116_6884978213534040064_n.jpg)](https://dentedreality.com.au/2018/05/13/another-10-mile-training-hike-for-fjallravenclassic-this-time-with-akires/) 

[![Another 10 mile training hike for #fjallravenclassic. This time with @akires](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2018/05/14182157/31489548_623167098019116_6884978213534040064_n.jpg)](https://www.instagram.com/p/Bivko4sFZiT/)

Another 10 mile training hike for #fjallravenclassic. This time with @akires

39.6678136-105.2578443




* #[fjallravenclassic](https://dentedreality.com.au/tags/fjallravenclassic/)

Posted on [Instagram](https://www.instagram.com/p/Bivko4sFZiT/) [9:48 pm, May 13, 2018](https://dentedreality.com.au/2018/05/13/another-10-mile-training-hike-for-fjallravenclassic-this-time-with-akires/ "9:48 pm") 
jQuery(document).ready(function(){
var gmap\_m78620e0e5aa879d140d1cdeb915dbf5e = {
positions : {
99 : new google.maps.LatLng( '39.667813594234', '-105.25784430977' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m78620e0e5aa879d140d1cdeb915dbf5e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m78620e0e5aa879d140d1cdeb915dbf5e.positions ) {
gmap\_m78620e0e5aa879d140d1cdeb915dbf5e.bounds.extend( gmap\_m78620e0e5aa879d140d1cdeb915dbf5e.positions[m] );
}
// Render markers
for ( var m in gmap\_m78620e0e5aa879d140d1cdeb915dbf5e.positions ) {
gmap\_m78620e0e5aa879d140d1cdeb915dbf5e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m78620e0e5aa879d140d1cdeb915dbf5e.map,
position : gmap\_m78620e0e5aa879d140d1cdeb915dbf5e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m78620e0e5aa879d140d1cdeb915dbf5e.map.setCenter( gmap\_m78620e0e5aa879d140d1cdeb915dbf5e.positions[99] );
});