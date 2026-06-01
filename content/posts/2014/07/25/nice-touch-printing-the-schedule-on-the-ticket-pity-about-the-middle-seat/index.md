---
title: ''
date: '2014-07-25T14:17:53+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/07/10518020_260764410784152_358312467_n.jpg?resize=640%2C640
---

[![Nice touch printing the "schedule" on the ticket (pity about the middle seat :(](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/07/10518020_260764410784152_358312467_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/07/25/nice-touch-printing-the-schedule-on-the-ticket-pity-about-the-middle-seat/) 

Nice touch printing the “schedule” on the ticket (pity about the middle seat ![:(](http://i1.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_sad.gif?w=607)





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/q4q5dHCmKX/) [2:17 pm, July 25, 2014](http://dentedreality.com.au/2014/07/25/nice-touch-printing-the-schedule-on-the-ticket-pity-about-the-middle-seat/ "2:17 pm") 
jQuery(document).ready(function(){
var gmap\_m35a58030269ba98bfe190255c34bee60 = {
positions : {
592 : new google.maps.LatLng( '39.858801508', '-104.675928339' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m35a58030269ba98bfe190255c34bee60' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m35a58030269ba98bfe190255c34bee60.positions ) {
gmap\_m35a58030269ba98bfe190255c34bee60.bounds.extend( gmap\_m35a58030269ba98bfe190255c34bee60.positions[m] );
}
// Render markers
for ( var m in gmap\_m35a58030269ba98bfe190255c34bee60.positions ) {
gmap\_m35a58030269ba98bfe190255c34bee60.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m35a58030269ba98bfe190255c34bee60.map,
position : gmap\_m35a58030269ba98bfe190255c34bee60.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m35a58030269ba98bfe190255c34bee60.map.setCenter( gmap\_m35a58030269ba98bfe190255c34bee60.positions[592] );
});