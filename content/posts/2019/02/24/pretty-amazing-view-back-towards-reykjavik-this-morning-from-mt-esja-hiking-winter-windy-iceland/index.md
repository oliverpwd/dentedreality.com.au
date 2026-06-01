---
title: ''
date: '2019-02-24T18:50:21-07:00'
format: image
service: instagram
tags:
- hiking
- iceland
- windy
- winter
latitude: '64.2093275'
longitude: '-21.7120314'
image: https://dentedreality.com.au/wp-content/uploads/2019/02/52478674_168813050772762_5394212964437345959_n.jpg
---

[![Pretty amazing view back towards Reykjavík this morning, from Mt. Esja. #hiking #winter #windy #iceland](https://dentedreality.com.au/wp-content/uploads/2019/02/52478674_168813050772762_5394212964437345959_n.jpg)](https://dentedreality.com.au/2019/02/24/pretty-amazing-view-back-towards-reykjavik-this-morning-from-mt-esja-hiking-winter-windy-iceland/) 

[![Pretty amazing view back towards Reykjavík this morning, from Mt. Esja. #hiking #winter #windy #iceland](https://dentedreality.com.au/wp-content/uploads/2019/02/52478674_168813050772762_5394212964437345959_n.jpg)](https://www.instagram.com/p/BuSXThYHxtl/)

Pretty amazing view back towards Reykjavík this morning, from Mt. Esja. #hiking #winter #windy #iceland

64.2093275-21.7120314




* #[hiking](https://dentedreality.com.au/tags/hiking/)
* #[iceland](https://dentedreality.com.au/tags/iceland/)
* #[windy](https://dentedreality.com.au/tags/windy/)
* #[winter](https://dentedreality.com.au/tags/winter/)

Posted on [Instagram](https://www.instagram.com/p/BuSXThYHxtl/) [6:50 pm, February 24, 2019](https://dentedreality.com.au/2019/02/24/pretty-amazing-view-back-towards-reykjavik-this-morning-from-mt-esja-hiking-winter-windy-iceland/ "6:50 pm") 
jQuery(document).ready(function(){
var gmap\_m8a3c96210e5c13b869415aaee2511976 = {
positions : {
468 : new google.maps.LatLng( '64.2093275', '-21.7120314' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8a3c96210e5c13b869415aaee2511976' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8a3c96210e5c13b869415aaee2511976.positions ) {
gmap\_m8a3c96210e5c13b869415aaee2511976.bounds.extend( gmap\_m8a3c96210e5c13b869415aaee2511976.positions[m] );
}
// Render markers
for ( var m in gmap\_m8a3c96210e5c13b869415aaee2511976.positions ) {
gmap\_m8a3c96210e5c13b869415aaee2511976.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8a3c96210e5c13b869415aaee2511976.map,
position : gmap\_m8a3c96210e5c13b869415aaee2511976.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8a3c96210e5c13b869415aaee2511976.map.setCenter( gmap\_m8a3c96210e5c13b869415aaee2511976.positions[468] );
});