---
title: Republica Dominica
date: '2013-12-26T12:24:08+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901127856_7c08203b93_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901127856_7c08203b93_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/26/republica-dominica-16/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/26/republica-dominica-16/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901127856/) [12:24 pm, December 26, 2013](http://dentedreality.com.au/2013/12/26/republica-dominica-16/ "12:24 pm") 
jQuery(document).ready(function(){
var gmap\_m7b1bc7f7fd41de608f41edd435392162 = {
positions : {
102 : new google.maps.LatLng( '19.585263', '-70.738831' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7b1bc7f7fd41de608f41edd435392162' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7b1bc7f7fd41de608f41edd435392162.positions ) {
gmap\_m7b1bc7f7fd41de608f41edd435392162.bounds.extend( gmap\_m7b1bc7f7fd41de608f41edd435392162.positions[m] );
}
// Render markers
for ( var m in gmap\_m7b1bc7f7fd41de608f41edd435392162.positions ) {
gmap\_m7b1bc7f7fd41de608f41edd435392162.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7b1bc7f7fd41de608f41edd435392162.map,
position : gmap\_m7b1bc7f7fd41de608f41edd435392162.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7b1bc7f7fd41de608f41edd435392162.map.setCenter( gmap\_m7b1bc7f7fd41de608f41edd435392162.positions[102] );
});