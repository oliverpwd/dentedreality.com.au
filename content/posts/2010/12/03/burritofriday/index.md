---
title: ''
date: '2010-12-03T22:46:43+00:00'
format: image
service: instagram
tags:
- burritofriday
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/397858862d1d4e7684ba21452f030e29_7.jpg?resize=607%2C607
---

[![#burritofriday](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/397858862d1d4e7684ba21452f030e29_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2010/12/03/burritofriday/) 

#burritofriday





* #[burritofriday](http://dentedreality.com.au/tags/burritofriday/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/ctyO/) [10:46 pm, December 3, 2010](http://dentedreality.com.au/2010/12/03/burritofriday/ "10:46 pm") 
jQuery(document).ready(function(){
var gmap\_m60150715b5f29b1de54ab427a0831b85 = {
positions : {
994 : new google.maps.LatLng( '37.790371292', '-122.399939566' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m60150715b5f29b1de54ab427a0831b85' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m60150715b5f29b1de54ab427a0831b85.positions ) {
gmap\_m60150715b5f29b1de54ab427a0831b85.bounds.extend( gmap\_m60150715b5f29b1de54ab427a0831b85.positions[m] );
}
// Render markers
for ( var m in gmap\_m60150715b5f29b1de54ab427a0831b85.positions ) {
gmap\_m60150715b5f29b1de54ab427a0831b85.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m60150715b5f29b1de54ab427a0831b85.map,
position : gmap\_m60150715b5f29b1de54ab427a0831b85.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m60150715b5f29b1de54ab427a0831b85.map.setCenter( gmap\_m60150715b5f29b1de54ab427a0831b85.positions[994] );
});