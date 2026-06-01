---
title: Bremer Bay
date: '2011-01-19T13:13:44+00:00'
format: image
service: flickr
tags:
- australia
- bremer
- bremerbay
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434787246_0de55fd7ce_o.jpg?resize=607%2C452
---

[![Bremer Bay](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434787246_0de55fd7ce_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/19/bremer-bay-28/) 
# [Bremer Bay](http://dentedreality.com.au/2011/01/19/bremer-bay-28/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[bremer](http://dentedreality.com.au/tags/bremer/)
* #[bremerbay](http://dentedreality.com.au/tags/bremerbay/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434787246/) [1:13 pm, January 19, 2011](http://dentedreality.com.au/2011/01/19/bremer-bay-28/ "1:13 pm") 
jQuery(document).ready(function(){
var gmap\_m6ff39c89407be10155b7f8aa0a09b181 = {
positions : {
560 : new google.maps.LatLng( '-34.394', '119.399666' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6ff39c89407be10155b7f8aa0a09b181' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6ff39c89407be10155b7f8aa0a09b181.positions ) {
gmap\_m6ff39c89407be10155b7f8aa0a09b181.bounds.extend( gmap\_m6ff39c89407be10155b7f8aa0a09b181.positions[m] );
}
// Render markers
for ( var m in gmap\_m6ff39c89407be10155b7f8aa0a09b181.positions ) {
gmap\_m6ff39c89407be10155b7f8aa0a09b181.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6ff39c89407be10155b7f8aa0a09b181.map,
position : gmap\_m6ff39c89407be10155b7f8aa0a09b181.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6ff39c89407be10155b7f8aa0a09b181.map.setCenter( gmap\_m6ff39c89407be10155b7f8aa0a09b181.positions[560] );
});