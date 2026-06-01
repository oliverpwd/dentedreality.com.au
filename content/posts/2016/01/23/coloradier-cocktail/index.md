---
title: ''
date: '2016-01-23T17:21:53+00:00'
format: image
service: instagram
tags:
- cocktail
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/01/12446234_918912504895574_1152093213_n.jpg?fit=640%2C640
---

[![Coloradier #cocktail](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/01/12446234_918912504895574_1152093213_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/01/23/coloradier-cocktail/) 

Coloradier #cocktail





* #[cocktail](http://dentedreality.com.au/tags/cocktail/)

Posted on [Instagram](https://www.instagram.com/p/BA5sgkXCmIZ/) [5:21 pm, January 23, 2016](http://dentedreality.com.au/2016/01/23/coloradier-cocktail/ "5:21 pm") 
jQuery(document).ready(function(){
var gmap\_m3093369fe02e20622b07ccab984b9686 = {
positions : {
805 : new google.maps.LatLng( '39.7530022', '-104.9997253' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3093369fe02e20622b07ccab984b9686' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3093369fe02e20622b07ccab984b9686.positions ) {
gmap\_m3093369fe02e20622b07ccab984b9686.bounds.extend( gmap\_m3093369fe02e20622b07ccab984b9686.positions[m] );
}
// Render markers
for ( var m in gmap\_m3093369fe02e20622b07ccab984b9686.positions ) {
gmap\_m3093369fe02e20622b07ccab984b9686.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3093369fe02e20622b07ccab984b9686.map,
position : gmap\_m3093369fe02e20622b07ccab984b9686.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3093369fe02e20622b07ccab984b9686.map.setCenter( gmap\_m3093369fe02e20622b07ccab984b9686.positions[805] );
});