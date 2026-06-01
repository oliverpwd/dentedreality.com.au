---
title: Republica Dominica
date: '2013-12-30T11:03:49+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
- panorama
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924703784_d6ddc7b105_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924703784_d6ddc7b105_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/30/republica-dominica-6/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/30/republica-dominica-6/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)
* #[panorama](http://dentedreality.com.au/tags/panorama/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924703784/) [11:03 am, December 30, 2013](http://dentedreality.com.au/2013/12/30/republica-dominica-6/ "11:03 am") 
jQuery(document).ready(function(){
var gmap\_m6206914ca9aff647154b33872bbc3ca4 = {
positions : {
623 : new google.maps.LatLng( '19.093477', '-70.59462' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6206914ca9aff647154b33872bbc3ca4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6206914ca9aff647154b33872bbc3ca4.positions ) {
gmap\_m6206914ca9aff647154b33872bbc3ca4.bounds.extend( gmap\_m6206914ca9aff647154b33872bbc3ca4.positions[m] );
}
// Render markers
for ( var m in gmap\_m6206914ca9aff647154b33872bbc3ca4.positions ) {
gmap\_m6206914ca9aff647154b33872bbc3ca4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6206914ca9aff647154b33872bbc3ca4.map,
position : gmap\_m6206914ca9aff647154b33872bbc3ca4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6206914ca9aff647154b33872bbc3ca4.map.setCenter( gmap\_m6206914ca9aff647154b33872bbc3ca4.positions[623] );
});