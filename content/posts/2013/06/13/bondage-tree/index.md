---
title: Bondage Tree
date: '2013-06-13T17:54:02+00:00'
format: image
service: flickr
tags:
- art
- tree
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9437052045_ae7b667daa_o.jpg?resize=607%2C813
---

[![Bondage Tree](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9437052045_ae7b667daa_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2013/06/13/bondage-tree/) 
# [Bondage Tree](http://dentedreality.com.au/2013/06/13/bondage-tree/)





* #[art](http://dentedreality.com.au/tags/art/)
* #[tree](http://dentedreality.com.au/tags/tree/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437052045/) [5:54 pm, June 13, 2013](http://dentedreality.com.au/2013/06/13/bondage-tree/ "5:54 pm") 
jQuery(document).ready(function(){
var gmap\_m829fc99de68bfb313ddb90efa15027b2 = {
positions : {
715 : new google.maps.LatLng( '45.518333', '-122.674667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m829fc99de68bfb313ddb90efa15027b2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m829fc99de68bfb313ddb90efa15027b2.positions ) {
gmap\_m829fc99de68bfb313ddb90efa15027b2.bounds.extend( gmap\_m829fc99de68bfb313ddb90efa15027b2.positions[m] );
}
// Render markers
for ( var m in gmap\_m829fc99de68bfb313ddb90efa15027b2.positions ) {
gmap\_m829fc99de68bfb313ddb90efa15027b2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m829fc99de68bfb313ddb90efa15027b2.map,
position : gmap\_m829fc99de68bfb313ddb90efa15027b2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m829fc99de68bfb313ddb90efa15027b2.map.setCenter( gmap\_m829fc99de68bfb313ddb90efa15027b2.positions[715] );
});