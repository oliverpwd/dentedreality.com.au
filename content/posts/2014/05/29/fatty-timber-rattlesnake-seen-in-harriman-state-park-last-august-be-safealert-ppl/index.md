---
title: ''
date: '2014-05-29T09:12:54+00:00'
format: image
service: instagram
tags:
- harriman
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/05/10358457_800744519937904_75383355_n.jpg?resize=640%2C640
---

[![Fatty Timber Rattlesnake seen in #Harriman State Park last August. Be safe/alert, ppl!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/05/10358457_800744519937904_75383355_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/05/29/fatty-timber-rattlesnake-seen-in-harriman-state-park-last-august-be-safealert-ppl/) 

Fatty Timber Rattlesnake seen in #Harriman State Park last August. Be safe/alert, ppl!





* #[harriman](http://dentedreality.com.au/tags/harriman/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/olWrz6CmIs/) [9:12 am, May 29, 2014](http://dentedreality.com.au/2014/05/29/fatty-timber-rattlesnake-seen-in-harriman-state-park-last-august-be-safealert-ppl/ "9:12 am") 
jQuery(document).ready(function(){
var gmap\_m4091327b44afd9d4bef46ead4ec4fc03 = {
positions : {
771 : new google.maps.LatLng( '41.204333333', '-74.176666667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4091327b44afd9d4bef46ead4ec4fc03' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4091327b44afd9d4bef46ead4ec4fc03.positions ) {
gmap\_m4091327b44afd9d4bef46ead4ec4fc03.bounds.extend( gmap\_m4091327b44afd9d4bef46ead4ec4fc03.positions[m] );
}
// Render markers
for ( var m in gmap\_m4091327b44afd9d4bef46ead4ec4fc03.positions ) {
gmap\_m4091327b44afd9d4bef46ead4ec4fc03.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4091327b44afd9d4bef46ead4ec4fc03.map,
position : gmap\_m4091327b44afd9d4bef46ead4ec4fc03.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4091327b44afd9d4bef46ead4ec4fc03.map.setCenter( gmap\_m4091327b44afd9d4bef46ead4ec4fc03.positions[771] );
});