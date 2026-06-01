---
title: ''
date: '2019-03-21T15:57:16-06:00'
format: image
service: instagram
latitude: '40.01654'
longitude: '-105.28198'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/03/21162502/53813370_2471963382814023_1880830831062451150_n.jpg?fit=640%2C640&ssl=1
---

[![Just hanging out here with @howard.schultz during @techstars. Hearing about the background of @starbucks and what makes a successful company.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/03/21162502/53813370_2471963382814023_1880830831062451150_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/03/21/just-hanging-out-here-with-howard-schultz-during-techstars-hearing-about-the-background-of-starbucks-and-what-makes-a-successful-company/) 

[![Just hanging out here with @howard.schultz during @techstars. Hearing about the background of @starbucks and what makes a successful company.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/03/21162502/53813370_2471963382814023_1880830831062451150_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BvSUgR-Hs1C/)

Just hanging out here with @howard.schultz during @techstars. Hearing about the background of @starbucks and what makes a successful company.

40.01654-105.28198




Posted on [Instagram](https://www.instagram.com/p/BvSUgR-Hs1C/) [3:57 pm, March 21, 2019](https://dentedreality.com.au/2019/03/21/just-hanging-out-here-with-howard-schultz-during-techstars-hearing-about-the-background-of-starbucks-and-what-makes-a-successful-company/ "3:57 pm") 
jQuery(document).ready(function(){
var gmap\_m3686ba0e550423dea5cc43aaed4db178 = {
positions : {
780 : new google.maps.LatLng( '40.01654', '-105.28198' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3686ba0e550423dea5cc43aaed4db178' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3686ba0e550423dea5cc43aaed4db178.positions ) {
gmap\_m3686ba0e550423dea5cc43aaed4db178.bounds.extend( gmap\_m3686ba0e550423dea5cc43aaed4db178.positions[m] );
}
// Render markers
for ( var m in gmap\_m3686ba0e550423dea5cc43aaed4db178.positions ) {
gmap\_m3686ba0e550423dea5cc43aaed4db178.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3686ba0e550423dea5cc43aaed4db178.map,
position : gmap\_m3686ba0e550423dea5cc43aaed4db178.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3686ba0e550423dea5cc43aaed4db178.map.setCenter( gmap\_m3686ba0e550423dea5cc43aaed4db178.positions[780] );
});