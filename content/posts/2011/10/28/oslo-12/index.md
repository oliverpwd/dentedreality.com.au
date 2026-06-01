---
title: Oslo
date: '2011-10-28T06:44:06+00:00'
format: image
service: flickr
tags:
- coffee
- norway
- Oslo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812165774_898255d748_o.jpg?resize=607%2C452
---

[![Oslo](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6812165774_898255d748_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/10/28/oslo-12/) 
# [Oslo](http://dentedreality.com.au/2011/10/28/oslo-12/)





* #[coffee](http://dentedreality.com.au/tags/coffee/)
* #[norway](http://dentedreality.com.au/tags/norway/)
* #[Oslo](http://dentedreality.com.au/tags/oslo/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812165774/) [6:44 am, October 28, 2011](http://dentedreality.com.au/2011/10/28/oslo-12/ "6:44 am") 
jQuery(document).ready(function(){
var gmap\_m2245ba9a8ef7a7c40ecb6633799b3c42 = {
positions : {
832 : new google.maps.LatLng( '59.920666', '10.728' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2245ba9a8ef7a7c40ecb6633799b3c42' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2245ba9a8ef7a7c40ecb6633799b3c42.positions ) {
gmap\_m2245ba9a8ef7a7c40ecb6633799b3c42.bounds.extend( gmap\_m2245ba9a8ef7a7c40ecb6633799b3c42.positions[m] );
}
// Render markers
for ( var m in gmap\_m2245ba9a8ef7a7c40ecb6633799b3c42.positions ) {
gmap\_m2245ba9a8ef7a7c40ecb6633799b3c42.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2245ba9a8ef7a7c40ecb6633799b3c42.map,
position : gmap\_m2245ba9a8ef7a7c40ecb6633799b3c42.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2245ba9a8ef7a7c40ecb6633799b3c42.map.setCenter( gmap\_m2245ba9a8ef7a7c40ecb6633799b3c42.positions[832] );
});