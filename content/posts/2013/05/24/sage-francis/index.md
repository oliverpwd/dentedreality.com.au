---
title: Sage Francis
date: '2013-05-24T20:24:27+00:00'
format: image
service: flickr
tags:
- concert
- knittingfactory
- livemusic
- sagefrancis
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436933271_8f2c1dcff9_o.jpg?resize=607%2C452
---

[![Sage Francis](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436933271_8f2c1dcff9_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/05/24/sage-francis/) 
# [Sage Francis](http://dentedreality.com.au/2013/05/24/sage-francis/)

At the Knitting Factory





* #[concert](http://dentedreality.com.au/tags/concert/)
* #[knittingfactory](http://dentedreality.com.au/tags/knittingfactory/)
* #[livemusic](http://dentedreality.com.au/tags/livemusic/)
* #[sagefrancis](http://dentedreality.com.au/tags/sagefrancis/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9436933271/) [8:24 pm, May 24, 2013](http://dentedreality.com.au/2013/05/24/sage-francis/ "8:24 pm") 
jQuery(document).ready(function(){
var gmap\_m4a73966ab5d5de537166d1ffccd22bfc = {
positions : {
873 : new google.maps.LatLng( '40.714333', '-73.955834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4a73966ab5d5de537166d1ffccd22bfc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4a73966ab5d5de537166d1ffccd22bfc.positions ) {
gmap\_m4a73966ab5d5de537166d1ffccd22bfc.bounds.extend( gmap\_m4a73966ab5d5de537166d1ffccd22bfc.positions[m] );
}
// Render markers
for ( var m in gmap\_m4a73966ab5d5de537166d1ffccd22bfc.positions ) {
gmap\_m4a73966ab5d5de537166d1ffccd22bfc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4a73966ab5d5de537166d1ffccd22bfc.map,
position : gmap\_m4a73966ab5d5de537166d1ffccd22bfc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4a73966ab5d5de537166d1ffccd22bfc.map.setCenter( gmap\_m4a73966ab5d5de537166d1ffccd22bfc.positions[873] );
});