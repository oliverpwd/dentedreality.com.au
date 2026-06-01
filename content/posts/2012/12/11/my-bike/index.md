---
title: My Bike
date: '2012-12-11T11:35:34+00:00'
format: image
service: flickr
tags:
- badboy9
- bicycle
- bike
- cannondale
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8460376110_220d77bbd8_o.jpg?resize=607%2C452
---

[![My Bike](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8460376110_220d77bbd8_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/12/11/my-bike/) 
# [My Bike](http://dentedreality.com.au/2012/12/11/my-bike/)





* #[badboy9](http://dentedreality.com.au/tags/badboy9/)
* #[bicycle](http://dentedreality.com.au/tags/bicycle/)
* #[bike](http://dentedreality.com.au/tags/bike/)
* #[cannondale](http://dentedreality.com.au/tags/cannondale/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460376110/) [11:35 am, December 11, 2012](http://dentedreality.com.au/2012/12/11/my-bike/ "11:35 am") 
jQuery(document).ready(function(){
var gmap\_me7926a88c0bce197a0a6f236e1dbdf66 = {
positions : {
159 : new google.maps.LatLng( '40.671333', '-73.985' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me7926a88c0bce197a0a6f236e1dbdf66' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me7926a88c0bce197a0a6f236e1dbdf66.positions ) {
gmap\_me7926a88c0bce197a0a6f236e1dbdf66.bounds.extend( gmap\_me7926a88c0bce197a0a6f236e1dbdf66.positions[m] );
}
// Render markers
for ( var m in gmap\_me7926a88c0bce197a0a6f236e1dbdf66.positions ) {
gmap\_me7926a88c0bce197a0a6f236e1dbdf66.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me7926a88c0bce197a0a6f236e1dbdf66.map,
position : gmap\_me7926a88c0bce197a0a6f236e1dbdf66.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me7926a88c0bce197a0a6f236e1dbdf66.map.setCenter( gmap\_me7926a88c0bce197a0a6f236e1dbdf66.positions[159] );
});