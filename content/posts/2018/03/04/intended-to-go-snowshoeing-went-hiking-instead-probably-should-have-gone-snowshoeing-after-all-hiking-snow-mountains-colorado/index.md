---
title: ''
date: '2018-03-04T21:38:36+00:00'
format: image
service: instagram
tags:
- colorado
- hiking
- mountains
- snow
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2018/03/28157647_159264241441691_8679941167900524544_n.jpg?fit=640%2C640&ssl=1
---

[![Intended to go snowshoeing, went hiking instead. Probably should have gone snowshoeing after all. #hiking #snow #mountains #Colorado](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2018/03/28157647_159264241441691_8679941167900524544_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2018/03/04/intended-to-go-snowshoeing-went-hiking-instead-probably-should-have-gone-snowshoeing-after-all-hiking-snow-mountains-colorado/) 

[![Intended to go snowshoeing, went hiking instead. Probably should have gone snowshoeing after all. #hiking #snow #mountains #Colorado](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2018/03/28157647_159264241441691_8679941167900524544_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/Bf7axcWhWV3/)

Intended to go snowshoeing, went hiking instead. Probably should have gone snowshoeing after all. #hiking #snow #mountains #Colorado





* #[colorado](https://dentedreality.com.au/tags/colorado/)
* #[hiking](https://dentedreality.com.au/tags/hiking/)
* #[mountains](https://dentedreality.com.au/tags/mountains/)
* #[snow](https://dentedreality.com.au/tags/snow/)

Posted on [Instagram](https://www.instagram.com/p/Bf7axcWhWV3/) [9:38 pm, March 4, 2018](https://dentedreality.com.au/2018/03/04/intended-to-go-snowshoeing-went-hiking-instead-probably-should-have-gone-snowshoeing-after-all-hiking-snow-mountains-colorado/ "9:38 pm") 
jQuery(document).ready(function(){
var gmap\_m23d496f5373d7f91f093a6103a800ace = {
positions : {
611 : new google.maps.LatLng( '39.702457', '-105.854212' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m23d496f5373d7f91f093a6103a800ace' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m23d496f5373d7f91f093a6103a800ace.positions ) {
gmap\_m23d496f5373d7f91f093a6103a800ace.bounds.extend( gmap\_m23d496f5373d7f91f093a6103a800ace.positions[m] );
}
// Render markers
for ( var m in gmap\_m23d496f5373d7f91f093a6103a800ace.positions ) {
gmap\_m23d496f5373d7f91f093a6103a800ace.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m23d496f5373d7f91f093a6103a800ace.map,
position : gmap\_m23d496f5373d7f91f093a6103a800ace.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m23d496f5373d7f91f093a6103a800ace.map.setCenter( gmap\_m23d496f5373d7f91f093a6103a800ace.positions[611] );
});