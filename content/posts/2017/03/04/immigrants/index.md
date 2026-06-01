---
title: ''
date: '2017-03-04T14:50:09+00:00'
format: image
service: instagram
tags:
- immigrants
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/03/17077019_1395087043875663_2664920636144484352_n.jpg?fit=640%2C640
---

[![#immigrants](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/03/17077019_1395087043875663_2664920636144484352_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2017/03/04/immigrants/) 

#immigrants





* #[immigrants](http://dentedreality.com.au/tags/immigrants/)

Posted on [Instagram](https://www.instagram.com/p/BRO14ivB7kb/) [2:50 pm, March 4, 2017](http://dentedreality.com.au/2017/03/04/immigrants/ "2:50 pm") 
jQuery(document).ready(function(){
var gmap\_m257573dd0cbab736fdcb1cf89db7b13b = {
positions : {
996 : new google.maps.LatLng( '39.747694765574', '-104.98420639855' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m257573dd0cbab736fdcb1cf89db7b13b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m257573dd0cbab736fdcb1cf89db7b13b.positions ) {
gmap\_m257573dd0cbab736fdcb1cf89db7b13b.bounds.extend( gmap\_m257573dd0cbab736fdcb1cf89db7b13b.positions[m] );
}
// Render markers
for ( var m in gmap\_m257573dd0cbab736fdcb1cf89db7b13b.positions ) {
gmap\_m257573dd0cbab736fdcb1cf89db7b13b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m257573dd0cbab736fdcb1cf89db7b13b.map,
position : gmap\_m257573dd0cbab736fdcb1cf89db7b13b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m257573dd0cbab736fdcb1cf89db7b13b.map.setCenter( gmap\_m257573dd0cbab736fdcb1cf89db7b13b.positions[996] );
});