---
title: Northbridge Graffiti
date: '2011-01-09T15:04:26+00:00'
format: image
service: flickr
tags:
- graffiti
- northbridge
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434720412_e67887533f_o.jpg?resize=607%2C452
---

[![Northbridge Graffiti](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434720412_e67887533f_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/09/northbridge-graffiti/) 
# [Northbridge Graffiti](http://dentedreality.com.au/2011/01/09/northbridge-graffiti/)





* #[graffiti](http://dentedreality.com.au/tags/graffiti/)
* #[northbridge](http://dentedreality.com.au/tags/northbridge/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434720412/) [3:04 pm, January 9, 2011](http://dentedreality.com.au/2011/01/09/northbridge-graffiti/ "3:04 pm") 
jQuery(document).ready(function(){
var gmap\_m2db8be366486dc508c7f46957f75a19b = {
positions : {
93 : new google.maps.LatLng( '-31.948834', '115.8565' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2db8be366486dc508c7f46957f75a19b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2db8be366486dc508c7f46957f75a19b.positions ) {
gmap\_m2db8be366486dc508c7f46957f75a19b.bounds.extend( gmap\_m2db8be366486dc508c7f46957f75a19b.positions[m] );
}
// Render markers
for ( var m in gmap\_m2db8be366486dc508c7f46957f75a19b.positions ) {
gmap\_m2db8be366486dc508c7f46957f75a19b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2db8be366486dc508c7f46957f75a19b.map,
position : gmap\_m2db8be366486dc508c7f46957f75a19b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2db8be366486dc508c7f46957f75a19b.map.setCenter( gmap\_m2db8be366486dc508c7f46957f75a19b.positions[93] );
});