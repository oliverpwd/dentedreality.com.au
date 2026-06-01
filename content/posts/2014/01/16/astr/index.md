---
title: ASTR
date: '2014-01-16T18:00:51+00:00'
format: image
service: flickr
tags:
- astr
- live
- music
- newyork
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13926945785_51a81644ec_o.jpg?resize=607%2C455
---

[![ASTR](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13926945785_51a81644ec_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/01/16/astr/) 
# [ASTR](http://dentedreality.com.au/2014/01/16/astr/)





* #[astr](http://dentedreality.com.au/tags/astr/)
* #[live](http://dentedreality.com.au/tags/live/)
* #[music](http://dentedreality.com.au/tags/music/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13926945785/) [6:00 pm, January 16, 2014](http://dentedreality.com.au/2014/01/16/astr/ "6:00 pm") 
jQuery(document).ready(function(){
var gmap\_mbfd026711cfe930b448219c98068f6b9 = {
positions : {
4 : new google.maps.LatLng( '40.729888', '-74.009956' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbfd026711cfe930b448219c98068f6b9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbfd026711cfe930b448219c98068f6b9.positions ) {
gmap\_mbfd026711cfe930b448219c98068f6b9.bounds.extend( gmap\_mbfd026711cfe930b448219c98068f6b9.positions[m] );
}
// Render markers
for ( var m in gmap\_mbfd026711cfe930b448219c98068f6b9.positions ) {
gmap\_mbfd026711cfe930b448219c98068f6b9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbfd026711cfe930b448219c98068f6b9.map,
position : gmap\_mbfd026711cfe930b448219c98068f6b9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbfd026711cfe930b448219c98068f6b9.map.setCenter( gmap\_mbfd026711cfe930b448219c98068f6b9.positions[4] );
});