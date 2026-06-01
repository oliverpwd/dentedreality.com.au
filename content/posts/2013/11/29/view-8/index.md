---
title: View
date: '2013-11-29T03:10:55+00:00'
format: image
service: flickr
tags:
- france
- paris
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900363182_f2a8f484bf_o.jpg?resize=607%2C455
---

[![View](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/13900363182_f2a8f484bf_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/29/view-8/) 
# [View](http://dentedreality.com.au/2013/11/29/view-8/)





* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900363182/) [3:10 am, November 29, 2013](http://dentedreality.com.au/2013/11/29/view-8/ "3:10 am") 
jQuery(document).ready(function(){
var gmap\_md7608acd8c5ad71bbb531466d8a1576b = {
positions : {
81 : new google.maps.LatLng( '48.88625', '2.343055' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md7608acd8c5ad71bbb531466d8a1576b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md7608acd8c5ad71bbb531466d8a1576b.positions ) {
gmap\_md7608acd8c5ad71bbb531466d8a1576b.bounds.extend( gmap\_md7608acd8c5ad71bbb531466d8a1576b.positions[m] );
}
// Render markers
for ( var m in gmap\_md7608acd8c5ad71bbb531466d8a1576b.positions ) {
gmap\_md7608acd8c5ad71bbb531466d8a1576b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md7608acd8c5ad71bbb531466d8a1576b.map,
position : gmap\_md7608acd8c5ad71bbb531466d8a1576b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md7608acd8c5ad71bbb531466d8a1576b.map.setCenter( gmap\_md7608acd8c5ad71bbb531466d8a1576b.positions[81] );
});