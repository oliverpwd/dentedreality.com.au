---
title: Gingers!
date: '2011-12-24T10:51:37+00:00'
format: image
service: flickr
tags:
- cookies
- gingerbread
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6813293248_e2184e982d_o.jpg?resize=607%2C452
---

[![Gingers!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6813293248_e2184e982d_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/12/24/gingers/) 
# [Gingers!](http://dentedreality.com.au/2011/12/24/gingers/)

They have no souls.





* #[cookies](http://dentedreality.com.au/tags/cookies/)
* #[gingerbread](http://dentedreality.com.au/tags/gingerbread/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813293248/) [10:51 am, December 24, 2011](http://dentedreality.com.au/2011/12/24/gingers/ "10:51 am") 
jQuery(document).ready(function(){
var gmap\_m4254b91987632fe77a1c438de7114baf = {
positions : {
830 : new google.maps.LatLng( '37.736', '-122.433834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4254b91987632fe77a1c438de7114baf' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4254b91987632fe77a1c438de7114baf.positions ) {
gmap\_m4254b91987632fe77a1c438de7114baf.bounds.extend( gmap\_m4254b91987632fe77a1c438de7114baf.positions[m] );
}
// Render markers
for ( var m in gmap\_m4254b91987632fe77a1c438de7114baf.positions ) {
gmap\_m4254b91987632fe77a1c438de7114baf.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4254b91987632fe77a1c438de7114baf.map,
position : gmap\_m4254b91987632fe77a1c438de7114baf.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4254b91987632fe77a1c438de7114baf.map.setCenter( gmap\_m4254b91987632fe77a1c438de7114baf.positions[830] );
});