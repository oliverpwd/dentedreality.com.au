---
title: Goat Banquet
date: '2013-12-28T08:49:15+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924692954_85e7237799_o.jpg?fit=1500%2C1500
---

[![Goat Banquet](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924692954_85e7237799_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/28/goat-banquet/) 
# [Goat Banquet](http://dentedreality.com.au/2013/12/28/goat-banquet/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924692954/) [8:49 am, December 28, 2013](http://dentedreality.com.au/2013/12/28/goat-banquet/ "8:49 am") 
jQuery(document).ready(function(){
var gmap\_mac4c38b31867add249f82708a14c2720 = {
positions : {
713 : new google.maps.LatLng( '19.690975', '-71.28875' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mac4c38b31867add249f82708a14c2720' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mac4c38b31867add249f82708a14c2720.positions ) {
gmap\_mac4c38b31867add249f82708a14c2720.bounds.extend( gmap\_mac4c38b31867add249f82708a14c2720.positions[m] );
}
// Render markers
for ( var m in gmap\_mac4c38b31867add249f82708a14c2720.positions ) {
gmap\_mac4c38b31867add249f82708a14c2720.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mac4c38b31867add249f82708a14c2720.map,
position : gmap\_mac4c38b31867add249f82708a14c2720.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mac4c38b31867add249f82708a14c2720.map.setCenter( gmap\_mac4c38b31867add249f82708a14c2720.positions[713] );
});