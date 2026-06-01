---
title: VIP Workshop, 2012
date: '2012-03-28T16:22:48+00:00'
format: image
service: flickr
tags:
- automattic
- vip
- wordpress
- wpvip
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7770425580_cbac8b4438_o.jpg?resize=607%2C452
---

[![VIP Workshop, 2012](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7770425580_cbac8b4438_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/28/vip-workshop-2012-2/) 
# [VIP Workshop, 2012](http://dentedreality.com.au/2012/03/28/vip-workshop-2012-2/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[vip](http://dentedreality.com.au/tags/vip/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)
* #[wpvip](http://dentedreality.com.au/tags/wpvip/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770425580/) [4:22 pm, March 28, 2012](http://dentedreality.com.au/2012/03/28/vip-workshop-2012-2/ "4:22 pm") 
jQuery(document).ready(function(){
var gmap\_m8b6534f2388954c51c1d463387b7c58e = {
positions : {
476 : new google.maps.LatLng( '38.505', '-122.468667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8b6534f2388954c51c1d463387b7c58e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8b6534f2388954c51c1d463387b7c58e.positions ) {
gmap\_m8b6534f2388954c51c1d463387b7c58e.bounds.extend( gmap\_m8b6534f2388954c51c1d463387b7c58e.positions[m] );
}
// Render markers
for ( var m in gmap\_m8b6534f2388954c51c1d463387b7c58e.positions ) {
gmap\_m8b6534f2388954c51c1d463387b7c58e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8b6534f2388954c51c1d463387b7c58e.map,
position : gmap\_m8b6534f2388954c51c1d463387b7c58e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8b6534f2388954c51c1d463387b7c58e.map.setCenter( gmap\_m8b6534f2388954c51c1d463387b7c58e.positions[476] );
});