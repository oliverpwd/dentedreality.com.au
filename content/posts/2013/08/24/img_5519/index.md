---
title: Geographer
date: '2013-08-24T19:00:03+00:00'
format: image
tags:
- bowery
- boweryballroom
- concert
- geographer
- live music
- newyork
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767764582_ae58202eb9_o.jpg?resize=607%2C452
---

[![IMG_5519](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767764582_ae58202eb9_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/08/24/img_5519/) 
# [Geographer](http://dentedreality.com.au/2013/08/24/img_5519/)





* #[bowery](http://dentedreality.com.au/tags/bowery/)
* #[boweryballroom](http://dentedreality.com.au/tags/boweryballroom/)
* #[concert](http://dentedreality.com.au/tags/concert/)
* #[geographer](http://dentedreality.com.au/tags/geographer/)
* #[live music](http://dentedreality.com.au/tags/live-music/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9767764582/) [7:00 pm, August 24, 2013](http://dentedreality.com.au/2013/08/24/img_5519/ "7:00 pm") 
jQuery(document).ready(function(){
var gmap\_mff8f6256c73322409d2f24ff6aac7f81 = {
positions : {
670 : new google.maps.LatLng( '40.7205', '-73.993667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mff8f6256c73322409d2f24ff6aac7f81' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mff8f6256c73322409d2f24ff6aac7f81.positions ) {
gmap\_mff8f6256c73322409d2f24ff6aac7f81.bounds.extend( gmap\_mff8f6256c73322409d2f24ff6aac7f81.positions[m] );
}
// Render markers
for ( var m in gmap\_mff8f6256c73322409d2f24ff6aac7f81.positions ) {
gmap\_mff8f6256c73322409d2f24ff6aac7f81.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mff8f6256c73322409d2f24ff6aac7f81.map,
position : gmap\_mff8f6256c73322409d2f24ff6aac7f81.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mff8f6256c73322409d2f24ff6aac7f81.map.setCenter( gmap\_mff8f6256c73322409d2f24ff6aac7f81.positions[670] );
});