---
title: Me in Oslo
date: '2011-10-29T10:33:03+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- me
- norway
- Oslo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6958278545_438edcda17_o.jpg?resize=480%2C640
---

[![Me in Oslo](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6958278545_438edcda17_o.jpg?resize=480%2C640)](http://dentedreality.com.au/2011/10/29/me-in-oslo/) 
# [Me in Oslo](http://dentedreality.com.au/2011/10/29/me-in-oslo/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[norway](http://dentedreality.com.au/tags/norway/)
* #[Oslo](http://dentedreality.com.au/tags/oslo/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958278545/) [10:33 am, October 29, 2011](http://dentedreality.com.au/2011/10/29/me-in-oslo/ "10:33 am") 
jQuery(document).ready(function(){
var gmap\_mcb8fc8001460b5017368c7961ed269fa = {
positions : {
61 : new google.maps.LatLng( '59.965', '10.6665' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mcb8fc8001460b5017368c7961ed269fa' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mcb8fc8001460b5017368c7961ed269fa.positions ) {
gmap\_mcb8fc8001460b5017368c7961ed269fa.bounds.extend( gmap\_mcb8fc8001460b5017368c7961ed269fa.positions[m] );
}
// Render markers
for ( var m in gmap\_mcb8fc8001460b5017368c7961ed269fa.positions ) {
gmap\_mcb8fc8001460b5017368c7961ed269fa.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mcb8fc8001460b5017368c7961ed269fa.map,
position : gmap\_mcb8fc8001460b5017368c7961ed269fa.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mcb8fc8001460b5017368c7961ed269fa.map.setCenter( gmap\_mcb8fc8001460b5017368c7961ed269fa.positions[61] );
});