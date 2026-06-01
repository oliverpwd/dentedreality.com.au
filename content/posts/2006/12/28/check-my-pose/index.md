---
title: Check my pose
date: '2006-12-28T18:13:09+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- boat
- glasses
- hat
- island
- me
- phuket
- thailand
- thailand06
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348098444_491856f316_o.jpg?resize=607%2C809
---

[![Check my pose](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/348098444_491856f316_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2006/12/28/check-my-pose/) 
# [Check my pose](http://dentedreality.com.au/2006/12/28/check-my-pose/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[boat](http://dentedreality.com.au/tags/boat/)
* #[glasses](http://dentedreality.com.au/tags/glasses/)
* #[hat](http://dentedreality.com.au/tags/hat/)
* #[island](http://dentedreality.com.au/tags/island/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348098444/) [6:13 pm, December 28, 2006](http://dentedreality.com.au/2006/12/28/check-my-pose/ "6:13 pm") 
jQuery(document).ready(function(){
var gmap\_m91af15f2ea9a9dc9df2f0f0ffb074ed7 = {
positions : {
133 : new google.maps.LatLng( '8.095005', '98.457927' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m91af15f2ea9a9dc9df2f0f0ffb074ed7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m91af15f2ea9a9dc9df2f0f0ffb074ed7.positions ) {
gmap\_m91af15f2ea9a9dc9df2f0f0ffb074ed7.bounds.extend( gmap\_m91af15f2ea9a9dc9df2f0f0ffb074ed7.positions[m] );
}
// Render markers
for ( var m in gmap\_m91af15f2ea9a9dc9df2f0f0ffb074ed7.positions ) {
gmap\_m91af15f2ea9a9dc9df2f0f0ffb074ed7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m91af15f2ea9a9dc9df2f0f0ffb074ed7.map,
position : gmap\_m91af15f2ea9a9dc9df2f0f0ffb074ed7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m91af15f2ea9a9dc9df2f0f0ffb074ed7.map.setCenter( gmap\_m91af15f2ea9a9dc9df2f0f0ffb074ed7.positions[133] );
});