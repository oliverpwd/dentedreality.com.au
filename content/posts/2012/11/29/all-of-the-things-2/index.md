---
title: ''
date: '2012-11-29T17:26:00+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/5eceb00c3a6b11e2b74c22000a9f1427_7.jpg?resize=607%2C607
---

[![All of the things.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/5eceb00c3a6b11e2b74c22000a9f1427_7.jpg?resize=607%2C607)](http://dentedreality.com.au/2012/11/29/all-of-the-things-2/) 

All of the things.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/SoOOFrCmMy/) [5:26 pm, November 29, 2012](http://dentedreality.com.au/2012/11/29/all-of-the-things-2/ "5:26 pm") 
jQuery(document).ready(function(){
var gmap\_ma5fe47cce39031fd41cf89ee15ac56e7 = {
positions : {
696 : new google.maps.LatLng( '29.959108275', '-90.060533746' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma5fe47cce39031fd41cf89ee15ac56e7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma5fe47cce39031fd41cf89ee15ac56e7.positions ) {
gmap\_ma5fe47cce39031fd41cf89ee15ac56e7.bounds.extend( gmap\_ma5fe47cce39031fd41cf89ee15ac56e7.positions[m] );
}
// Render markers
for ( var m in gmap\_ma5fe47cce39031fd41cf89ee15ac56e7.positions ) {
gmap\_ma5fe47cce39031fd41cf89ee15ac56e7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma5fe47cce39031fd41cf89ee15ac56e7.map,
position : gmap\_ma5fe47cce39031fd41cf89ee15ac56e7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma5fe47cce39031fd41cf89ee15ac56e7.map.setCenter( gmap\_ma5fe47cce39031fd41cf89ee15ac56e7.positions[696] );
});