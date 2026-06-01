---
title: Dinner at Bluewater
date: '2011-01-13T17:06:45+00:00'
format: image
service: flickr
tags:
- affogatto
- bluewater
- dinner
- frangelico
- perth
- restaurant
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434111899_7015dfe760_o.jpg?resize=607%2C452
---

[![Dinner at Bluewater](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434111899_7015dfe760_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/13/dinner-at-bluewater/) 
# [Dinner at Bluewater](http://dentedreality.com.au/2011/01/13/dinner-at-bluewater/)

Frangelico Affogatto





* #[affogatto](http://dentedreality.com.au/tags/affogatto/)
* #[bluewater](http://dentedreality.com.au/tags/bluewater/)
* #[dinner](http://dentedreality.com.au/tags/dinner/)
* #[frangelico](http://dentedreality.com.au/tags/frangelico/)
* #[perth](http://dentedreality.com.au/tags/perth/)
* #[restaurant](http://dentedreality.com.au/tags/restaurant/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434111899/) [5:06 pm, January 13, 2011](http://dentedreality.com.au/2011/01/13/dinner-at-bluewater/ "5:06 pm") 
jQuery(document).ready(function(){
var gmap\_m1798e62e1f470032f75187630fc4420d = {
positions : {
978 : new google.maps.LatLng( '-32.003', '115.842166' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1798e62e1f470032f75187630fc4420d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1798e62e1f470032f75187630fc4420d.positions ) {
gmap\_m1798e62e1f470032f75187630fc4420d.bounds.extend( gmap\_m1798e62e1f470032f75187630fc4420d.positions[m] );
}
// Render markers
for ( var m in gmap\_m1798e62e1f470032f75187630fc4420d.positions ) {
gmap\_m1798e62e1f470032f75187630fc4420d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1798e62e1f470032f75187630fc4420d.map,
position : gmap\_m1798e62e1f470032f75187630fc4420d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1798e62e1f470032f75187630fc4420d.map.setCenter( gmap\_m1798e62e1f470032f75187630fc4420d.positions[978] );
});