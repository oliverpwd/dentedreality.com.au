---
title: ''
date: '2015-05-10T16:23:37+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/11246310_1581581065450185_2033322749_n.jpg?resize=640%2C640
---

[![Here we go again.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/11246310_1581581065450185_2033322749_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/05/10/here-we-go-again/) 

Here we go again.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/2hJ4nmimEH/) [4:23 pm, May 10, 2015](http://dentedreality.com.au/2015/05/10/here-we-go-again/ "4:23 pm") 
jQuery(document).ready(function(){
var gmap\_m150d1a908799c607fea2896eab661868 = {
positions : {
666 : new google.maps.LatLng( '39.734836667', '-104.978438333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m150d1a908799c607fea2896eab661868' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m150d1a908799c607fea2896eab661868.positions ) {
gmap\_m150d1a908799c607fea2896eab661868.bounds.extend( gmap\_m150d1a908799c607fea2896eab661868.positions[m] );
}
// Render markers
for ( var m in gmap\_m150d1a908799c607fea2896eab661868.positions ) {
gmap\_m150d1a908799c607fea2896eab661868.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m150d1a908799c607fea2896eab661868.map,
position : gmap\_m150d1a908799c607fea2896eab661868.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m150d1a908799c607fea2896eab661868.map.setCenter( gmap\_m150d1a908799c607fea2896eab661868.positions[666] );
});