---
title: ''
date: '2014-09-15T17:42:27+00:00'
format: image
tags:
- a8cmeetup
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10684045_702580793152890_21977454_n.jpg?resize=640%2C640
---

[![Utah clouding. #a8cmeetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10684045_702580793152890_21977454_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/09/15/utah-clouding-a8cmeetup/) 

Utah clouding. #a8cmeetup





* #[a8cmeetup](http://dentedreality.com.au/tags/a8cmeetup/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/s_CgsrimOI/) [5:42 pm, September 15, 2014](http://dentedreality.com.au/2014/09/15/utah-clouding-a8cmeetup/ "5:42 pm") 
jQuery(document).ready(function(){
var gmap\_m16786442fce495a68f67531645b086dc = {
positions : {
469 : new google.maps.LatLng( '39.483546667', '-110.512428333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m16786442fce495a68f67531645b086dc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m16786442fce495a68f67531645b086dc.positions ) {
gmap\_m16786442fce495a68f67531645b086dc.bounds.extend( gmap\_m16786442fce495a68f67531645b086dc.positions[m] );
}
// Render markers
for ( var m in gmap\_m16786442fce495a68f67531645b086dc.positions ) {
gmap\_m16786442fce495a68f67531645b086dc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m16786442fce495a68f67531645b086dc.map,
position : gmap\_m16786442fce495a68f67531645b086dc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m16786442fce495a68f67531645b086dc.map.setCenter( gmap\_m16786442fce495a68f67531645b086dc.positions[469] );
});