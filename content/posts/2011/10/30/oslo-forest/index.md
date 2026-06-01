---
title: Oslo Forest
date: '2011-10-30T09:41:14+00:00'
format: image
service: flickr
tags:
- forest
- norway
- Oslo
- trees
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6958279263_c4a9f79d4f_o.jpg?resize=607%2C452
---

[![Oslo Forest](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6958279263_c4a9f79d4f_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/10/30/oslo-forest/) 
# [Oslo Forest](http://dentedreality.com.au/2011/10/30/oslo-forest/)





* #[forest](http://dentedreality.com.au/tags/forest/)
* #[norway](http://dentedreality.com.au/tags/norway/)
* #[Oslo](http://dentedreality.com.au/tags/oslo/)
* #[trees](http://dentedreality.com.au/tags/trees/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958279263/) [9:41 am, October 30, 2011](http://dentedreality.com.au/2011/10/30/oslo-forest/ "9:41 am") 
jQuery(document).ready(function(){
var gmap\_me3b8e77ebd0d708dea61378bb7a40c76 = {
positions : {
726 : new google.maps.LatLng( '59.974666', '10.726333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me3b8e77ebd0d708dea61378bb7a40c76' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me3b8e77ebd0d708dea61378bb7a40c76.positions ) {
gmap\_me3b8e77ebd0d708dea61378bb7a40c76.bounds.extend( gmap\_me3b8e77ebd0d708dea61378bb7a40c76.positions[m] );
}
// Render markers
for ( var m in gmap\_me3b8e77ebd0d708dea61378bb7a40c76.positions ) {
gmap\_me3b8e77ebd0d708dea61378bb7a40c76.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me3b8e77ebd0d708dea61378bb7a40c76.map,
position : gmap\_me3b8e77ebd0d708dea61378bb7a40c76.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me3b8e77ebd0d708dea61378bb7a40c76.map.setCenter( gmap\_me3b8e77ebd0d708dea61378bb7a40c76.positions[726] );
});