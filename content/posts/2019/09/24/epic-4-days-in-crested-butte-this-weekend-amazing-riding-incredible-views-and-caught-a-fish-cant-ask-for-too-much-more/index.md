---
title: ''
date: '2019-09-24T22:24:19-06:00'
format: image
service: instagram
latitude: '38.8697222'
longitude: '-106.9877778'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/09/24222507/71335514_595421947860064_82036701134943565_n.jpg
---

[![Epic 4 days in Crested Butte this weekend. Amazing riding, incredible views, and caught a fish. Can't ask for too much more.](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/09/24222507/71335514_595421947860064_82036701134943565_n.jpg)](https://dentedreality.com.au/2019/09/24/epic-4-days-in-crested-butte-this-weekend-amazing-riding-incredible-views-and-caught-a-fish-cant-ask-for-too-much-more/) 

[![Epic 4 days in Crested Butte this weekend. Amazing riding, incredible views, and caught a fish. Can't ask for too much more.](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/09/24222507/71335514_595421947860064_82036701134943565_n.jpg)](https://www.instagram.com/p/B20hcw4pySp/)

Epic 4 days in Crested Butte this weekend. Amazing riding, incredible views, and caught a fish. Can’t ask for too much more.

38.8697222-106.9877778




Posted on [Instagram](https://www.instagram.com/p/B20hcw4pySp/) [10:24 pm, September 24, 2019](https://dentedreality.com.au/2019/09/24/epic-4-days-in-crested-butte-this-weekend-amazing-riding-incredible-views-and-caught-a-fish-cant-ask-for-too-much-more/ "10:24 pm") 
jQuery(document).ready(function(){
var gmap\_m0c5bd0a7d321390ac744e25e805d24b4 = {
positions : {
682 : new google.maps.LatLng( '38.8697222', '-106.9877778' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0c5bd0a7d321390ac744e25e805d24b4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0c5bd0a7d321390ac744e25e805d24b4.positions ) {
gmap\_m0c5bd0a7d321390ac744e25e805d24b4.bounds.extend( gmap\_m0c5bd0a7d321390ac744e25e805d24b4.positions[m] );
}
// Render markers
for ( var m in gmap\_m0c5bd0a7d321390ac744e25e805d24b4.positions ) {
gmap\_m0c5bd0a7d321390ac744e25e805d24b4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0c5bd0a7d321390ac744e25e805d24b4.map,
position : gmap\_m0c5bd0a7d321390ac744e25e805d24b4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0c5bd0a7d321390ac744e25e805d24b4.map.setCenter( gmap\_m0c5bd0a7d321390ac744e25e805d24b4.positions[682] );
});