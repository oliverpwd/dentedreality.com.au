---
title: Dad, No Beard
date: '2014-03-15T07:08:21+00:00'
format: image
service: flickr
tags:
- craig
- dad
- perth
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904711266_bc6048df03_o.jpg?resize=607%2C455
---

[![Dad, No Beard](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904711266_bc6048df03_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/15/dad-no-beard/) 
# [Dad, No Beard](http://dentedreality.com.au/2014/03/15/dad-no-beard/)

Perth, Mooloolaba and Melbourne





* #[craig](http://dentedreality.com.au/tags/craig/)
* #[dad](http://dentedreality.com.au/tags/dad/)
* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904711266/) [7:08 am, March 15, 2014](http://dentedreality.com.au/2014/03/15/dad-no-beard/ "7:08 am") 
jQuery(document).ready(function(){
var gmap\_ma4968521dacf91e52db488aaf55b6bbb = {
positions : {
350 : new google.maps.LatLng( '-32.055425', '115.746788' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma4968521dacf91e52db488aaf55b6bbb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma4968521dacf91e52db488aaf55b6bbb.positions ) {
gmap\_ma4968521dacf91e52db488aaf55b6bbb.bounds.extend( gmap\_ma4968521dacf91e52db488aaf55b6bbb.positions[m] );
}
// Render markers
for ( var m in gmap\_ma4968521dacf91e52db488aaf55b6bbb.positions ) {
gmap\_ma4968521dacf91e52db488aaf55b6bbb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma4968521dacf91e52db488aaf55b6bbb.map,
position : gmap\_ma4968521dacf91e52db488aaf55b6bbb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma4968521dacf91e52db488aaf55b6bbb.map.setCenter( gmap\_ma4968521dacf91e52db488aaf55b6bbb.positions[350] );
});