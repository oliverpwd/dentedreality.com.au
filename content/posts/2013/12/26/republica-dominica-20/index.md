---
title: Republica Dominica
date: '2013-12-26T10:26:24+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901132142_367682928d_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901132142_367682928d_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/26/republica-dominica-20/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/26/republica-dominica-20/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901132142/) [10:26 am, December 26, 2013](http://dentedreality.com.au/2013/12/26/republica-dominica-20/ "10:26 am") 
jQuery(document).ready(function(){
var gmap\_ma8d4923b892aaae9f6df6935f353852b = {
positions : {
106 : new google.maps.LatLng( '19.581105', '-70.74547' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma8d4923b892aaae9f6df6935f353852b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma8d4923b892aaae9f6df6935f353852b.positions ) {
gmap\_ma8d4923b892aaae9f6df6935f353852b.bounds.extend( gmap\_ma8d4923b892aaae9f6df6935f353852b.positions[m] );
}
// Render markers
for ( var m in gmap\_ma8d4923b892aaae9f6df6935f353852b.positions ) {
gmap\_ma8d4923b892aaae9f6df6935f353852b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma8d4923b892aaae9f6df6935f353852b.map,
position : gmap\_ma8d4923b892aaae9f6df6935f353852b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma8d4923b892aaae9f6df6935f353852b.map.setCenter( gmap\_ma8d4923b892aaae9f6df6935f353852b.positions[106] );
});