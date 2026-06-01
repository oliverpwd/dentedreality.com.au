---
title: “The Church”
date: '2008-04-06T18:42:15+00:00'
format: image
service: flickr
tags:
- australia
- house
- masonry
- stone
- thechurch
- westernaustraliabremerbay
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2432629083_892280cdcd_o.jpg?resize=607%2C455
---

[!["The Church"](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2432629083_892280cdcd_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2008/04/06/the-church/) 
# [“The Church”](http://dentedreality.com.au/2008/04/06/the-church/)

A really strange "house" being built in Bremer Bay overlooking the ocean.





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[house](http://dentedreality.com.au/tags/house/)
* #[masonry](http://dentedreality.com.au/tags/masonry/)
* #[stone](http://dentedreality.com.au/tags/stone/)
* #[thechurch](http://dentedreality.com.au/tags/thechurch/)
* #[westernaustraliabremerbay](http://dentedreality.com.au/tags/westernaustraliabremerbay/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2432629083/) [6:42 pm, April 6, 2008](http://dentedreality.com.au/2008/04/06/the-church/ "6:42 pm") 
jQuery(document).ready(function(){
var gmap\_m43141027dc1576292b1c56c637d5243d = {
positions : {
418 : new google.maps.LatLng( '-34.45696', '119.365425' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m43141027dc1576292b1c56c637d5243d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m43141027dc1576292b1c56c637d5243d.positions ) {
gmap\_m43141027dc1576292b1c56c637d5243d.bounds.extend( gmap\_m43141027dc1576292b1c56c637d5243d.positions[m] );
}
// Render markers
for ( var m in gmap\_m43141027dc1576292b1c56c637d5243d.positions ) {
gmap\_m43141027dc1576292b1c56c637d5243d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m43141027dc1576292b1c56c637d5243d.map,
position : gmap\_m43141027dc1576292b1c56c637d5243d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m43141027dc1576292b1c56c637d5243d.map.setCenter( gmap\_m43141027dc1576292b1c56c637d5243d.positions[418] );
});