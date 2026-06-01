---
title: House on a Hill
date: '2008-04-06T18:42:37+00:00'
format: image
service: flickr
tags:
- australia
- beach
- house
- ocean
- view
- westernaustraliabremerbay
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433445750_eaab7c5e57_o.jpg?resize=607%2C455
---

[![House on a Hill](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433445750_eaab7c5e57_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2008/04/06/house-on-a-hill/) 
# [House on a Hill](http://dentedreality.com.au/2008/04/06/house-on-a-hill/)

Very mediterranean-looking.





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[house](http://dentedreality.com.au/tags/house/)
* #[ocean](http://dentedreality.com.au/tags/ocean/)
* #[view](http://dentedreality.com.au/tags/view/)
* #[westernaustraliabremerbay](http://dentedreality.com.au/tags/westernaustraliabremerbay/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2433445750/) [6:42 pm, April 6, 2008](http://dentedreality.com.au/2008/04/06/house-on-a-hill/ "6:42 pm") 
jQuery(document).ready(function(){
var gmap\_m5d05bf31cf6d028ad971d8646f570e0e = {
positions : {
241 : new google.maps.LatLng( '-34.45696', '119.365425' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5d05bf31cf6d028ad971d8646f570e0e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5d05bf31cf6d028ad971d8646f570e0e.positions ) {
gmap\_m5d05bf31cf6d028ad971d8646f570e0e.bounds.extend( gmap\_m5d05bf31cf6d028ad971d8646f570e0e.positions[m] );
}
// Render markers
for ( var m in gmap\_m5d05bf31cf6d028ad971d8646f570e0e.positions ) {
gmap\_m5d05bf31cf6d028ad971d8646f570e0e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5d05bf31cf6d028ad971d8646f570e0e.map,
position : gmap\_m5d05bf31cf6d028ad971d8646f570e0e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5d05bf31cf6d028ad971d8646f570e0e.map.setCenter( gmap\_m5d05bf31cf6d028ad971d8646f570e0e.positions[241] );
});