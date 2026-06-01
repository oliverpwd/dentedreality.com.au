---
title: Brooklyn View to Manhattan
date: '2012-06-08T10:38:29+00:00'
format: image
service: flickr
tags:
- beer
- brooklyn
- Manhattan
- view
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7911183590_be9c652a12_o.jpg?resize=607%2C452
---

[![Brooklyn View to Manhattan](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/06/7911183590_be9c652a12_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/06/08/brooklyn-view-to-manhattan/) 
# [Brooklyn View to Manhattan](http://dentedreality.com.au/2012/06/08/brooklyn-view-to-manhattan/)





* #[beer](http://dentedreality.com.au/tags/beer/)
* #[brooklyn](http://dentedreality.com.au/tags/brooklyn/)
* #[Manhattan](http://dentedreality.com.au/tags/manhattan/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7911183590/) [10:38 am, June 8, 2012](http://dentedreality.com.au/2012/06/08/brooklyn-view-to-manhattan/ "10:38 am") 
jQuery(document).ready(function(){
var gmap\_m4f75f3841974b38b8d3ac744e1429b14 = {
positions : {
775 : new google.maps.LatLng( '40.669166', '-73.985' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4f75f3841974b38b8d3ac744e1429b14' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4f75f3841974b38b8d3ac744e1429b14.positions ) {
gmap\_m4f75f3841974b38b8d3ac744e1429b14.bounds.extend( gmap\_m4f75f3841974b38b8d3ac744e1429b14.positions[m] );
}
// Render markers
for ( var m in gmap\_m4f75f3841974b38b8d3ac744e1429b14.positions ) {
gmap\_m4f75f3841974b38b8d3ac744e1429b14.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4f75f3841974b38b8d3ac744e1429b14.map,
position : gmap\_m4f75f3841974b38b8d3ac744e1429b14.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4f75f3841974b38b8d3ac744e1429b14.map.setCenter( gmap\_m4f75f3841974b38b8d3ac744e1429b14.positions[775] );
});