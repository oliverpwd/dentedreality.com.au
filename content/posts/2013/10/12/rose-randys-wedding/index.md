---
title: Rose & Randy’s Wedding
date: '2013-10-12T15:21:16+00:00'
format: image
service: flickr
tags:
- randy
- rose
- simonwedding
- wedding
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291589936_0e31ae36cd_o.jpg?fit=1500%2C1500
---

[![Rose & Randy's Wedding](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291589936_0e31ae36cd_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/10/12/rose-randys-wedding/) 
# [Rose & Randy’s Wedding](http://dentedreality.com.au/2013/10/12/rose-randys-wedding/)





* #[randy](http://dentedreality.com.au/tags/randy/)
* #[rose](http://dentedreality.com.au/tags/rose/)
* #[simonwedding](http://dentedreality.com.au/tags/simonwedding/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291589936/) [3:21 pm, October 12, 2013](http://dentedreality.com.au/2013/10/12/rose-randys-wedding/ "3:21 pm") 
jQuery(document).ready(function(){
var gmap\_mc642ccd044c2429630aaf3268d0625bc = {
positions : {
933 : new google.maps.LatLng( '38.410166', '-122.556' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc642ccd044c2429630aaf3268d0625bc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc642ccd044c2429630aaf3268d0625bc.positions ) {
gmap\_mc642ccd044c2429630aaf3268d0625bc.bounds.extend( gmap\_mc642ccd044c2429630aaf3268d0625bc.positions[m] );
}
// Render markers
for ( var m in gmap\_mc642ccd044c2429630aaf3268d0625bc.positions ) {
gmap\_mc642ccd044c2429630aaf3268d0625bc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc642ccd044c2429630aaf3268d0625bc.map,
position : gmap\_mc642ccd044c2429630aaf3268d0625bc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc642ccd044c2429630aaf3268d0625bc.map.setCenter( gmap\_mc642ccd044c2429630aaf3268d0625bc.positions[933] );
});