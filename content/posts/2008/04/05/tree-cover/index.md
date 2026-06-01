---
title: Tree-cover
date: '2008-04-05T18:32:52+00:00'
format: image
service: flickr
tags:
- australia
- renniewedding
- timswedding
- trees
- wallpaper
- westernaustraliadenmark
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2432623777_a0f5689575_o.jpg?resize=607%2C379
---

[![Tree-cover](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2432623777_a0f5689575_o.jpg?resize=607%2C379)](http://dentedreality.com.au/2008/04/05/tree-cover/) 
# [Tree-cover](http://dentedreality.com.au/2008/04/05/tree-cover/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[renniewedding](http://dentedreality.com.au/tags/renniewedding/)
* #[timswedding](http://dentedreality.com.au/tags/timswedding/)
* #[trees](http://dentedreality.com.au/tags/trees/)
* #[wallpaper](http://dentedreality.com.au/tags/wallpaper/)
* #[westernaustraliadenmark](http://dentedreality.com.au/tags/westernaustraliadenmark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2432623777/) [6:32 pm, April 5, 2008](http://dentedreality.com.au/2008/04/05/tree-cover/ "6:32 pm") 
jQuery(document).ready(function(){
var gmap\_mc1cbb4838e5651a4ef9206f7e7790d66 = {
positions : {
631 : new google.maps.LatLng( '-34.983877', '117.298278' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc1cbb4838e5651a4ef9206f7e7790d66' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc1cbb4838e5651a4ef9206f7e7790d66.positions ) {
gmap\_mc1cbb4838e5651a4ef9206f7e7790d66.bounds.extend( gmap\_mc1cbb4838e5651a4ef9206f7e7790d66.positions[m] );
}
// Render markers
for ( var m in gmap\_mc1cbb4838e5651a4ef9206f7e7790d66.positions ) {
gmap\_mc1cbb4838e5651a4ef9206f7e7790d66.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc1cbb4838e5651a4ef9206f7e7790d66.map,
position : gmap\_mc1cbb4838e5651a4ef9206f7e7790d66.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc1cbb4838e5651a4ef9206f7e7790d66.map.setCenter( gmap\_mc1cbb4838e5651a4ef9206f7e7790d66.positions[631] );
});