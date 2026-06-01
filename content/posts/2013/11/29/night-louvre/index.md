---
title: Night Louvre
date: '2013-11-29T14:08:57+00:00'
format: image
service: flickr
tags:
- france
- louvre
- paris
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900360146_681a7308cb_o.jpg?fit=1500%2C1500
---

[![Night Louvre](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900360146_681a7308cb_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/11/29/night-louvre/) 
# [Night Louvre](http://dentedreality.com.au/2013/11/29/night-louvre/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[louvre](http://dentedreality.com.au/tags/louvre/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900360146/) [2:08 pm, November 29, 2013](http://dentedreality.com.au/2013/11/29/night-louvre/ "2:08 pm") 
jQuery(document).ready(function(){
var gmap\_m4b1f7aea6ec558702757475ad363f0d7 = {
positions : {
652 : new google.maps.LatLng( '48.861652', '2.335011' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4b1f7aea6ec558702757475ad363f0d7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4b1f7aea6ec558702757475ad363f0d7.positions ) {
gmap\_m4b1f7aea6ec558702757475ad363f0d7.bounds.extend( gmap\_m4b1f7aea6ec558702757475ad363f0d7.positions[m] );
}
// Render markers
for ( var m in gmap\_m4b1f7aea6ec558702757475ad363f0d7.positions ) {
gmap\_m4b1f7aea6ec558702757475ad363f0d7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4b1f7aea6ec558702757475ad363f0d7.map,
position : gmap\_m4b1f7aea6ec558702757475ad363f0d7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4b1f7aea6ec558702757475ad363f0d7.map.setCenter( gmap\_m4b1f7aea6ec558702757475ad363f0d7.positions[652] );
});