---
title: BEER
date: '2013-12-29T14:30:22+00:00'
format: image
service: flickr
tags:
- beer
- dominicanrepublic
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901126321_89d67a17f0_o.jpg?fit=1500%2C1500
---

[![BEER](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901126321_89d67a17f0_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/29/beer-2/) 
# [BEER](http://dentedreality.com.au/2013/12/29/beer-2/)





* #[beer](http://dentedreality.com.au/tags/beer/)
* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901126321/) [2:30 pm, December 29, 2013](http://dentedreality.com.au/2013/12/29/beer-2/ "2:30 pm") 
jQuery(document).ready(function(){
var gmap\_mae61c53068a90b350eebd6647696eb9b = {
positions : {
587 : new google.maps.LatLng( '19.409558', '-70.641342' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mae61c53068a90b350eebd6647696eb9b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mae61c53068a90b350eebd6647696eb9b.positions ) {
gmap\_mae61c53068a90b350eebd6647696eb9b.bounds.extend( gmap\_mae61c53068a90b350eebd6647696eb9b.positions[m] );
}
// Render markers
for ( var m in gmap\_mae61c53068a90b350eebd6647696eb9b.positions ) {
gmap\_mae61c53068a90b350eebd6647696eb9b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mae61c53068a90b350eebd6647696eb9b.map,
position : gmap\_mae61c53068a90b350eebd6647696eb9b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mae61c53068a90b350eebd6647696eb9b.map.setCenter( gmap\_mae61c53068a90b350eebd6647696eb9b.positions[587] );
});