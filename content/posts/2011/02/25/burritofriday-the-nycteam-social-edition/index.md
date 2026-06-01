---
title: ''
date: '2011-02-25T17:38:57+00:00'
format: image
tags:
- burritofriday
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/1390db3741fd428490c4d043c8a770e1_7.jpg?resize=607%2C607
---

[![#burritofriday the NYC/Team Social edition](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/1390db3741fd428490c4d043c8a770e1_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2011/02/25/burritofriday-the-nycteam-social-edition/) 

#burritofriday the NYC/Team Social edition





* #[burritofriday](http://dentedreality.com.au/tags/burritofriday/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/B16eR/) [5:38 pm, February 25, 2011](http://dentedreality.com.au/2011/02/25/burritofriday-the-nycteam-social-edition/ "5:38 pm") 
jQuery(document).ready(function(){
var gmap\_m9642e2b613b7bee0bd7843ec6e090c77 = {
positions : {
165 : new google.maps.LatLng( '40.725836919', '-73.994805515' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9642e2b613b7bee0bd7843ec6e090c77' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9642e2b613b7bee0bd7843ec6e090c77.positions ) {
gmap\_m9642e2b613b7bee0bd7843ec6e090c77.bounds.extend( gmap\_m9642e2b613b7bee0bd7843ec6e090c77.positions[m] );
}
// Render markers
for ( var m in gmap\_m9642e2b613b7bee0bd7843ec6e090c77.positions ) {
gmap\_m9642e2b613b7bee0bd7843ec6e090c77.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9642e2b613b7bee0bd7843ec6e090c77.map,
position : gmap\_m9642e2b613b7bee0bd7843ec6e090c77.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9642e2b613b7bee0bd7843ec6e090c77.map.setCenter( gmap\_m9642e2b613b7bee0bd7843ec6e090c77.positions[165] );
});