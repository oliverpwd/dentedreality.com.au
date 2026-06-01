---
title: Dusk
date: '2013-12-03T11:12:58+00:00'
format: image
service: flickr
tags:
- dusk
- france
- paris
- sky
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900377876_c4b94a7667_o.jpg?fit=1500%2C1500
---

[![Dusk](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13900377876_c4b94a7667_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/03/dusk/) 
# [Dusk](http://dentedreality.com.au/2013/12/03/dusk/)





* #[dusk](http://dentedreality.com.au/tags/dusk/)
* #[france](http://dentedreality.com.au/tags/france/)
* #[paris](http://dentedreality.com.au/tags/paris/)
* #[sky](http://dentedreality.com.au/tags/sky/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13900377876/) [11:12 am, December 3, 2013](http://dentedreality.com.au/2013/12/03/dusk/ "11:12 am") 
jQuery(document).ready(function(){
var gmap\_m8694bf3c4a8235742c606272590106fc = {
positions : {
436 : new google.maps.LatLng( '48.857011', '2.353952' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8694bf3c4a8235742c606272590106fc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8694bf3c4a8235742c606272590106fc.positions ) {
gmap\_m8694bf3c4a8235742c606272590106fc.bounds.extend( gmap\_m8694bf3c4a8235742c606272590106fc.positions[m] );
}
// Render markers
for ( var m in gmap\_m8694bf3c4a8235742c606272590106fc.positions ) {
gmap\_m8694bf3c4a8235742c606272590106fc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8694bf3c4a8235742c606272590106fc.map,
position : gmap\_m8694bf3c4a8235742c606272590106fc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8694bf3c4a8235742c606272590106fc.map.setCenter( gmap\_m8694bf3c4a8235742c606272590106fc.positions[436] );
});