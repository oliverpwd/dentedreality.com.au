---
title: ''
date: '2014-09-16T12:15:59+00:00'
format: image
tags:
- a8cgm
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10643844_456624664475757_1870721789_n.jpg?resize=640%2C640
---

[![#a8cgm learning Node and code name Calypso.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10643844_456624664475757_1870721789_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/09/16/a8cgm-learning-node-and-code-name-calypso/) 

#a8cgm learning Node and code name Calypso.





* #[a8cgm](http://dentedreality.com.au/tags/a8cgm/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/tBB8XuimO-/) [12:15 pm, September 16, 2014](http://dentedreality.com.au/2014/09/16/a8cgm-learning-node-and-code-name-calypso/ "12:15 pm") 
jQuery(document).ready(function(){
var gmap\_m86cfc53115bf7fdd537a168ace3dce91 = {
positions : {
889 : new google.maps.LatLng( '40.686207537', '-111.556048344' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m86cfc53115bf7fdd537a168ace3dce91' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m86cfc53115bf7fdd537a168ace3dce91.positions ) {
gmap\_m86cfc53115bf7fdd537a168ace3dce91.bounds.extend( gmap\_m86cfc53115bf7fdd537a168ace3dce91.positions[m] );
}
// Render markers
for ( var m in gmap\_m86cfc53115bf7fdd537a168ace3dce91.positions ) {
gmap\_m86cfc53115bf7fdd537a168ace3dce91.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m86cfc53115bf7fdd537a168ace3dce91.map,
position : gmap\_m86cfc53115bf7fdd537a168ace3dce91.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m86cfc53115bf7fdd537a168ace3dce91.map.setCenter( gmap\_m86cfc53115bf7fdd537a168ace3dce91.positions[889] );
});