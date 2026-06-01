---
title: Pre-Maker Faire
date: '2012-09-30T08:34:19+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- me
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8244795543_19beaf7e34_o.jpg?resize=607%2C813
---

[![Pre-Maker Faire](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8244795543_19beaf7e34_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/09/30/pre-maker-faire/) 
# [Pre-Maker Faire](http://dentedreality.com.au/2012/09/30/pre-maker-faire/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8244795543/) [8:34 am, September 30, 2012](http://dentedreality.com.au/2012/09/30/pre-maker-faire/ "8:34 am") 
jQuery(document).ready(function(){
var gmap\_m83d57c5a487c7bb7455e058982f18780 = {
positions : {
412 : new google.maps.LatLng( '40.746666', '-73.899' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m83d57c5a487c7bb7455e058982f18780' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m83d57c5a487c7bb7455e058982f18780.positions ) {
gmap\_m83d57c5a487c7bb7455e058982f18780.bounds.extend( gmap\_m83d57c5a487c7bb7455e058982f18780.positions[m] );
}
// Render markers
for ( var m in gmap\_m83d57c5a487c7bb7455e058982f18780.positions ) {
gmap\_m83d57c5a487c7bb7455e058982f18780.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m83d57c5a487c7bb7455e058982f18780.map,
position : gmap\_m83d57c5a487c7bb7455e058982f18780.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m83d57c5a487c7bb7455e058982f18780.map.setCenter( gmap\_m83d57c5a487c7bb7455e058982f18780.positions[412] );
});