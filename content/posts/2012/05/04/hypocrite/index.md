---
title: Hypocrite
date: '2012-05-04T10:37:59+00:00'
format: image
service: flickr
tags:
- chees
- evan
- evansolomon
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/05/7770726950_b288dbff9b_o.jpg?resize=607%2C813
---

[![Hypocrite](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/05/7770726950_b288dbff9b_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/05/04/hypocrite/) 
# [Hypocrite](http://dentedreality.com.au/2012/05/04/hypocrite/)

Evan does not love cheese.





* #[chees](http://dentedreality.com.au/tags/chees/)
* #[evan](http://dentedreality.com.au/tags/evan/)
* #[evansolomon](http://dentedreality.com.au/tags/evansolomon/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770726950/) [10:37 am, May 4, 2012](http://dentedreality.com.au/2012/05/04/hypocrite/ "10:37 am") 
jQuery(document).ready(function(){
var gmap\_m205efb6ad88259af8234bdf028a75996 = {
positions : {
598 : new google.maps.LatLng( '37.7805', '-122.413667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m205efb6ad88259af8234bdf028a75996' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m205efb6ad88259af8234bdf028a75996.positions ) {
gmap\_m205efb6ad88259af8234bdf028a75996.bounds.extend( gmap\_m205efb6ad88259af8234bdf028a75996.positions[m] );
}
// Render markers
for ( var m in gmap\_m205efb6ad88259af8234bdf028a75996.positions ) {
gmap\_m205efb6ad88259af8234bdf028a75996.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m205efb6ad88259af8234bdf028a75996.map,
position : gmap\_m205efb6ad88259af8234bdf028a75996.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m205efb6ad88259af8234bdf028a75996.map.setCenter( gmap\_m205efb6ad88259af8234bdf028a75996.positions[598] );
});