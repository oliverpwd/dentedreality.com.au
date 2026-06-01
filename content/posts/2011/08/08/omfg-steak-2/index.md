---
title: OMFG Steak
date: '2011-08-08T16:09:43+00:00'
format: image
service: flickr
tags:
- 4505meats
- steak
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6323517330_273d764813_o.jpg?resize=607%2C452
---

[![OMFG Steak](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6323517330_273d764813_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/08/08/omfg-steak-2/) 
# [OMFG Steak](http://dentedreality.com.au/2011/08/08/omfg-steak-2/)

2.5 lb steaks from 4505 Meats





* #[4505meats](http://dentedreality.com.au/tags/4505meats/)
* #[steak](http://dentedreality.com.au/tags/steak/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6323517330/) [4:09 pm, August 8, 2011](http://dentedreality.com.au/2011/08/08/omfg-steak-2/ "4:09 pm") 
jQuery(document).ready(function(){
var gmap\_m29e4f4b4c5c1e01be36044afc3f73f33 = {
positions : {
845 : new google.maps.LatLng( '37.791333', '-122.417667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m29e4f4b4c5c1e01be36044afc3f73f33' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m29e4f4b4c5c1e01be36044afc3f73f33.positions ) {
gmap\_m29e4f4b4c5c1e01be36044afc3f73f33.bounds.extend( gmap\_m29e4f4b4c5c1e01be36044afc3f73f33.positions[m] );
}
// Render markers
for ( var m in gmap\_m29e4f4b4c5c1e01be36044afc3f73f33.positions ) {
gmap\_m29e4f4b4c5c1e01be36044afc3f73f33.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m29e4f4b4c5c1e01be36044afc3f73f33.map,
position : gmap\_m29e4f4b4c5c1e01be36044afc3f73f33.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m29e4f4b4c5c1e01be36044afc3f73f33.map.setCenter( gmap\_m29e4f4b4c5c1e01be36044afc3f73f33.positions[845] );
});