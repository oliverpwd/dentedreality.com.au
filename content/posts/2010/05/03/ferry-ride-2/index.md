---
title: Ferry Ride
date: '2010-05-03T14:29:33+00:00'
format: image
service: flickr
tags:
- alameda
- boat
- ferry
- sanfrancisco
- treasureisland
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/05/4746454699_fd1450e507_o.jpg?resize=607%2C455
---

[![Ferry Ride](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/05/4746454699_fd1450e507_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/05/03/ferry-ride-2/) 
# [Ferry Ride](http://dentedreality.com.au/2010/05/03/ferry-ride-2/)





* #[alameda](http://dentedreality.com.au/tags/alameda/)
* #[boat](http://dentedreality.com.au/tags/boat/)
* #[ferry](http://dentedreality.com.au/tags/ferry/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[treasureisland](http://dentedreality.com.au/tags/treasureisland/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4746454699/) [2:29 pm, May 3, 2010](http://dentedreality.com.au/2010/05/03/ferry-ride-2/ "2:29 pm") 
jQuery(document).ready(function(){
var gmap\_m74b696130b6368844a11a8f6337959c9 = {
positions : {
400 : new google.maps.LatLng( '37.792666', '-122.3905' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m74b696130b6368844a11a8f6337959c9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m74b696130b6368844a11a8f6337959c9.positions ) {
gmap\_m74b696130b6368844a11a8f6337959c9.bounds.extend( gmap\_m74b696130b6368844a11a8f6337959c9.positions[m] );
}
// Render markers
for ( var m in gmap\_m74b696130b6368844a11a8f6337959c9.positions ) {
gmap\_m74b696130b6368844a11a8f6337959c9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m74b696130b6368844a11a8f6337959c9.map,
position : gmap\_m74b696130b6368844a11a8f6337959c9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m74b696130b6368844a11a8f6337959c9.map.setCenter( gmap\_m74b696130b6368844a11a8f6337959c9.positions[400] );
});