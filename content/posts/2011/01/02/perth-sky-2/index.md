---
title: Perth Sky
date: '2011-01-02T08:37:57+00:00'
format: image
service: flickr
tags:
- australia
- perth
- sky
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434098685_bbcaed9fd2_o.jpg?resize=607%2C452
---

[![Perth Sky](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434098685_bbcaed9fd2_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/02/perth-sky-2/) 
# [Perth Sky](http://dentedreality.com.au/2011/01/02/perth-sky-2/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[perth](http://dentedreality.com.au/tags/perth/)
* #[sky](http://dentedreality.com.au/tags/sky/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434098685/) [8:37 am, January 2, 2011](http://dentedreality.com.au/2011/01/02/perth-sky-2/ "8:37 am") 
jQuery(document).ready(function(){
var gmap\_mc5fbe49a51100781a5b4b76ad89d297e = {
positions : {
495 : new google.maps.LatLng( '-32.053', '115.846499' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc5fbe49a51100781a5b4b76ad89d297e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc5fbe49a51100781a5b4b76ad89d297e.positions ) {
gmap\_mc5fbe49a51100781a5b4b76ad89d297e.bounds.extend( gmap\_mc5fbe49a51100781a5b4b76ad89d297e.positions[m] );
}
// Render markers
for ( var m in gmap\_mc5fbe49a51100781a5b4b76ad89d297e.positions ) {
gmap\_mc5fbe49a51100781a5b4b76ad89d297e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc5fbe49a51100781a5b4b76ad89d297e.map,
position : gmap\_mc5fbe49a51100781a5b4b76ad89d297e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc5fbe49a51100781a5b4b76ad89d297e.map.setCenter( gmap\_mc5fbe49a51100781a5b4b76ad89d297e.positions[495] );
});