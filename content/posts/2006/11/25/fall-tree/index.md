---
title: Fall Tree
date: '2006-11-25T12:10:46+00:00'
format: image
service: flickr
tags:
- bigsur
- bottchersgap
- california
- colors
- fall
- lospadresnationalpark
- tree
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/11/308096029_ba195ec5ff_o.jpg?resize=607%2C455
---

[![Fall Tree](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/11/308096029_ba195ec5ff_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/11/25/fall-tree/) 
# [Fall Tree](http://dentedreality.com.au/2006/11/25/fall-tree/)

Awesome colors – everything from bright yellow through brown, red, gold, to rich, dark greens.





* #[bigsur](http://dentedreality.com.au/tags/bigsur/)
* #[bottchersgap](http://dentedreality.com.au/tags/bottchersgap/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[colors](http://dentedreality.com.au/tags/colors/)
* #[fall](http://dentedreality.com.au/tags/fall/)
* #[lospadresnationalpark](http://dentedreality.com.au/tags/lospadresnationalpark/)
* #[tree](http://dentedreality.com.au/tags/tree/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/308096029/) [12:10 pm, November 25, 2006](http://dentedreality.com.au/2006/11/25/fall-tree/ "12:10 pm") 
jQuery(document).ready(function(){
var gmap\_m08464be33096979898ae209966e1af7b = {
positions : {
523 : new google.maps.LatLng( '36.34389', '-121.776409' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m08464be33096979898ae209966e1af7b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m08464be33096979898ae209966e1af7b.positions ) {
gmap\_m08464be33096979898ae209966e1af7b.bounds.extend( gmap\_m08464be33096979898ae209966e1af7b.positions[m] );
}
// Render markers
for ( var m in gmap\_m08464be33096979898ae209966e1af7b.positions ) {
gmap\_m08464be33096979898ae209966e1af7b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m08464be33096979898ae209966e1af7b.map,
position : gmap\_m08464be33096979898ae209966e1af7b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m08464be33096979898ae209966e1af7b.map.setCenter( gmap\_m08464be33096979898ae209966e1af7b.positions[523] );
});