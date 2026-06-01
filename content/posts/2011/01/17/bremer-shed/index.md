---
title: Bremer Shed
date: '2011-01-17T14:05:07+00:00'
format: image
service: flickr
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434115529_9bbfab328f_o.jpg?resize=607%2C452
---

[![Bremer Shed](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434115529_9bbfab328f_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/17/bremer-shed/) 
# [Bremer Shed](http://dentedreality.com.au/2011/01/17/bremer-shed/)





Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434115529/) [2:05 pm, January 17, 2011](http://dentedreality.com.au/2011/01/17/bremer-shed/ "2:05 pm") 
jQuery(document).ready(function(){
var gmap\_mb8cc0f86a04f65e494c465e55290db3c = {
positions : {
689 : new google.maps.LatLng( '-34.405', '119.017' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb8cc0f86a04f65e494c465e55290db3c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb8cc0f86a04f65e494c465e55290db3c.positions ) {
gmap\_mb8cc0f86a04f65e494c465e55290db3c.bounds.extend( gmap\_mb8cc0f86a04f65e494c465e55290db3c.positions[m] );
}
// Render markers
for ( var m in gmap\_mb8cc0f86a04f65e494c465e55290db3c.positions ) {
gmap\_mb8cc0f86a04f65e494c465e55290db3c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb8cc0f86a04f65e494c465e55290db3c.map,
position : gmap\_mb8cc0f86a04f65e494c465e55290db3c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb8cc0f86a04f65e494c465e55290db3c.map.setCenter( gmap\_mb8cc0f86a04f65e494c465e55290db3c.positions[689] );
});