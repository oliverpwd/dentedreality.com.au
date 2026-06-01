---
title: ''
date: '2014-05-27T13:32:29+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/05/10358288_244695669062642_1889681349_n.jpg?resize=640%2C640
---

[![So hot, they're dropping like flies.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/05/10358288_244695669062642_1889681349_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/05/27/so-hot-theyre-dropping-like-flies/) 

So hot, they’re dropping like flies.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/ogqzO6imCB/) [1:32 pm, May 27, 2014](http://dentedreality.com.au/2014/05/27/so-hot-theyre-dropping-like-flies/ "1:32 pm") 
jQuery(document).ready(function(){
var gmap\_m217163574a3ad7377989c1248342b122 = {
positions : {
217 : new google.maps.LatLng( '40.669405', '-73.984978333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m217163574a3ad7377989c1248342b122' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m217163574a3ad7377989c1248342b122.positions ) {
gmap\_m217163574a3ad7377989c1248342b122.bounds.extend( gmap\_m217163574a3ad7377989c1248342b122.positions[m] );
}
// Render markers
for ( var m in gmap\_m217163574a3ad7377989c1248342b122.positions ) {
gmap\_m217163574a3ad7377989c1248342b122.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m217163574a3ad7377989c1248342b122.map,
position : gmap\_m217163574a3ad7377989c1248342b122.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m217163574a3ad7377989c1248342b122.map.setCenter( gmap\_m217163574a3ad7377989c1248342b122.positions[217] );
});