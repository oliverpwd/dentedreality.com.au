---
title: ''
date: '2016-09-12T14:13:17+00:00'
format: image
service: instagram
tags:
- 14er
- colorado
- mountains
- torreyspeak
- view
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14360076_532846916907045_801111330_n.jpg?fit=640%2C640
---

[![View from the top of the world. Torreys Peak on the weekend. #14er #torreyspeak #colorado #mountains #view](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/09/14360076_532846916907045_801111330_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/09/12/view-from-the-top-of-the-world-torreys-peak-on-the-weekend-14er-torreyspeak-colorado-mountains-view/) 

View from the top of the world. Torreys Peak on the weekend. #14er #torreyspeak #colorado #mountains #view





* #[14er](http://dentedreality.com.au/tags/14er/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[mountains](http://dentedreality.com.au/tags/mountains/)
* #[torreyspeak](http://dentedreality.com.au/tags/torreyspeak/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Instagram](https://www.instagram.com/p/BKRNRsNgsFZ/) [2:13 pm, September 12, 2016](http://dentedreality.com.au/2016/09/12/view-from-the-top-of-the-world-torreys-peak-on-the-weekend-14er-torreyspeak-colorado-mountains-view/ "2:13 pm") 
jQuery(document).ready(function(){
var gmap\_m59a237c892229a815be77b0ec288441f = {
positions : {
966 : new google.maps.LatLng( '39.642777777778', '-105.82111111111' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m59a237c892229a815be77b0ec288441f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m59a237c892229a815be77b0ec288441f.positions ) {
gmap\_m59a237c892229a815be77b0ec288441f.bounds.extend( gmap\_m59a237c892229a815be77b0ec288441f.positions[m] );
}
// Render markers
for ( var m in gmap\_m59a237c892229a815be77b0ec288441f.positions ) {
gmap\_m59a237c892229a815be77b0ec288441f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m59a237c892229a815be77b0ec288441f.map,
position : gmap\_m59a237c892229a815be77b0ec288441f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m59a237c892229a815be77b0ec288441f.map.setCenter( gmap\_m59a237c892229a815be77b0ec288441f.positions[966] );
});