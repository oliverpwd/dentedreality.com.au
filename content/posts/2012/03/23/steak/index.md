---
title: Steak
date: '2012-03-23T17:23:08+00:00'
format: image
service: flickr
tags:
- food
- meat
- steak
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721702578_beda7ec094_o.jpg?resize=607%2C452
---

[![Steak](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/03/7721702578_beda7ec094_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/03/23/steak/) 
# [Steak](http://dentedreality.com.au/2012/03/23/steak/)





* #[food](http://dentedreality.com.au/tags/food/)
* #[meat](http://dentedreality.com.au/tags/meat/)
* #[steak](http://dentedreality.com.au/tags/steak/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7721702578/) [5:23 pm, March 23, 2012](http://dentedreality.com.au/2012/03/23/steak/ "5:23 pm") 
jQuery(document).ready(function(){
var gmap\_m6c2551c3a8b17a5317a306a8e6ad90ed = {
positions : {
91 : new google.maps.LatLng( '37.795166', '-122.423167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6c2551c3a8b17a5317a306a8e6ad90ed' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6c2551c3a8b17a5317a306a8e6ad90ed.positions ) {
gmap\_m6c2551c3a8b17a5317a306a8e6ad90ed.bounds.extend( gmap\_m6c2551c3a8b17a5317a306a8e6ad90ed.positions[m] );
}
// Render markers
for ( var m in gmap\_m6c2551c3a8b17a5317a306a8e6ad90ed.positions ) {
gmap\_m6c2551c3a8b17a5317a306a8e6ad90ed.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6c2551c3a8b17a5317a306a8e6ad90ed.map,
position : gmap\_m6c2551c3a8b17a5317a306a8e6ad90ed.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6c2551c3a8b17a5317a306a8e6ad90ed.map.setCenter( gmap\_m6c2551c3a8b17a5317a306a8e6ad90ed.positions[91] );
});