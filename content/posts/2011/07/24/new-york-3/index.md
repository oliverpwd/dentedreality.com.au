---
title: New York
date: '2011-07-24T09:53:38+00:00'
format: image
service: flickr
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6322934993_42a8b7c62b_o.jpg?resize=607%2C452
---

[![New York](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/07/6322934993_42a8b7c62b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/07/24/new-york-3/) 
# [New York](http://dentedreality.com.au/2011/07/24/new-york-3/)





Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6322934993/) [9:53 am, July 24, 2011](http://dentedreality.com.au/2011/07/24/new-york-3/ "9:53 am") 
jQuery(document).ready(function(){
var gmap\_m75e122e999af1375e56307e5dbb973a7 = {
positions : {
615 : new google.maps.LatLng( '40.7175', '-73.958167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m75e122e999af1375e56307e5dbb973a7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m75e122e999af1375e56307e5dbb973a7.positions ) {
gmap\_m75e122e999af1375e56307e5dbb973a7.bounds.extend( gmap\_m75e122e999af1375e56307e5dbb973a7.positions[m] );
}
// Render markers
for ( var m in gmap\_m75e122e999af1375e56307e5dbb973a7.positions ) {
gmap\_m75e122e999af1375e56307e5dbb973a7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m75e122e999af1375e56307e5dbb973a7.map,
position : gmap\_m75e122e999af1375e56307e5dbb973a7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m75e122e999af1375e56307e5dbb973a7.map.setCenter( gmap\_m75e122e999af1375e56307e5dbb973a7.positions[615] );
});