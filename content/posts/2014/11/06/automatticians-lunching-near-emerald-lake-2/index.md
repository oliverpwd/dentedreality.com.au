---
title: ''
date: '2014-11-06T22:51:17+00:00'
format: image
service: instagram
tags:
- photo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/927379_671322516315618_2043547096_n.jpg?resize=640%2C640
---

[![Automatticians lunching near Emerald Lake.](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/11/927379_671322516315618_2043547096_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/11/06/automatticians-lunching-near-emerald-lake-2/) 

Automatticians lunching near Emerald Lake.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/vFmDngimOX/) [10:51 pm, November 6, 2014](http://dentedreality.com.au/2014/11/06/automatticians-lunching-near-emerald-lake-2/ "10:51 pm") 
jQuery(document).ready(function(){
var gmap\_m27c048ddb74fa65290648e64d6322279 = {
positions : {
756 : new google.maps.LatLng( '40.441003729', '-105.754434474' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m27c048ddb74fa65290648e64d6322279' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m27c048ddb74fa65290648e64d6322279.positions ) {
gmap\_m27c048ddb74fa65290648e64d6322279.bounds.extend( gmap\_m27c048ddb74fa65290648e64d6322279.positions[m] );
}
// Render markers
for ( var m in gmap\_m27c048ddb74fa65290648e64d6322279.positions ) {
gmap\_m27c048ddb74fa65290648e64d6322279.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m27c048ddb74fa65290648e64d6322279.map,
position : gmap\_m27c048ddb74fa65290648e64d6322279.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m27c048ddb74fa65290648e64d6322279.map.setCenter( gmap\_m27c048ddb74fa65290648e64d6322279.positions[756] );
});