---
title: ''
date: '2014-04-30T04:48:06+00:00'
format: image
service: instagram
tags:
- photo
- ullconf
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/914323_650746864995522_87824824_n.jpg?resize=640%2C640
---

[![Drinking the #ullconf-aid.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/04/914323_650746864995522_87824824_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/04/30/drinking-the-ullconf-aid/) 

Drinking the #ullconf-aid.





* #[photo](http://dentedreality.com.au/tags/photo/)
* #[ullconf](http://dentedreality.com.au/tags/ullconf/)

Posted on [Instagram](http://instagram.com/p/naNU7QimBL/) [4:48 am, April 30, 2014](http://dentedreality.com.au/2014/04/30/drinking-the-ullconf-aid/ "4:48 am") 
jQuery(document).ready(function(){
var gmap\_m7116a37ef50c0392d3ce59d066490e6c = {
positions : {
930 : new google.maps.LatLng( '52.6483', '-7.196821667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7116a37ef50c0392d3ce59d066490e6c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7116a37ef50c0392d3ce59d066490e6c.positions ) {
gmap\_m7116a37ef50c0392d3ce59d066490e6c.bounds.extend( gmap\_m7116a37ef50c0392d3ce59d066490e6c.positions[m] );
}
// Render markers
for ( var m in gmap\_m7116a37ef50c0392d3ce59d066490e6c.positions ) {
gmap\_m7116a37ef50c0392d3ce59d066490e6c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7116a37ef50c0392d3ce59d066490e6c.map,
position : gmap\_m7116a37ef50c0392d3ce59d066490e6c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7116a37ef50c0392d3ce59d066490e6c.map.setCenter( gmap\_m7116a37ef50c0392d3ce59d066490e6c.positions[930] );
});