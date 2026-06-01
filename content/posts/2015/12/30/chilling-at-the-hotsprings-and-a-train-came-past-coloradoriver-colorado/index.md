---
title: ''
date: '2015-12-30T16:42:22+00:00'
format: image
service: instagram
tags:
- colorado
- coloradoriver
- hotsprings
- train
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/12/10261079_1099076246793903_42296560_n.jpg?fit=640%2C640
---

[![Chilling at the #hotsprings and a #train came past. #coloradoriver #colorado](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/12/10261079_1099076246793903_42296560_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2015/12/30/chilling-at-the-hotsprings-and-a-train-came-past-coloradoriver-colorado/) 

Chilling at the #hotsprings and a #train came past. #coloradoriver #colorado





* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[coloradoriver](http://dentedreality.com.au/tags/coloradoriver/)
* #[hotsprings](http://dentedreality.com.au/tags/hotsprings/)
* #[train](http://dentedreality.com.au/tags/train/)

Posted on [Instagram](https://www.instagram.com/p/_706OLCmP4/) [4:42 pm, December 30, 2015](http://dentedreality.com.au/2015/12/30/chilling-at-the-hotsprings-and-a-train-came-past-coloradoriver-colorado/ "4:42 pm") 
jQuery(document).ready(function(){
var gmap\_m37447611cf67779d4353845beb8884aa = {
positions : {
47 : new google.maps.LatLng( '39.953158', '-106.547003' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m37447611cf67779d4353845beb8884aa' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m37447611cf67779d4353845beb8884aa.positions ) {
gmap\_m37447611cf67779d4353845beb8884aa.bounds.extend( gmap\_m37447611cf67779d4353845beb8884aa.positions[m] );
}
// Render markers
for ( var m in gmap\_m37447611cf67779d4353845beb8884aa.positions ) {
gmap\_m37447611cf67779d4353845beb8884aa.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m37447611cf67779d4353845beb8884aa.map,
position : gmap\_m37447611cf67779d4353845beb8884aa.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m37447611cf67779d4353845beb8884aa.map.setCenter( gmap\_m37447611cf67779d4353845beb8884aa.positions[47] );
});