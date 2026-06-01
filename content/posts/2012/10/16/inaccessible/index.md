---
title: Inaccessible
date: '2012-10-16T14:43:21+00:00'
format: image
service: flickr
tags:
- accessibility
- WPNYC
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8245863616_14d560b242_o.jpg?resize=607%2C452
---

[![Inaccessible](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/10/8245863616_14d560b242_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/10/16/inaccessible/) 
# [Inaccessible](http://dentedreality.com.au/2012/10/16/inaccessible/)





* #[accessibility](http://dentedreality.com.au/tags/accessibility/)
* #[WPNYC](http://dentedreality.com.au/tags/wpnyc/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8245863616/) [2:43 pm, October 16, 2012](http://dentedreality.com.au/2012/10/16/inaccessible/ "2:43 pm") 
jQuery(document).ready(function(){
var gmap\_m5f9bd91043eea0361c18546adfd4f01d = {
positions : {
69 : new google.maps.LatLng( '40.725833', '-74.006' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5f9bd91043eea0361c18546adfd4f01d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5f9bd91043eea0361c18546adfd4f01d.positions ) {
gmap\_m5f9bd91043eea0361c18546adfd4f01d.bounds.extend( gmap\_m5f9bd91043eea0361c18546adfd4f01d.positions[m] );
}
// Render markers
for ( var m in gmap\_m5f9bd91043eea0361c18546adfd4f01d.positions ) {
gmap\_m5f9bd91043eea0361c18546adfd4f01d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5f9bd91043eea0361c18546adfd4f01d.map,
position : gmap\_m5f9bd91043eea0361c18546adfd4f01d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5f9bd91043eea0361c18546adfd4f01d.map.setCenter( gmap\_m5f9bd91043eea0361c18546adfd4f01d.positions[69] );
});