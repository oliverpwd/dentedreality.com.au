---
title: OMFG Steak
date: '2011-08-02T18:31:38+00:00'
format: image
service: flickr
tags:
- 4505meats
- steak
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6323515010_471b356449_o.jpg?resize=607%2C452
---

[![OMFG Steak](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/08/6323515010_471b356449_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/08/02/omfg-steak-3/) 
# [OMFG Steak](http://dentedreality.com.au/2011/08/02/omfg-steak-3/)

2.5 lb steaks from 4505 Meats





* #[4505meats](http://dentedreality.com.au/tags/4505meats/)
* #[steak](http://dentedreality.com.au/tags/steak/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6323515010/) [6:31 pm, August 2, 2011](http://dentedreality.com.au/2011/08/02/omfg-steak-3/ "6:31 pm") 
jQuery(document).ready(function(){
var gmap\_mf6ac09d4daf0545f9b05a8f4fd0e1c92 = {
positions : {
173 : new google.maps.LatLng( '37.791333', '-122.417834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf6ac09d4daf0545f9b05a8f4fd0e1c92' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf6ac09d4daf0545f9b05a8f4fd0e1c92.positions ) {
gmap\_mf6ac09d4daf0545f9b05a8f4fd0e1c92.bounds.extend( gmap\_mf6ac09d4daf0545f9b05a8f4fd0e1c92.positions[m] );
}
// Render markers
for ( var m in gmap\_mf6ac09d4daf0545f9b05a8f4fd0e1c92.positions ) {
gmap\_mf6ac09d4daf0545f9b05a8f4fd0e1c92.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf6ac09d4daf0545f9b05a8f4fd0e1c92.map,
position : gmap\_mf6ac09d4daf0545f9b05a8f4fd0e1c92.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf6ac09d4daf0545f9b05a8f4fd0e1c92.map.setCenter( gmap\_mf6ac09d4daf0545f9b05a8f4fd0e1c92.positions[173] );
});