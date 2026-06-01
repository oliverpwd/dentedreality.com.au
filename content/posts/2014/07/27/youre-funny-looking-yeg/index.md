---
title: ''
date: '2014-07-27T11:13:00+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/07/10543570_709697829066170_609419314_n.jpg?resize=640%2C640
---

[![You're funny looking, YEG.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/07/10543570_709697829066170_609419314_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/07/27/youre-funny-looking-yeg/) 

You’re funny looking, YEG.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/q9fVDSCmGR/) [11:13 am, July 27, 2014](http://dentedreality.com.au/2014/07/27/youre-funny-looking-yeg/ "11:13 am") 
jQuery(document).ready(function(){
var gmap\_m5934527b6b10a623a80917da2471833e = {
positions : {
4 : new google.maps.LatLng( '53.307396957', '-113.584170182' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5934527b6b10a623a80917da2471833e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5934527b6b10a623a80917da2471833e.positions ) {
gmap\_m5934527b6b10a623a80917da2471833e.bounds.extend( gmap\_m5934527b6b10a623a80917da2471833e.positions[m] );
}
// Render markers
for ( var m in gmap\_m5934527b6b10a623a80917da2471833e.positions ) {
gmap\_m5934527b6b10a623a80917da2471833e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5934527b6b10a623a80917da2471833e.map,
position : gmap\_m5934527b6b10a623a80917da2471833e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5934527b6b10a623a80917da2471833e.map.setCenter( gmap\_m5934527b6b10a623a80917da2471833e.positions[4] );
});